"""Advanced Calculator client – STDIO transport, tools + resource + prompt."""
import asyncio
import sys
from pathlib import Path

# Run from repo root; ensure we can find server
EXAMPLE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(EXAMPLE_DIR))

from fastmcp import Client

# STDIO: client spawns server as subprocess (real client–server separation)
client = Client(str(EXAMPLE_DIR / "server.py"))


async def main():
    async with client:
        # Server info (from handshake)
        info = client.initialize_result.serverInfo
        print(f"Server: {info.name}")

        # Tools
        tools = await client.list_tools()
        print(f"Tools: {[t.name for t in tools]}")

        # Resource
        resources = await client.list_resources()
        print(f"Resources: {[r.uri for r in resources]}")

        content = await client.read_resource("calc://info")
        print(f"Resource: {content[0].text}")

        # Prompts
        prompts = await client.list_prompts()
        print(f"Prompts: {[p.name for p in prompts]}")

        # Call tools
        r1 = await client.call_tool("multiply", {"a": 6, "b": 7})
        print(f"multiply(6, 7) => {r1.data}")

        r2 = await client.call_tool("divide", {"a": 20, "b": 4})
        print(f"divide(20, 4) => {r2.data}")


if __name__ == "__main__":
    asyncio.run(main())
