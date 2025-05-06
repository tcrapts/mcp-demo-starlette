import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather tool")


@mcp.tool()
async def fetch_weather(latitude: float, longitude: float) -> str:
    """Fetch current weather for a location defined by latitude and longitude."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current_weather": True,
            },
        )
        return response.text
