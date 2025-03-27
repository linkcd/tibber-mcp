# Tibber MCP
This is [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) Server for [Tibber](https://tibber.com/), a Norwegian power supplier. 

You can run the MCP server locally and access it via the different host such as Claude Desktop or [Roo Code](https://marketplace.visualstudio.com/items?itemName=RooVeterinaryInc.roo-cline).

## Overview
This Tibber MCP server provides AI agent a convenient way to talk to [Tibber API](https://developer.tibber.com/docs), and query information such as current price and your consumption.

## Example Queries
Once connected to the MCP server, you can ask questions like:
- "Analyze my power consumption data and present the usual peak hours and any other interesting patterns in an easy-to-read format."
- "When did I use the most power yesterday?"
- "How much power I consumpted yesterday 7AM?"

## Demo video
[![Tibber MCP Demo](https://img.youtube.com/vi/FiqKPa9i6V4/0.jpg)](https://www.youtube.com/watch?v=FiqKPa9i6V4)


## Requirements
- Python 3.12
- Tibber API token (You can get it from [Tibber developer portal](https://developer.tibber.com/settings/access-token))

## Installation
1. Install `uv`:
   ```bash
   # On macOS and Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   
   ```powershell
   # On Windows
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. Clone this repository:
   ```
   git clone https://github.com/linkcd/tibber-mcp.git
   cd tibber-mcp
   ```

3. Set up the Python virtual environment and install dependencies:
   ```
   uv venv --python 3.12 && source .venv/bin/activate && uv pip install --requirement pyproject.toml
   ```

## Host Configuration
In Claude Desktop or Roo Code in VS
```json
{
   "mcpServers":{
      "tibber":{
         "command":"uv",
         "args":[
            "--directory",
            "[PATH-TO-ROOT-OF-THE-CLONED-TIBBER-MCP-FOLDER]",
            "run",
            "server.py"
         ],
         "env":{
            "TIBBER_API_TOKEN":"[YOUR-TIBBER-TOKEN]"
         }
      }
   }
}
```
> **IMPORTANT**: Replace `[YOUR-TIBBER-TOKEN]` with your actual token. Never commit actual credentials to version control.


### Available Tools
The server exposes the following tools that LLM can use:
1. **`get_consumption_data()`**: Get the hourly consumption data for the last 30 days, such as time period, total cost, base energy cost, and consumpted kwh
2. **`get_price_and_home_info()`**: Get price info (current, today and tomorrow) and home info (owner, address, subscription...)


## License
[MIT License](LICENSE)

## Acknowledgments
- This tool uses Anthropic's MCP framework
- Built with [FastMCP](https://github.com/jlowin/fastmcp) for server implementation
- The tibber ingeratoin is based on [pyTibber](https://github.com/Danielhiversen/pyTibber) library
