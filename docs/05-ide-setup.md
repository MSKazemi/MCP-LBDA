# 05 – Add MCP Server to VS Code & Cursor

How to run this course's MCP servers inside your IDE and use them in Chat.

---

## What is Chat (VS Code / Cursor)?

**Chat** is the AI assistant panel where you type messages and get responses. The AI can use MCP tools, resources, and prompts when you ask it to.

| IDE | Chat feature | Shortcut |
|-----|--------------|----------|
| **VS Code** | Copilot Chat (with GitHub Copilot) | `Ctrl+Alt+I` (Win/Linux), `⌃⌘I` (Mac) |
| **Cursor** | Cursor Chat (built-in) | `Ctrl+L` or Chat panel |

---

## VS Code – Add MCP Server

VS Code uses `mcp.json` with a `servers` section. Configuration can live in your user profile (global) or in `.vscode/mcp.json` (workspace).

### 1. Open configuration

- **User (global):** Command Palette (`Ctrl+Shift+P`) → `MCP: Open User Configuration`
- **Workspace:** Create or edit `.vscode/mcp.json` in your project (to share with the team)

### 2. Add the calculator server

Example for the basic calculator in this repo (use your real paths):

```json
{
  "servers": {
    "calculator": {
      "command": "/path/to/MCP-LBDA/.venv/bin/python",
      "args": [
        "/path/to/MCP-LBDA/examples/01-calculator/server.py"
      ]
    }
  }
}
```

For the advanced calculator:

```json
{
  "servers": {
    "calculator": {
      "command": "/path/to/MCP-LBDA/.venv/bin/python",
      "args": [
        "/path/to/MCP-LBDA/examples/01-calculator/server.py"
      ]
    },
    "calculator-advanced": {
      "command": "/path/to/MCP-LBDA/.venv/bin/python",
      "args": [
        "/path/to/MCP-LBDA/examples/02-calculator-advanced/server.py"
      ]
    }
  }
}
```

Replace `/path/to/MCP-LBDA` with your actual repo path. On Windows, use the path to `.venv\Scripts\python.exe` and `\\` for backslashes in JSON strings. See also `mcp.json.example` in the repo root.

### 3. Trust and start

When you first add a server, VS Code may ask you to trust it. Approve to let it start. Use **MCP: List Servers** to see status and logs.

### 4. Use in Chat

Open Chat (`Ctrl+Alt+I`), then try:

- *"Add 3 and 4 using the calculator"*
- *"Compute 5 * (3 + 2)"*
- *"Read the resource at calc://info"*

---

## Cursor – Add MCP Server

Cursor uses `mcp.json` with a `mcpServers` section. The file lives at:

- **Global:** `~/.cursor/mcp.json`

### 1. Edit configuration

Open `~/.cursor/mcp.json` and add your servers:

```json
{
  "mcpServers": {
    "calculator": {
      "command": "/path/to/MCP-LBDA/.venv/bin/python",
      "args": [
        "/path/to/MCP-LBDA/examples/01-calculator/server.py"
      ]
    },
    "calculator-advanced": {
      "command": "/path/to/MCP-LBDA/.venv/bin/python",
      "args": [
        "/path/to/MCP-LBDA/examples/02-calculator-advanced/server.py"
      ]
    }
  }
}
```

**Tips:**

- Use `python3` instead of a venv path if your system `python3` has the required packages.
- On systems without a `python` symlink, prefer `python3` or the full path to your venv Python.

### 2. Reload MCP servers

After saving, reload MCP: Command Palette → `MCP: Reload Servers`, or restart Cursor.

### 3. Use in Chat

Open Cursor Chat (`Ctrl+L`) and try the same prompts as for VS Code.

---

## Quick reference

| Config key | VS Code | Cursor |
|------------|---------|--------|
| Root | `servers` | `mcpServers` |
| File | User profile or `.vscode/mcp.json` | `~/.cursor/mcp.json` |

Both use `command` and `args` for stdio servers. Make sure your Python environment has `fastmcp` installed (`pip install -r requirements.txt`).

---

## Troubleshooting

| Error | Cause | Fix |
|-------|-------|-----|
| `spawn python ENOENT` | `python` not in PATH | Use `python3` or full path to venv Python |
| `ModuleNotFoundError: fastmcp` | Wrong Python env | Use the venv Python that has `fastmcp` installed |
| Server not found in Chat | Config not loaded | Reload MCP servers or restart the IDE |

