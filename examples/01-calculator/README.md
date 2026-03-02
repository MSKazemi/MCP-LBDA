# Example 01 – Calculator

Your first MCP server: two simple tools.

## What This Demonstrates

- Defining tools with `@mcp.tool()`
- Type hints → automatic schema
- Docstring → tool description

## How to Run

```bash
python server.py
```

Or with uvicorn (if using SSE transport):

```bash
uvicorn server:mcp --reload
```

## What to Observe

1. The server starts and waits for connections.
2. Connect a client (e.g., Cursor MCP, Claude Desktop).
3. Call `add` with two integers – you get their sum.
4. Call `subtract` – you get the difference.

## Next

Try [Example 02 – File Reader](../02-file-reader/) for interaction with the environment.
