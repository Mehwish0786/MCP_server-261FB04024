# Building a Python MCP Server with VS Code and GitHub Copilot

A step-by-step implementation and usage guide for creating a local **Model Context Protocol (MCP)** server in Python and connecting it to **VS Code** with **GitHub Copilot Agent Mode**.

---

## 📌 Project Overview

-**Name:** Shaik.Mehwish
-**Reg NO:** 261FB04024

- **Project Name:** `hello-mcp`
- **Language:** Python (3.11+)
- **SDK:** Model Context Protocol (MCP) Python SDK 2.x (`mcp[cli]`)
- **Transport:** Standard Input/Output (`stdio`)
- **Environment:** Visual Studio Code
- **AI Client:** GitHub Copilot (Agent Mode)
- **Implemented Tools:**
  1. `get_greeting(name: str) -> str`: Returns a personalized greeting for a student.
  2. `add_numbers(a: int, b: int) -> int`: Adds two integers and returns their sum.

---

## 💻 Software Requirements & Versions

| Requirement | Specification / Recommended Version |
| :--- | :--- |
| **Operating System** | Windows 10/11 (64-bit) |
| **Python** | Python 3.12.x (meets 3.11+ requirement) |
| **VS Code** | Latest VS Code installed |
| **GitHub Account** | Active GitHub account with GitHub Copilot access |
| **Copilot Extension** | GitHub Copilot & GitHub Copilot Chat installed (Agent mode enabled) |
| **Python MCP SDK** | `mcp[cli]` (Python SDK 2.x) |

---

## 📁 Project Structure

```text
hello-mcp/
├── server.py             # Python MCP server implementation
├── requirements.txt      # Project dependencies (mcp[cli])
├── README.md             # Complete step-by-step documentation
├── .venv/                # Isolated virtual environment
└── .vscode/
    └── mcp.json          # VS Code MCP server configuration
```

---

## 🚀 Step-by-Step Implementation Guide

### Phase 1: Create the Project & Virtual Environment

1. Open PowerShell or Terminal in your project directory:
   ```powershell
   cd "C:\Users\shaik\OneDrive\Desktop\hello-mcp 261FB04024"
   ```
2. Create an isolated Python 3.12 virtual environment:
   ```powershell
   py -3.12 -m venv .venv
   ```
   > **Why?** A virtual environment isolates project dependencies and prevents version conflicts with other Python projects on your system.

---

### Phase 2: Install Dependencies

1. Install the MCP SDK along with CLI extras:
   ```powershell
   .venv\Scripts\python.exe -m pip install "mcp[cli]" --default-timeout=120
   ```
2. Verify that the SDK was installed successfully:
   ```powershell
   .venv\Scripts\python.exe -m pip show mcp
   ```

---

### Phase 3: Create the Server Script (`server.py`)

Create `server.py` in the root of the project with the following code:

```python
from mcp.server.mcpserver import MCPServer

# Initialize the MCP server instance
mcp = MCPServer("Hello MCP")

# Tool 1: Return a personalized greeting
@mcp.tool()
def get_greeting(name: str) -> str:
    """Return a greeting for a student."""
    return f"Hello, {name}! Your first MCP tool works."

# Tool 2: Add two integers
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

# Start the stdio server loop
if __name__ == "__main__":
    mcp.run()
```

#### Code Breakdown:
- `MCPServer("Hello MCP")`: Creates and names the MCP server instance.
- `@mcp.tool()`: Decorator that exposes standard Python functions as MCP tools discoverable by LLMs.
- Type hints (`name: str`, `a: int`, `b: int`) and docstrings: Automatically converted into JSON Schema parameters for the AI model.
- `mcp.run()`: Runs the server over stdio, listening for JSON-RPC messages.

---

### Phase 4: Configure VS Code (`.vscode/mcp.json`)

Create a `.vscode` folder and add `mcp.json`:

```json
{
  "servers": {
    "helloMcp": {
      "type": "stdio",
      "command": "${workspaceFolder}\\.venv\\Scripts\\python.exe",
      "args": ["server.py"]
    }
  }
}
```

#### Configuration Details:
- `"helloMcp"`: The unique identifier for your server in VS Code.
- `"type": "stdio"`: The communication transport mechanism.
- `"command"`: Path to the virtual environment's Python interpreter (`${workspaceFolder}\.venv\Scripts\python.exe`).
- `"args"`: The entry script argument (`["server.py"]`).

---

### Phase 5: Start & Verify the Server in VS Code

1. Save all files in VS Code.
2. Press `Ctrl + Shift + P` to open the Command Palette.
3. Type and select: **`MCP: List Servers`**.
4. Select **`helloMcp`**.
5. Click **Start / Restart**.
6. Check the **MCP Output Panel** to confirm:
   ```text
   helloMcp
   Connection state: Running
   Discovered 2 tools
   ```

---

### Phase 6: Test `get_greeting` with GitHub Copilot

1. Open **Copilot Chat** in VS Code.
2. Ensure **Agent mode** is enabled (or type `@agent`).
3. Enter the test prompt:
   > *"Use the get_greeting MCP tool from helloMcp with the name Students. Show me the result."*
4. **Expected Tool Result:**
   ```text
   Hello, Students! Your first MCP tool works.
   ```

---

### Phase 7: Test `add_numbers` with GitHub Copilot

1. In Copilot Chat (Agent mode), enter:
   > *"Use the add_numbers MCP tool from helloMcp with a = 10 and b = 20. Show me the result."*
2. **Expected Tool Result:**
   ```text
   30
   ```

---

## 🛠️ Troubleshooting Guide

| Issue | Cause | Solution |
| :--- | :--- | :--- |
| `No module named mcp.server.fastmcp` | FastMCP legacy import used in SDK 2.x | Use `from mcp.server.mcpserver import MCPServer` |
| `Path not found` | Incorrect interpreter or file path | Verify that `.venv\Scripts\python.exe` exists and match `.vscode/mcp.json` |
| `Pip download timeout` | Slow or unstable network connection | Add `--default-timeout=120` to the pip install command and check internet |
| `Server does not start` | Python syntax error or invalid JSON | Verify `server.py` syntax, check `.vscode/mcp.json` commas, and inspect MCP logs |
| `Copilot skips tools` | Copilot permissions or agent mode disabled | Switch Copilot Chat to **Agent mode**; verify server status is **Running** and tools are **Discovered** |

---

## 🎯 Summary of Outcomes

- ✅ **Isolated Python Environment** created under `.venv`.
- ✅ **MCP SDK 2.x** installed and configured.
- ✅ Two custom Python tools (`get_greeting`, `add_numbers`) exposed.
- ✅ VS Code `.vscode/mcp.json` configured for local stdio communication.
- ✅ Ready for interactive Copilot Agent tool calling.
