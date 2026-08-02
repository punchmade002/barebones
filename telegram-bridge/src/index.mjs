import { config, configurationErrors } from "./config.mjs";

const MAX_HISTORY_ITEMS = 12;
const TELEGRAM_MESSAGE_LIMIT = 4000;
const historyByChat = new Map();

function log(message) {
  console.log(`[${new Date().toISOString()}] ${message}`);
}

async function requestJson(url, options) {
  const response = await fetch(url, options);
  const payload = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(payload?.description || payload?.error?.message || `HTTP ${response.status}`);
  }
  return payload;
}

function createTelegramClient(token) {
  const endpoint = `https://api.telegram.org/bot${token}`;

  return {
    async call(method, payload = {}) {
      const result = await requestJson(`${endpoint}/${method}`, {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(payload),
      });
      if (!result.ok) throw new Error(result.description || `Telegram ${method} failed`);
      return result.result;
    },
  };
}

async function createOpenAIResponse(chatId, userText) {
  const history = historyByChat.get(chatId) || [];
  const input = [...history, { role: "user", content: userText }];
  const result = await requestJson("https://api.openai.com/v1/responses", {
    method: "POST",
    headers: {
      authorization: `Bearer ${config.openaiApiKey}`,
      "content-type": "application/json",
    },
    body: JSON.stringify({
      model: config.model,
      store: false,
      instructions: [
        `You are ${config.botLabel}, a helpful participant in the Barebones project Telegram group.`,
        "Be concise and candid. You may discuss plans, status, and handoffs.",
        "You do not have direct access to the repository, GitHub, the other agent's session, or this user's private data. Never claim you performed an action unless it was described in this chat.",
      ].join(" "),
      input,
    }),
  });

  const answer = result.output_text?.trim() || "I wasn't able to produce a text reply.";
  const nextHistory = [...input, { role: "assistant", content: answer }].slice(-MAX_HISTORY_ITEMS);
  historyByChat.set(chatId, nextHistory);
  return answer;
}

function splitMessage(text) {
  const chunks = [];
  let remaining = text;
  while (remaining.length > TELEGRAM_MESSAGE_LIMIT) {
    let boundary = remaining.lastIndexOf("\n", TELEGRAM_MESSAGE_LIMIT);
    if (boundary < TELEGRAM_MESSAGE_LIMIT / 2) boundary = TELEGRAM_MESSAGE_LIMIT;
    chunks.push(remaining.slice(0, boundary));
    remaining = remaining.slice(boundary).trimStart();
  }
  if (remaining) chunks.push(remaining);
  return chunks;
}

async function reply(telegram, message, text) {
  for (const chunk of splitMessage(text)) {
    await telegram.call("sendMessage", {
      chat_id: message.chat.id,
      text: chunk,
      reply_to_message_id: message.message_id,
    });
  }
}

function commandText(text, username) {
  const command = text.match(/^\/(?:codex|ask)(?:@[^\s]+)?\s*([\s\S]*)$/i);
  if (command) return command[1].trim();

  const mention = username && text.match(new RegExp(`^@${username.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}\\b[,:]?\\s*([\\s\\S]*)$`, "i"));
  return mention ? mention[1].trim() : null;
}

function isAllowedChat(chatId) {
  return Boolean(config.allowedChatId) && String(chatId) === String(config.allowedChatId);
}

async function handleMessage(telegram, bot, message) {
  if (!message?.text || message.from?.is_bot) return;

  const text = message.text.trim();
  if (/^\/id(?:@[^\s]+)?\s*$/i.test(text)) {
    await reply(telegram, message, `This chat's ID is \`${message.chat.id}\`. Add it as TELEGRAM_ALLOWED_CHAT_ID, then restart me.`);
    return;
  }

  if (!isAllowedChat(message.chat.id)) return;

  if (/^\/(?:reset|new)(?:@[^\s]+)?\s*$/i.test(text)) {
    historyByChat.delete(message.chat.id);
    await reply(telegram, message, "Conversation context cleared.");
    return;
  }

  const prompt = config.requireTrigger ? commandText(text, bot.username) : text;
  if (!prompt) return;

  if (!prompt.trim()) {
    await reply(telegram, message, "Ask a question after `/codex`, `/ask`, or mention me directly.");
    return;
  }

  try {
    const answer = await createOpenAIResponse(message.chat.id, prompt);
    await reply(telegram, message, answer);
  } catch (error) {
    log(`OpenAI reply failed: ${error.message}`);
    await reply(telegram, message, "I couldn't complete that request. Check the bridge terminal for the error details.");
  }
}

async function run() {
  const errors = configurationErrors();
  if (errors.length) throw new Error(errors.join("; "));

  const telegram = createTelegramClient(config.telegramBotToken);
  const bot = await telegram.call("getMe");
  log(`Connected as @${bot.username}. Model: ${config.model}.`);

  if (!config.allowedChatId) {
    log("No TELEGRAM_ALLOWED_CHAT_ID configured. Send /id in the target group, set the returned ID, then restart. Other messages are ignored.");
  }

  let offset = 0;
  for (;;) {
    try {
      const updates = await telegram.call("getUpdates", {
        offset,
        timeout: 30,
        allowed_updates: ["message"],
      });
      for (const update of updates) {
        offset = update.update_id + 1;
        await handleMessage(telegram, bot, update.message);
      }
    } catch (error) {
      log(`Polling error: ${error.message}. Retrying in 3 seconds.`);
      await new Promise((resolve) => setTimeout(resolve, 3000));
    }
  }
}

if (process.argv.includes("--check")) {
  const errors = configurationErrors({ requireTelegram: false });
  if (errors.length) {
    console.error(`Configuration incomplete: ${errors.join("; ")}`);
    process.exitCode = 1;
  } else {
    console.log(`OpenAI configuration present. Model: ${config.model}`);
  }
} else {
  run().catch((error) => {
    console.error(`Bridge could not start: ${error.message}`);
    process.exitCode = 1;
  });
}
