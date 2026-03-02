# Model Context Protocol (MCP) – Hands-On Course

A self-paced, beginner-to-intermediate course for building MCP servers with **FastMCP**. Learn by doing.

---

## 🎯 What You Will Learn

- **What MCP is** – and why it matters for LLM applications
- **Model vs. Tool** – how LLMs call external capabilities
- **Building an MCP server** – from scratch, step by step
- **Exposing tools safely** – design patterns for real-world use
- **How LLM tool-calling works** – the full request-response flow

---

## ⚡ Quick Start (5 Minutes)

```bash
# Clone and enter
cd MCP-LBDA

# Create and activate virtual environment
python3 -m venv .venv       # or: python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run your first MCP server
python examples/01-calculator/server.py
```

Connect a client (e.g., Cursor, Claude Desktop) and try the `add` tool. You're running MCP.

**Use in VS Code or Cursor Chat:** See [docs/05-ide-setup.md](docs/05-ide-setup.md) – add the MCP server to your IDE and ask the AI to use the calculator tools.

### Test with the included client

Each example has a `client.py` alongside `server.py`:

```bash
python examples/01-calculator/client.py
```

Expected: `add(3, 7) => 10`

### Full teaching demo (Fake LLM loop)

See the complete loop – User → Fake LLM → Client → Server → Result:

```bash
python examples/01-calculator/demo.py
```

Try: `add 4 and 5` | `subtract 10 3` | `quit`

---

## 📚 Learning Path

Follow this order for best results:

| # | Step | What to do |
|---|------|------------|
| 1 | Read | [`docs/01-introduction.md`](docs/01-introduction.md) – What problem does MCP solve? |
| 2 | Run | [`examples/01-calculator`](examples/01-calculator) – Server + client |
| 2b | Demo | [`examples/01-calculator/demo.py`](examples/01-calculator/demo.py) – Full loop (fake LLM) |
| 3 | Read | [`docs/02-core-concepts.md`](docs/02-core-concepts.md) – Tools, resources, prompts |
| 3 | Run | [`examples/02-calculator-advanced`](examples/02-calculator-advanced) – More features |
| 4 | Run | [`examples/03-file-reader`](examples/03-file-reader) – File I/O |
| 5 | Read | [`docs/03-architecture.md`](docs/03-architecture.md) – How the pieces fit together |
| 6 | Run | [`examples/04-sqlite-tool`](examples/04-sqlite-tool) – Database |
| 7 | Read | [`docs/04-fastmcp-explained.md`](docs/04-fastmcp-explained.md) – What FastMCP hides |
| 8 | Read | [`docs/05-ide-setup.md`](docs/05-ide-setup.md) – Add MCP to VS Code / Cursor, use in Chat |
| 9 | Practice | [`exercises/`](exercises/) – Build your own tools |

---

## 📁 Repository Structure

```
MCP-LBDA/
├── examples/
│   ├── 01-calculator/        ← Minimal: in-memory FastMCP
│   ├── 02-calculator-advanced/ ← Same domain, more features
│   ├── 03-file-reader/       ← File I/O
│   └── 04-sqlite-tool/       ← Database
├── docs/
│   └── 05-ide-setup.md       ← Add MCP to VS Code/Cursor
├── exercises/
├── mcp.json.example         ← Sample config for IDE
└── ...
```

**Key:** Both server and client use **FastMCP**. See [gofastmcp.com/servers/server](https://gofastmcp.com/servers/server) and [gofastmcp.com/clients/client](https://gofastmcp.com/clients/client).

---

## 🤔 FAQ

See [FAQ.md](FAQ.md) for common questions: *Why not REST? Why not LangChain? What is transport?*

---

## 📜 License

MIT – see [LICENSE](LICENSE).
