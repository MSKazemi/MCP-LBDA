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
cd mcp-course

# Install
pip install -r requirements.txt

# Run your first MCP server
python examples/01-calculator/server.py
```

Connect a client (e.g., Cursor, Claude Desktop) and try the `add` tool. You're running MCP.

---

## 📚 Learning Path

Follow this order for best results:

| # | Step | What to do |
|---|------|------------|
| 1 | Read | [`docs/01-introduction.md`](docs/01-introduction.md) – What problem does MCP solve? |
| 2 | Run | [`examples/01-calculator`](examples/01-calculator) – Your first tool |
| 3 | Read | [`docs/02-core-concepts.md`](docs/02-core-concepts.md) – Tools, resources, prompts |
| 4 | Run | [`examples/02-file-reader`](examples/02-file-reader) – Interacting with the environment |
| 5 | Read | [`docs/03-architecture.md`](docs/03-architecture.md) – How the pieces fit together |
| 6 | Run | [`examples/03-sqlite-tool`](examples/03-sqlite-tool) – Real data integration |
| 7 | Read | [`docs/04-fastmcp-explained.md`](docs/04-fastmcp-explained.md) – What FastMCP hides |
| 8 | Practice | [`exercises/`](exercises/) – Build your own tools |

---

## 📁 Repository Structure

```
mcp-course/
├── README.md           ← You are here
├── requirements.txt
├── docs/               ← Concepts before code
├── examples/           ← Runnable servers
├── exercises/          ← Practice challenges
├── solutions/          ← Reference answers
├── slides/             ← Lecture outline
└── CONTRIBUTING.md     ← How to add tools
```

---

## 🤔 FAQ

See [FAQ.md](FAQ.md) for common questions: *Why not REST? Why not LangChain? What is transport?*

---

## 📜 License

MIT – see [LICENSE](LICENSE).
