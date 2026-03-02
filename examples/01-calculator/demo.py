"""Full demo: User → Fake LLM → FastMCP Client → Server → Result."""
import asyncio
import re
from typing import NamedTuple

from fastmcp import Client

from server import mcp

client = Client(mcp)


class ToolCall(NamedTuple):
    tool: str
    arguments: dict


def fake_llm(user_input: str) -> ToolCall | None:
    """Parse user input → tool call. e.g. 'add 4 and 5' → add(4, 5)."""
    inp = user_input.strip().lower()
    if m := re.search(r"add\s+(\d+)\s+(?:and\s+)?(\d+)", inp):
        return ToolCall("add", {"a": int(m.group(1)), "b": int(m.group(2))})
    if m := re.search(r"(\d+)\s*\+\s*(\d+)", inp):
        return ToolCall("add", {"a": int(m.group(1)), "b": int(m.group(2))})
    if m := re.search(r"subtract\s+(\d+)\s+(\d+)", inp):
        return ToolCall("subtract", {"a": int(m.group(1)), "b": int(m.group(2))})
    if m := re.search(r"(\d+)\s+minus\s+(\d+)", inp):
        return ToolCall("subtract", {"a": int(m.group(1)), "b": int(m.group(2))})
    return None


async def call_tool(tool_name: str, arguments: dict):
    async with client:
        result = await client.call_tool(tool_name, arguments)
        return result.data


def main():
    print("Full MCP demo (Fake LLM + FastMCP Client + Server)")
    print("Try: 'add 4 and 5'  |  'subtract 10 3'  |  'quit'")
    print("-" * 50)

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        if not user_input or user_input.lower() in ("quit", "exit", "q"):
            print("Bye!")
            break

        tool_call = fake_llm(user_input)
        if tool_call is None:
            print("(Fake LLM didn't understand. Try 'add 4 and 5' or 'subtract 10 3')")
            continue

        print(f"  [Fake LLM] → {tool_call.tool}{tool_call.arguments}")
        result = asyncio.run(call_tool(tool_call.tool, tool_call.arguments))
        print(f"  [Server]   → {result}")


if __name__ == "__main__":
    main()
