# Example 03 – SQLite Tool

An MCP server that lets the model query a SQLite database.

## What This Demonstrates

- Integrating with a real data system
- Read-only query restriction for safety
- Auto-creating a sample database if missing

## How to Run

```bash
python server.py
```

On first run, a `database.db` file is created with a sample `tasks` table.

## What to Observe

1. Connect a client.
2. Ask: "What tasks are in the database?"
3. The model will call `sql_query` with `SELECT * FROM tasks`.
4. You'll get the rows as text.

## Schema

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    title TEXT,
    done INTEGER
);
```

Sample rows: "Learn MCP" (done=1), "Build a tool" (done=0).

## Security Note

This example restricts to SELECT only. In production, add further guards (allowed tables, query timeouts, etc.).
