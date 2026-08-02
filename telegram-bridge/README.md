# Barebones Telegram relay

This is a free Telegram coordination relay for Codex, Claude, and the project owner. It does **not** call OpenAI, Anthropic, or any other model API. GitHub remains the durable source of truth for tasks, commits, and reviews.

The relay has two jobs:

- Post labelled progress, handoff, blocker, and question messages through either agent's Telegram bot.
- Listen through the Codex bot and write human group messages to a shared local inbox, which active agents can read.

It cannot wake an inactive agent. An active agent should check the inbox at the start of work and after a Telegram notification.

## Local configuration

Keep this in the ignored root file `openaiapi.env.txt` or `telegram-bridge.env.txt` (the OpenAI key is no longer used by this relay):

```env
TELEGRAM_CODEX_BOT_TOKEN=...
TELEGRAM_CLAUDE_BOT_TOKEN=...
TELEGRAM_ALLOWED_GROUP_ID=-1001234567890
TELEGRAM_CODEX_BOT_LABEL=Barebones Codex
TELEGRAM_CLAUDE_BOT_LABEL=Barebones Claude
```

The current Codex token can stay under the older name `TELEGRAM_BOT_TOKEN`, but the explicit name above is clearer. Never commit or share either token.

For the inbox listener to capture normal group messages, use BotFather's `/setprivacy` command and disable privacy mode for the Codex bot. Otherwise, tag `@codex_barebones_bot` or use a command when you need an agent to see a message.

## Run

Requires Node.js 18+ and no npm install.

```sh
cd telegram-bridge
npm run check
npm start
```

`npm start` is the long-running inbox listener. It writes local, ignored data to `.relay/inbox.jsonl`; keep one listener instance only.

Post a status update:

```sh
npm run relay -- post --agent codex --kind update --message "Implemented the Telegram relay."
npm run relay -- post --agent claude --kind handoff --message "Please review the bridge configuration."
```

Read recent human group messages:

```sh
npm run relay -- read --limit 20
```

## Working agreement

- Post material changes, blockers, questions, and handoffs to Telegram using the agent's bot identity.
- The Codex listener writes incoming human messages to the shared inbox; agents read it before selecting work.
- Keep GitHub issue #1 and focused commits/PRs as the permanent task trail.
