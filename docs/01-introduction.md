# 01 – Introduction

## What Problem Does MCP Solve?

Large Language Models (LLMs) are powerful at reasoning and generating text. But they cannot by themselves:

- Read your files
- Query your database
- Call external APIs
- Run shell commands
- Access real-time data

**MCP (Model Context Protocol)** gives LLMs a standard way to call **tools** that do these things. Instead of hard-coding every integration, you define tools once; any MCP-compatible client can use them.

---

## Why Tool Calling Matters

Without tools, an LLM can only:
- Answer from its training data
- Hallucinate about real-world state

With tools, an LLM can:
- Get up-to-date information
- Take actions on your behalf
- Integrate with your systems safely and consistently

---

## The Flow

```
User → Model → Tool Call → MCP Server → Result → Model → User
```

1. The **user** asks a question.
2. The **model** decides it needs a tool (e.g., "add two numbers").
3. The model calls the **tool** via the MCP client.
4. The **MCP server** runs the tool and returns the result.
5. The model receives the result, reasons, and responds to the user.

---

## Real-World Use Cases

| Use Case        | Tools Might Include                    |
|-----------------|----------------------------------------|
| Code assistant  | File read, search, lint, run tests     |
| Data analysis   | SQL query, CSV load, chart generation  |
| DevOps          | Deploy, logs, metrics, alerts          |
| Personal agent  | Calendar, email, reminders, notes      |

---

## What You Need to Know

- No prior MCP knowledge assumed
- Basic Python is enough
- We use **FastMCP** – a simple framework that hides the protocol details

**Next:** [02 – Core Concepts](02-core-concepts.md)
