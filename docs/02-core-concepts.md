# 02 – Core Concepts

Short definitions with mini examples.

---

## Tool

A **tool** is a function the model can call. It has a name, parameters (with types), and a description. The model uses this to decide when and how to call it.

```
Example: add(a: int, b: int) → "Add two integers"
```

---

## Resource

A **resource** is data the model can read (e.g., a file, a URL). The model can fetch it by URI. Resources are read-only from the model's perspective.

```
Example: file:///path/to/notes.txt
```

---

## Prompt

A **prompt** is a pre-defined template the model can use to structure its behavior (e.g., "You are a helpful assistant that always cites sources").

---

## Server

The **MCP server** hosts tools, resources, and prompts. It runs as a process and responds to requests from clients.

---

## Client

The **MCP client** connects to the server and forwards requests from the model (e.g., Claude Desktop, Cursor, or a custom app).

---

## Transport

The **transport** is how the client and server communicate (e.g., stdio, HTTP). MCP defines the message format; transport is the carrier.

---

## Mini Example: Tool vs Resource

| Concept  | Model Action | Example                  |
|----------|--------------|--------------------------|
| **Tool** | Call function | `add(2, 3)` → `5`        |
| **Resource** | Read content | `get file://notes.txt` → file text |

**Next:** [03 – Architecture](03-architecture.md)
