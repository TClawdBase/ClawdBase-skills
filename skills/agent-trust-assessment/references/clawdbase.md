# Clawdbase registry and scoring

## Resolve and assess

1. Discover the Clawdbase MCP server's directory search, operation listing and relevant score tool using the agent's tool interface. `search_directory` returns existing public evidence; `list_operations` gives current operation names, scopes and pricing. If an exact hyphenated name returns no matches, search a distinctive component and filter by exact name and entity type.
2. Compare `stableKey`, `canonicalHref`, repository and creator when available. A name or repository can have separate agent and skill records or multiple matching records. If more than one is plausible, ask the user to choose. Use the canonical subject accepted by the chosen operation.
3. For a requested fresh MCP score, invoke the relevant score tool with the selected subject and a new UUID idempotency key, if supported by its current schema. Inspect the actual schema before calling. Check the returned resolved subject, Trust and Confidence, verification, evidence, charge source and settlement. Reuse the same UUID for retries of the same operation. A successful free-tier call may consume an included free call.
4. Compare a fresh result with the public snapshot without assuming differing values are an error. For identity assessments, `persisted_to_page` can be `false`, and evidence version or freshness can be unknown. `received_at` is a receipt time, not proof of evidence freshness. If accessible, reread the exact record to verify persistence.

## REST operation

The current [REST API contract](https://www.clawdbase.ai/docs/developers/rest-api) documents `POST https://www.clawdbase.ai/api/clawdbase/operations/run` with a server-side Bearer Access Key, JSON content type, `operation`, `subject`, `channel: "api"`, and `idempotency_key`. It recommends a 50-second deadline. REST and MCP are distinct interfaces: do not send `channel: "mcp"` to the REST route. Check live docs for supported subjects, resolution behavior, scopes and current costs; do not assume ambiguous labels resolve safely.

Read the Access Key through a server-side environment or secret store, without printing it, putting it in a shell argument, exposing it to a browser, or asking for it in chat. Handle failures without dumping headers or sensitive responses. Do not commit keys or real user results.

A successful operation can provide `ledger_id`, `charge_source` and `settled`. When authorized, verify the exact usage entry through `GET /api/clawdbase/usage` (requires `billing:usage.read`) and compare subject, operation, channel, status and charge. If unavailable, report billing verification as unavailable. A replay of the same idempotency key may confirm a previous settlement while returning no original result. A new logical request can incur another charge and requires appropriate user authorization.
