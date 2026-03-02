"""Minimal MCP client – FastMCP Client, in-memory (same process)."""
import asyncio
from fastmcp import Client
from server import mcp

client = Client(mcp)


async def main():
    async with client:
        tools = await client.list_tools()
        print(f"Tools: {[t.name for t in tools]}")

        result = await client.call_tool("add", {"a": 3, "b": 7})
        print(f"add(3, 7) => {result.data}")


if __name__ == "__main__":
    asyncio.run(main())
