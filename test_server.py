r"""
Test script to verify hello-mcp server tools directly.
Run this from VS Code terminal:
    .venv\Scripts\python.exe test_server.py
"""
import asyncio
import server

async def main():
    print("=" * 50)
    print("Testing 'hello-mcp' Server Tools...")
    print("=" * 50)

    # 1. Test get_greeting
    name = "Students"
    greeting_direct = server.get_greeting(name)
    print(f"\n[Test 1] Direct Call: get_greeting('{name}')")
    print(f"Result: {greeting_direct}")

    # 2. Test add_numbers
    a, b = 10, 20
    sum_direct = server.add_numbers(a, b)
    print(f"\n[Test 2] Direct Call: add_numbers({a}, {b})")
    print(f"Result: {sum_direct}")

    # 3. Test via MCP Server Registration & Call Tool
    print("\n[Test 3] Testing via MCP Protocol...")
    tools = await server.mcp.list_tools()
    tool_names = [t.name for t in tools]
    print(f"Discovered Tools: {tool_names}")
    assert "get_greeting" in tool_names, "get_greeting missing!"
    assert "add_numbers" in tool_names, "add_numbers missing!"

    res1 = await server.mcp.call_tool("get_greeting", {"name": "Students"})
    print(f"MCP Call get_greeting -> {res1.content[0].text}")

    res2 = await server.mcp.call_tool("add_numbers", {"a": 10, "b": 20})
    print(f"MCP Call add_numbers -> {res2.content[0].text}")

    print("\n" + "=" * 50)
    print("ALL TESTS PASSED SUCCESSFULLY! (0 ERRORS)")
    print("=" * 50)

if __name__ == "__main__":
    asyncio.run(main())
