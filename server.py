"""
Weather Service MCP Server
-------------------------
A simple Model Context Protocol (MCP) server that provides weather information tools, resources, and prompts.
"""

import logging
from mcp.server.fastmcp import FastMCP
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("WeatherService")

# Create an MCP Server
mcp = FastMCP("Weather Service")

@mcp.tool()
def get_weather(location: str) -> str:
    """Return a mock weather report for a given location."""
    logger.info(f"get_weather called with location: {location}")
    # In a real app, fetch weather from an API here
    return f"The weather in {location} is sunny and 25°C."

@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """Return mock weather data for a given location as a resource."""
    logger.info(f"weather_resource called with location: {location}")
    return f"Weather data for {location}: sunny, 25°C, humidity 40%."

@mcp.prompt()
def weather_report(location: str) -> str:
    """Prompt template for weather reporting."""
    logger.info(f"weather_report called with location: {location}")
    return f"You are a weather reporter. What is the weather report for {location}?"

if __name__ == "__main__":
    logger.info("Starting Weather Service MCP server on port 8000...")
    mcp.run(transport="sse", port=8000)