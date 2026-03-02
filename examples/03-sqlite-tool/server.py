import sqlite3
from pathlib import Path

from fastmcp import FastMCP

DB_PATH = Path(__file__).parent / "database.db"
mcp = FastMCP("SQLite Tool")


def get_connection():
    """Get a connection to the SQLite database."""
    return sqlite3.connect(DB_PATH)


@mcp.tool()
def sql_query(query: str) -> str:
    """Execute a read-only SQL query on the sample database. Use SELECT only."""
    if ";" in query and "SELECT" not in query.upper().split(";")[0]:
        return "Error: Only SELECT queries are allowed."
    if "INSERT" in query.upper() or "UPDATE" in query.upper() or "DELETE" in query.upper():
        return "Error: Write operations are not allowed."
    try:
        conn = get_connection()
        cur = conn.execute(query)
        rows = cur.fetchall()
        cols = [d[0] for d in cur.description] if cur.description else []
        conn.close()
        if not cols:
            return f"Query executed. Rows affected: {len(rows)}"
        return "\n".join([str(dict(zip(cols, row))) for row in rows])
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    # Ensure sample DB exists
    if not DB_PATH.exists():
        conn = sqlite3.connect(DB_PATH)
        conn.execute(
            "CREATE TABLE tasks (id INTEGER PRIMARY KEY, title TEXT, done INTEGER)"
        )
        conn.execute("INSERT INTO tasks (title, done) VALUES ('Learn MCP', 1)")
        conn.execute("INSERT INTO tasks (title, done) VALUES ('Build a tool', 0)")
        conn.commit()
        conn.close()
    mcp.run()
