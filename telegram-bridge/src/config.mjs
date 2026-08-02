import { existsSync, readFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const bridgeRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const repositoryRoot = resolve(bridgeRoot, "..");

function parseEnv(text) {
  const values = {};

  for (const rawLine of text.split(/\r?\n/)) {
    const line = rawLine.trim();
    if (!line || line.startsWith("#")) continue;

    const separator = line.indexOf("=");
    if (separator < 1) continue;

    const key = line.slice(0, separator).trim();
    let value = line.slice(separator + 1).trim();
    if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }
    values[key] = value;
  }

  return values;
}

function loadLocalEnv() {
  const values = {};
  const sources = [
    process.env.BRIDGE_ENV_FILE,
    resolve(repositoryRoot, "openaiapi.env.txt"),
    resolve(repositoryRoot, "telegram-bridge.env"),
    resolve(bridgeRoot, ".env"),
  ];

  for (const source of sources) {
    if (!source || !existsSync(source)) continue;
    Object.assign(values, parseEnv(readFileSync(source, "utf8")));
  }

  return values;
}

const localEnv = loadLocalEnv();
const get = (name, fallback = "") => process.env[name] ?? localEnv[name] ?? fallback;

export const config = Object.freeze({
  openaiApiKey: get("OPENAI_API_KEY"),
  telegramBotToken: get("TELEGRAM_BOT_TOKEN"),
  allowedChatId: get("TELEGRAM_ALLOWED_CHAT_ID"),
  model: get("OPENAI_MODEL", "gpt-5-mini"),
  botLabel: get("BOT_LABEL", "Barebones Codex"),
  requireTrigger: get("TELEGRAM_REQUIRE_TRIGGER", "true").toLowerCase() !== "false",
});

export function configurationErrors({ requireTelegram = true } = {}) {
  const errors = [];
  if (!config.openaiApiKey) errors.push("OPENAI_API_KEY is missing");
  if (requireTelegram && !config.telegramBotToken) errors.push("TELEGRAM_BOT_TOKEN is missing");
  return errors;
}
