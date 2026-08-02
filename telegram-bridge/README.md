# Barebones Telegram bridge

This is a lightweight local bridge between one Telegram bot and the OpenAI Responses API. It uses long polling, so it works from a Mac without a public URL or a paid hosting service.

It is a separate API-backed chat participant, not a remote control for a live Codex or Claude session. It cannot inspect the repository, run commands, or automatically relay private agent-session messages. Use GitHub issue #1 for durable work tracking.

## Configure

The OpenAI key is loaded from the local root file `openaiapi.env.txt`, which must contain:

```env
OPENAI_API_KEY=...
```

Create a second local file at the repository root called `telegram-bridge.env.txt`
(or `telegram-bridge.env` if you prefer):

```env
TELEGRAM_BOT_TOKEN=...
TELEGRAM_ALLOWED_CHAT_ID=
OPENAI_MODEL=gpt-5-mini
BOT_LABEL=Barebones Codex
TELEGRAM_REQUIRE_TRIGGER=true
```

Both files are ignored by Git. Never commit or share the bot/API tokens.

If you keep a private test-chat ID too, put the real group in
`TELEGRAM_ALLOWED_GROUP_ID`; it takes precedence over `TELEGRAM_ALLOWED_CHAT_ID`.

If you run the bridge from a separate Git worktree while keeping secrets in
another local checkout, set `BRIDGE_ENV_FILE` to the absolute path of the file
that contains `OPENAI_API_KEY` instead of copying the key.

## First run

Requires Node.js 18 or later. There are no npm dependencies to install.

```sh
cd telegram-bridge
npm run check
npm start
```

With `TELEGRAM_ALLOWED_CHAT_ID` blank, the bot ignores all normal messages. Send `/id@your_bot_username` in the intended Telegram group; the bot replies with the group ID. Put that value in `telegram-bridge.env`, stop the bridge with `Ctrl+C`, and start it again.

In a group, trigger it with one of:

```text
/codex What should we work on next?
/ask Summarise the current handoff.
@your_bot_username What is our next task?
/reset
```

`/reset` clears the small in-memory conversation context for that group. The bot only responds in the configured group. A group ID typically starts with `-100`.

## Keep it running

Leave `npm start` running in a terminal while you want the bot online. Only one long-polling instance should use a bot token at a time. For always-on operation, deploy the same code to a host with a persistent process, then move the local environment variables to that host's secret store.
