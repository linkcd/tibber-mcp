# Tibber MCP
This is [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) Server for [Tibber](https://tibber.com/), a Norwegian power supplier. 

You can run the MCP server locally and access it via the different host such as Claude Desktop or [Roo Code](https://marketplace.visualstudio.com/items?itemName=RooVeterinaryInc.roo-cline).

## Overview

This tool provides a convenient way to talk to [Tibber API](https://developer.tibber.com/docs), and query information such as current price and your consumption.

### Example Queries
Once connected to the MCP server, you can ask questions like:
- "Analyze my power consumption data and present the usual peak hours and any other interesting patterns in an easy-to-read format."
- "When did I use the most power yesterday?"
- "How much power I consumpted yesterday 7AM?"


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

## Usage
```
export TIBBER_API_TOKEN=[YOUR-TIBBER-TOKEN]
python server.py
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
            "[PATH-TO-ROOT-OF-THE-CLONED-FOLDER]/tibber-mcp",
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
The server exposes the following tools that Claude can use:

1. **`get_ec2_spend_last_day()`**: Retrieves EC2 spending data for the previous day


## License
[MIT License](LICENSE)

## Acknowledgments
- This tool uses Anthropic's MCP framework
- Built with [FastMCP](https://github.com/jlowin/fastmcp) for server implementation
- The tibber ingeratoin is based on [pyTibber](https://github.com/Danielhiversen/pyTibber) library
