import { appendFileSync, existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { config, getAgent } from "./config.mjs";

const relayDir = resolve(".relay");
const inboxFile = resolve(relayDir, "inbox.jsonl");
const cursorFile = resolve(relayDir, "cursor.json");

function log(message) {
  console.log(`[${new Date().toISOString()}] ${message}`);
}

function ensureRelayDirectory() {
  mkdirSync(relayDir, { recursive: true });
}

function readCursor() {
  if (!existsSync(cursorFile)) return 0;
  try {
    return Number(JSON.parse(readFileSync(cursorFile, "utf8")).offset) || 0;
  } catch {
    return 0;
  }
}

function writeCursor(offset) {
  ensureRelayDirectory();
  writeFileSync(cursorFile, JSON.stringify({ offset }));
}

function telegramClient(token) {
  const endpoint = `https://api.telegram.org/bot${token}`;
  return {
    async call(method, payload = {}) {
      const response = await fetch(`${endpoint}/${method}`, {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(payload),
      });
      const result = await response.json().catch(() => ({}));
      if (!response.ok || !result.ok) throw new Error(result.description || `Telegram ${method} failed`);
      return result.result;
    },
  };
}

function parseOptions(args) {
  const options = {};
  const rest = [];
  for (let index = 0; index < args.length; index += 1) {
    const value = args[index];
    if (value.startsWith("--") && args[index + 1]) {
      options[value.slice(2)] = args[index + 1];
      index += 1;
    } else {
      rest.push(value);
    }
  }
  return { options, rest };
}

async function post(args) {
  const { options, rest } = parseOptions(args);
  const agentName = options.agent || "codex";
  const kind = (options.kind || "update").toUpperCase();
  const message = options.message || rest.join(" ");
  if (!message) throw new Error("A message is required. Use --message \"...\".");

  const agent = getAgent(agentName);
  const telegram = telegramClient(agent.token);
  await telegram.call("sendMessage", {
    chat_id: config.groupId,
    text: `[${agent.label} · ${kind}]\n${message}`,
  });
  log(`Posted ${kind.toLowerCase()} as ${agentName}.`);
}

function recordIncoming(message) {
  if (!message?.text || message.from?.is_bot || String(message.chat?.id) !== String(config.groupId)) return;
  ensureRelayDirectory();
  appendFileSync(inboxFile, `${JSON.stringify({
    receivedAt: new Date().toISOString(),
    messageId: message.message_id,
    sender: message.from?.username || message.from?.first_name || "unknown",
    text: message.text,
  })}\n`);
  log(`Recorded group message #${message.message_id} in the shared inbox.`);
}

async function listen(args) {
  const { options } = parseOptions(args);
  const agent = getAgent("codex");
  const telegram = telegramClient(agent.token);
  const bot = await telegram.call("getMe");
  let offset = readCursor();
  log(`Listening as @${bot.username}; writing the shared inbox to ${inboxFile}.`);

  do {
    const updates = await telegram.call("getUpdates", {
      offset,
      timeout: options.once ? 0 : 30,
      allowed_updates: ["message"],
    });
    for (const update of updates) {
      offset = update.update_id + 1;
      writeCursor(offset);
      recordIncoming(update.message);
    }
  } while (!options.once);
}

function readInbox(args) {
  const { options } = parseOptions(args);
  const limit = Math.max(1, Number(options.limit) || 20);
  if (!existsSync(inboxFile)) {
    console.log("No group messages have been recorded yet.");
    return;
  }
  const entries = readFileSync(inboxFile, "utf8").trim().split("\n").filter(Boolean).slice(-limit);
  for (const entry of entries) {
    const message = JSON.parse(entry);
    console.log(`[${message.receivedAt}] ${message.sender}: ${message.text}`);
  }
}

function help() {
  console.log(`Usage:
  npm run relay -- post --agent codex --kind update --message "Implemented X"
  npm run relay -- post --agent claude --kind handoff --message "Please review Y"
  npm run relay -- listen
  npm run relay -- read --limit 20`);
}

const [command, ...args] = process.argv.slice(2);
try {
  if (command === "post") await post(args);
  else if (command === "listen") await listen(args);
  else if (command === "read") readInbox(args);
  else help();
} catch (error) {
  console.error(`Relay error: ${error.message}`);
  process.exitCode = 1;
}
