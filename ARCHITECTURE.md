# Architecture (Advanced)

For learners who want to go deeper than the main docs.

---

## MCP Specification

MCP is defined in the [Model Context Protocol specification](https://spec.modelcontextprotocol.io/). Key components:

- **JSON-RPC 2.0** as the message format
- **Initialization** handshake with capabilities
- **Tools**: `tools/list`, `tools/call`
- **Resources**: `resources/list`, `resources/read`
- **Prompts**: `prompts/list`, `prompts/get`

---

## Transport Options

| Transport | Protocol | Use Case |
|-----------|----------|----------|
| stdio | stdin/stdout | Local CLI, Claude Desktop |
| HTTP + SSE | HTTP with Server-Sent Events | Remote servers, web clients |
| HTTP (streamable) | HTTP POST | Simple request-response |

---

## FastMCP Internals (Simplified)

1. **Decorators** (`@mcp.tool`, etc.) register handlers
2. **Schema** is derived from type hints via Pydantic
3. **run()** starts the chosen transport and listens for JSON-RPC messages
4. Incoming `tools/call` → route to your function → return result as JSON-RPC response

---

## Extending the Course

- Add a **custom transport** (e.g., WebSocket)
- Implement a **minimal MCP server** in another language
- Add **authentication** for HTTP transport
- Explore **prompts** in depth

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add examples.
