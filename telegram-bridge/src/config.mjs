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
    if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) value = value.slice(1, -1);
    values[key] = value;
  }
  return values;
}

function loadLocalEnv() {
  const values = {};
  const sources = [
    process.env.BRIDGE_ENV_FILE,
    resolve(repositoryRoot, "telegram-bridge.env"),
    resolve(repositoryRoot, "telegram-bridge.env.txt"),
    resolve(repositoryRoot, "openaiapi.env.txt"),
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
const groupId = get("TELEGRAM_ALLOWED_GROUP_ID") || get("TELEGRAM_ALLOWED_CHAT_ID_CODEX") || get("TELEGRAM_ALLOWED_CHAT_ID");

export const config = Object.freeze({
  groupId,
  agents: Object.freeze({
    codex: Object.freeze({
      label: get("TELEGRAM_CODEX_BOT_LABEL", "Barebones Codex"),
      token: get("TELEGRAM_CODEX_BOT_TOKEN") || get("TELEGRAM_BOT_TOKEN"),
    }),
    claude: Object.freeze({
      label: get("TELEGRAM_CLAUDE_BOT_LABEL", "Barebones Claude"),
      token: get("TELEGRAM_CLAUDE_BOT_TOKEN"),
    }),
  }),
});

export function getAgent(agentName) {
  const agent = config.agents[agentName];
  if (!agent) throw new Error(`Unknown agent '${agentName}'. Use codex or claude.`);
  if (!agent.token) throw new Error(`Missing Telegram token for ${agentName}.`);
  if (!config.groupId) throw new Error("Missing TELEGRAM_ALLOWED_GROUP_ID.");
  return agent;
}
