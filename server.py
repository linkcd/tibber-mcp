import os
import tibber
import asyncio
import logging

from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

tibber_api_token = os.environ.get('TIBBER_API_TOKEN') 

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("tibber-mcp")


@mcp.tool()
async def get_price_and_home_info() -> str:
    """Get the infomation of:
        1. current price, with price break down, price level, and currency
        2. hourly price and price level of today
        3. hourly price and price level of tomorrow
        4. home address info, timezone etc
    the currency is applying to all prices
    """
    try:
        tibber_connection = tibber.Tibber(tibber_api_token, user_agent="tibber-mcp")
        await tibber_connection.update_info()
        
        homes = tibber_connection.get_homes()
        if not homes:
            logger.error("No homes found for this Tibber account")
            return "No homes found"
        
        home = homes[0]
        await home.update_info_and_price_info() #using predefined query UPDATE_INFO_PRICE for getting most of info such as current price, today and tomorrow price, home info and subscription etc
        result = home.info 

        await tibber_connection.close_connection()
        return str(result)
    
    except Exception as e:
        logger.error(f"Error retrieving price info: {e}")
        return f"Error: {str(e)}"

@mcp.tool()
async def get_consumption_data() -> str:
    """Get the hourly consumption data for the last 30 days, such as time period, total cost, base energy cost, and consumpted kwh.
    """
    try:
        tibber_connection = tibber.Tibber(tibber_api_token, user_agent="tibber-mcp")
        await tibber_connection.update_info()
        
        homes = tibber_connection.get_homes()
        if not homes:
            logger.error("No homes found for this Tibber account")
            return "No homes found"
        
        home = homes[0]
        await home.fetch_consumption_data()

        await tibber_connection.close_connection()

        result = home.hourly_consumption_data
        return str(result)
    
    except Exception as e:
        logger.error(f"Error retrieving price info: {e}")
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Run the server with the specified transport
    mcp.run(transport=os.environ.get('MCP_TRANSPORT', 'stdio'))