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
async def get_user_info() -> str:
    """Get user information such as name and address
    """
    tibber_connection = tibber.Tibber(tibber_api_token, user_agent="change_this")
    await tibber_connection.update_info()
    name = tibber_connection.name

    home = tibber_connection.get_homes()[0]
    await home.fetch_consumption_data()
    await home.update_info()
    address = home.address1

    result = f"{name}, {address}"

    await tibber_connection.close_connection()
    return result

@mcp.tool()
async def get_price_info() -> str:
    """Get price info of electricity, the currency is NOK.
    """
    try:
        tibber_connection = tibber.Tibber(tibber_api_token, user_agent="change_this")
        await tibber_connection.update_info()
        
        homes = tibber_connection.get_homes()
        if not homes:
            logger.error("No homes found for this Tibber account")
            return "No homes found"
        
        home = homes[0]
        await home.update_price_info()

        await tibber_connection.close_connection()
        
        result = home.price_total
        logger.info(f"electricity price info: {result}")
        return str(result)
    
    except Exception as e:
        logger.error(f"Error retrieving price info: {e}")
        return f"Error: {str(e)}"

@mcp.tool()
async def get_consumption_data() -> str:
    """Get power consumption data for the last 30 days, the currency is NOK.
    """
    try:
        tibber_connection = tibber.Tibber(tibber_api_token, user_agent="change_this")
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
    # Initialize and run the server
    mcp.run(transport='stdio')