# 04 – FastMCP Explained

FastMCP lets you focus on tools and logic while it handles the protocol.

---

## What FastMCP Hides

| Concern               | What you'd do manually | What FastMCP does |
|-----------------------|------------------------|-------------------|
| JSON-RPC              | Serialize/parse messages | Built-in |
| Schema generation     | Write tool schemas by hand | From Python type hints |
| Transport             | Implement stdio/HTTP   | `mcp.run()` handles it |
| Session management   | Track state, lifecycle | Handled for you |

---

## From Function to Tool

You write:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b
```

FastMCP automatically:
- Infers the JSON schema from `a: int`, `b: int`
- Uses the docstring as the tool description
- Registers the tool with the MCP server
- Handles validation and error responses

---

## The Abstraction Trade-off

| Pro                          | Con                          |
|------------------------------|------------------------------|
| Less boilerplate             | Less control over low-level details |
| Fast iteration               | May need to drop down for edge cases |
| Pythonic, readable           | Tied to FastMCP's conventions |

For learning and most projects, the pros outweigh the cons.

---

## When You Might Go Deeper

- Custom transports
- Special session handling
- Integrating with non-Python systems
- Debugging protocol-level issues

The MCP spec is open; you can implement servers in any language.

**Next:** [05 – IDE Setup](05-ide-setup.md) – Add MCP to VS Code/Cursor and use in Chat. Then try the [exercises](../exercises/).
