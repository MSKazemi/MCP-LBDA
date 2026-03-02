# Contributing to MCP Course

Thank you for contributing! This guide helps you add tools and examples.

---

## How to Add a New Example

1. **Create a folder** in `examples/` with the next number:
   ```
   examples/04-my-example/
   ├── server.py
   ├── client.py
   └── README.md
   ```

2. **Follow the pattern:**
   - `server.py` – FastMCP server with `if __name__ == "__main__": mcp.run()`
   - `client.py` – MCP SDK client that spawns server and calls tools (same dir as server)
   - `README.md` – What it demonstrates, how to run, what to observe

3. **Update the root README** – add your example to the Learning Path table if it fits the sequence.

---

## How to Add an Exercise

1. **Create** `exercises/exercise-NN-description.md`
2. **Include:**
   - Goal
   - Tasks (numbered)
   - Hints
   - Link to solution

3. **Create the solution** in `solutions/solution-NN/`
4. **Keep solutions separate** – never mix with exercise instructions.

---

## Code Style

- Python: PEP 8, type hints where helpful
- Docstrings: Clear, one-line for tools
- Keep examples minimal – no extra dependencies unless necessary

---

## Diagram Updates

Diagrams live in `docs/diagrams/`. If you add or change:

- `mcp-overview.png` – high-level MCP components
- `client-server-flow.png` – request/response flow
- `tool-execution-flow.png` – tool call lifecycle

Keep them simple; ASCII in markdown is fine too.
