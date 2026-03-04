# Model Context Protocol (MCP) – Hands-On Course

A self-paced, beginner-to-intermediate course for building MCP servers with **FastMCP**. Learn by doing.

---

## 🎯 What You Will Learn

- **What MCP is** – and why it matters for LLM applications
- **Model vs. Tool** – how LLMs call external capabilities
- **Building an MCP server** – from scratch, step by step
- **Exposing tools safely** – design patterns for real-world use
- **How LLM tool-calling works** – the full request–response flow

**Prerequisites:** Basic Python. No prior MCP knowledge required.

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

Connect a client (e.g., Cursor, VS Code, Claude Desktop) and try the `add` tool. You're running MCP.

**Use in VS Code or Cursor Chat:** See [Add MCP to your IDE](docs/05-ide-setup.md) – add the server and ask the AI to use the calculator tools.

### Test with the included client

Each example has a `client.py` alongside `server.py`:

```bash
python examples/01-calculator/client.py
```

Expected: `add(3, 7) => 10`

### Full teaching demo (fake LLM loop)

See the complete loop – User → Fake LLM → Client → Server → Result:

```bash
python examples/01-calculator/demo.py
```

Try: `add 4 and 5` | `subtract 10 3` | `quit`

---

## 📚 Teaching Docs

All docs include simple explanations. Code examples have inline comments.

| Doc | Topic |
|-----|-------|
| [01 – Introduction](docs/01-introduction.md) | What problem MCP solves, tool calling, real-world use cases |
| [02 – Core Concepts](docs/02-core-concepts.md) | Tools, resources, prompts; architecture diagram |
| [03 – Architecture](docs/03-architecture.md) | Request lifecycle, how pieces fit together |
| [04 – FastMCP Explained](docs/04-fastmcp.md) | MCP vs SDK vs FastMCP; what FastMCP hides |
| [05 – IDE Setup](docs/05-ide-setup.md) | Add MCP to VS Code or Cursor, use in Chat |

**Going deeper:** [03-architecture](docs/03-architecture.md) includes MCP spec and transport options.

---

## 📖 Learning Path

Follow this order for best results:

| # | Step | What to do |
|---|------|------------|
| 1 | **Read** | [01-introduction](docs/01-introduction.md) – What problem does MCP solve? |
| 2 | **Run** | [examples/01-calculator](examples/01-calculator) – Server + client |
| 2b | **Demo** | [examples/01-calculator/demo.py](examples/01-calculator/demo.py) – Full loop (fake LLM) |
| 3 | **Read** | [02-core-concepts](docs/02-core-concepts.md) – Tools, resources, prompts |
| 4 | **Run** | [examples/02-calculator-advanced](examples/02-calculator-advanced) – STDIO, resources, prompts |
| 5 | **Run** | [examples/03-file-reader](examples/03-file-reader) – File I/O |
| 6 | **Read** | [03-architecture](docs/03-architecture.md) – Request flow |
| 7 | **Run** | [examples/04-sqlite-tool](examples/04-sqlite-tool) – Database |
| 8 | **Read** | [04-fastmcp](docs/04-fastmcp.md) – What FastMCP hides |
| 9 | **Setup** | [05-ide-setup](docs/05-ide-setup.md) – Add MCP to VS Code / Cursor |
| 10 | **Practice** | [exercises/](exercises/) – Build your own tools |

---

## 🛠 Examples

| Example | What it shows |
|---------|---------------|
| [01-calculator](examples/01-calculator) | Minimal: in-memory server, 2 tools, demo loop |
| [02-calculator-advanced](examples/02-calculator-advanced) | STDIO transport, resource, prompt, instructions |
| [03-file-reader](examples/03-file-reader) | File I/O – `read_file` tool |
| [04-sqlite-tool](examples/04-sqlite-tool) | Database – read-only SQL queries |

Each has a `README.md`, `server.py`, and `client.py`. Code includes inline comments for learners.

---

## ✏️ Exercises

| Exercise | Goal |
|----------|------|
| [01 – Build a Tool](exercises/exercise-01-build-tool.md) | Add `multiply`; explore type validation |
| [02 – Add a Resource](exercises/exercise-02-add-resource.md) | Expose read-only data at a URI |
| [03 – Multi-Tool Server](exercises/exercise-03-multi-tool.md) | Notes server: create, list, get, delete |

Solutions: [solutions/solution-01](solutions/solution-01), [solution-02](solutions/solution-02), [solution-03](solutions/solution-03).

---

## 📁 Repository Structure

```
MCP-LBDA/
├── docs/                      ← Teaching docs
│   ├── 01-introduction.md
│   ├── 02-core-concepts.md
│   ├── 03-architecture.md
│   ├── 04-fastmcp.md
│   └── 05-ide-setup.md
├── examples/
│   ├── 01-calculator/         ← Minimal: server, client, demo
│   ├── 02-calculator-advanced/← STDIO, resource, prompt
│   ├── 03-file-reader/        ← File I/O
│   └── 04-sqlite-tool/        ← Database
├── exercises/                 ← Hands-on tasks
│   ├── exercise-01-build-tool.md
│   ├── exercise-02-add-resource.md
│   └── exercise-03-multi-tool.md
├── solutions/                 ← Exercise answers
│   ├── solution-01/
│   ├── solution-02/
│   └── solution-03/
├── mcp.json.cursor.example    ← Cursor config
├── mcp.json.vscode.example    ← VS Code config
├── FAQ.md                    ← Common questions
└── requirements.txt
```

**Key:** Servers and clients use **FastMCP**. See [gofastmcp.com/servers/server](https://gofastmcp.com/servers/server) and [gofastmcp.com/clients/client](https://gofastmcp.com/clients/client).

---

## 🤔 FAQ

See [FAQ.md](FAQ.md) for: *Why not REST? Why not LangChain? What is transport? Do I need Cursor?*

---

## 📜 License

MIT – see [LICENSE](LICENSE).
