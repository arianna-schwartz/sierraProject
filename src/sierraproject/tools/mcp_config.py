import os
from pathlib import Path

from crewai_tools import MCPServerAdapter
from crewai_tools.adapters.mcp_adapter import StdioServerParameters
from dotenv import load_dotenv

load_dotenv()


def get_stagehand_mcp_tools():
    """
    Configures and returns MCP adapter for the Stagehand MCP server.
    
    Returns:
        MCPServerAdapter instance configured for Stagehand
    """
    # Get the path to the MCP server
    current_dir = Path(__file__).parent.parent
    mcp_server_path = current_dir / "mcp-servers" / "stagehand" / "dist" / "index.js"
    
    # Configure the MCP server parameters for stdio transport
    server_params = StdioServerParameters(
        command="node",
        args=[str(mcp_server_path)],
        env={
            "BROWSERBASE_API_KEY": os.getenv("BROWSERBASE_API_KEY"),
            "BROWSERBASE_PROJECT_ID": os.getenv("BROWSERBASE_PROJECT_ID"),
            "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        }
    )
    
    # Create and return the MCP adapter
    return MCPServerAdapter(server_params)