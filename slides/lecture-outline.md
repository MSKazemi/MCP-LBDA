# MCP Course – Lecture Outline

Use this for in-person or recorded sessions. Adjust timing to your course duration.

---

## Block 1: Introduction (15–20 min)

1. **What is MCP?** (5 min)
   - Problem: LLMs need real-world data and actions
   - Solution: Standard protocol for tools
   - Flow: User → Model → Tool → Server → Result → User

2. **Core Concepts** (5 min)
   - Tool, Resource, Prompt, Server, Client, Transport
   - One-sentence definitions

3. **Real-World Use Cases** (5 min)
   - Code assistant, data analysis, DevOps, personal agent

---

## Block 2: Architecture (15–20 min)

1. **Diagram Walkthrough** (10 min)
   - LLM → Client → Server
   - Tools, Resources, Prompts boxes
   - Use `docs/diagrams/` if available

2. **Request Flow** (5 min)
   - Step-by-step: user question → tool call → result → answer

3. **Q&A** (5 min)

---

## Block 3: Hands-On – Calculator (20–25 min)

1. **Live Demo** (10 min)
   - Open `examples/01-calculator/server.py`
   - Walk through `@mcp.tool()`, types, docstring
   - Run server, connect client, call `add`

2. **Students Follow Along** (10 min)
   - Everyone runs the example
   - Try `subtract`, experiment with inputs

3. **Exercise 01** (5 min)
   - Add `multiply` – start in class, finish as homework

---

## Block 4: Hands-On – File Reader & SQLite (25–30 min)

1. **File Reader** (10 min)
   - Demo `examples/02-file-reader`
   - Discuss security: path restrictions

2. **SQLite Tool** (10 min)
   - Demo `examples/03-sqlite-tool`
   - Discuss read-only restriction, schema

3. **Students Run Both** (10 min)
   - Ask model to read a file, query the DB

---

## Block 5: FastMCP Deep Dive (15–20 min)

1. **What FastMCP Hides** (10 min)
   - JSON-RPC, schema generation, transport, sessions
   - Trade-offs: less control, more speed

2. **Exercises 02 & 03** (5 min)
   - Introduce Add Resource, Multi-Tool
   - Point to solutions for self-check

---

## Block 6: Wrap-Up (10 min)

1. **Recap** (5 min)
   - What we built, what we learned
   - Where to go next: MCP spec, custom transports

2. **Q&A + Resources** (5 min)
   - FAQ, CONTRIBUTING, GitHub links

---

## Suggested Durations

| Format   | Total | Blocks to Include          |
|----------|-------|----------------------------|
| 2 hours  | 120m  | 1, 2, 3, 6                 |
| 4 hours  | 240m  | 1–5, shorter blocks        |
| 6 hours  | 360m  | All blocks + longer hands-on |
