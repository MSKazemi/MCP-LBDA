# 03 – Architecture

## The Big Picture

```
                    ┌─────┐
                    │ LLM │
                    └──┬──┘
                       │ "Call add(2,3)"
                       ▼
              ┌────────────────┐
              │   MCP Client   │  ← FastMCP Client
              │ (e.g. Cursor)  │
              └───────┬────────┘
                      │ JSON-RPC over transport
                      ▼
              ┌────────────────┐
              │   MCP Server   │  ← FastMCP
              ├────────────────┤
              │  Tools         │  ← add, multiply, read_file...
              │  Resources     │  ← file://, custom URIs
              │  Prompts       │  ← predefined templates
              └────────────────┘
```

**Key:** FastMCP provides both server and client. See [gofastmcp.com](https://gofastmcp.com).

---

## What Each Box Does

| Component   | Role |
|------------|------|
| **LLM**    | Reasons about user input, decides when to call tools, interprets results. |
| **MCP Client** | Talks to the LLM, sends tool calls to the server, returns results. |
| **MCP Server** | Runs your tools, serves resources, manages prompts. |
| **Tools**  | Your Python functions exposed with names and schemas. |
| **Resources** | Read-only content the model can fetch by URI. |
| **Prompts** | Templates that shape the model's behavior. |

---

## Request Flow (Simplified)

1. User: "What is 7 + 12?"
2. LLM: decides it needs `add(7, 12)`
3. Client: sends `tools/call` with `{"name": "add", "arguments": {"a": 7, "b": 12}}`
4. Server: runs `add(7, 12)` → `19`
5. Client: returns `19` to the LLM
6. LLM: "7 + 12 = 19"

---

## Why This Design?

- **Standardized:** Same protocol for any LLM and any tool set
- **Decoupled:** Server and client can evolve independently
- **Secure:** Server runs in your environment; you control what tools exist

## Teaching: Full Loop

```
User → Fake LLM (simulated) → MCP Client → FastMCP Server → Tool → Result → User
```

Run `examples/01-calculator/demo.py` to see this without a real LLM. The fake LLM converts "add 4 and 5" into a structured tool call; the client sends it; the server runs the tool. Each example has `server.py` and `client.py` in the same directory.

**Next:** [04 – FastMCP Explained](04-fastmcp-explained.md)
