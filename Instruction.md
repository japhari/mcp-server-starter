# Instruction.md

## How to Create an MCP Server (as implemented in `server.py`)

Follow these steps to create an MCP server similar to the implementation in `server.py`:

### 1. Import FastMCP

Import the `FastMCP` class from the `mcp.server.fastmcp` module:

```python
from mcp.server.fastmcp import FastMCP
```

### 2. Create an MCP Server Instance

Create an instance of `FastMCP` with a service name:

```python
mcp = FastMCP("Weather Service")
```

### 3. Define a Tool

Use the `@mcp.tool()` decorator to define a tool function:

```python
@mcp.tool()
def get_weather(location: str) -> str:
    return f"The weather in {location} is sunny."
```

### 4. Define a Resource

Use the `@mcp.resource()` decorator to define a resource endpoint:

```python
@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    return f"The data for {location} is sunny."
```

### 5. Define a Prompt

Use the `@mcp.prompt()` decorator to define a prompt function:

```python
@mcp.prompt()
def weather_report(location: str) -> str:
    return f"""You are weather reporter. Weather report for {location}?"""
```

### 6. Run the Server

Start the server by calling `mcp.run()` with the desired transport and port:

```python
if __name__ == "__main__":
    mcp.run(transport="sse", port=8000)
```

---

**Summary:**

- Import `FastMCP`.
- Create an MCP server instance.
- Define tools, resources, and prompts using decorators.
- Run the server with the desired configuration.
