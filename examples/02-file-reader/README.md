# Example 02 – File Reader

An MCP server that lets the model read files from your environment.

## What This Demonstrates

- Tools that interact with the environment (filesystem)
- Error handling (file not found, not a file)
- Path handling with `pathlib`

## How to Run

```bash
python server.py
```

## What to Observe

1. Connect a client.
2. Ask the model to "read the contents of README.md in this example folder".
3. The model will call `read_file` with the path.
4. You'll get the file contents in the response.

## Security Note

This example reads from the filesystem. In production, restrict paths (e.g., allowlist directories) to avoid exposing sensitive files.

## Next

Try [Example 03 – SQLite Tool](../03-sqlite-tool/) for database integration.
