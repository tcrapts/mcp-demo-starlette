# An MCP server with Starlette
This project demonstrates how to add real-time weather information to Large Language Models using a [Model Context Protocol Server (MCP)](https://modelcontextprotocol.io/introduction).

## Usage
1. Start the MCP server: `uv run uvicorn src.server:app --reload --port 8000`
2. Run the client: `uv run python -m src.client "What is the current weather in Barcelona?"`

Optional: you can inspect the MCP server using the [Inspector](https://github.com/modelcontextprotocol/inspector). This requires `npx` to be installed.

```bash
npx @modelcontextprotocol/inspector uv run src.server
```
A web interface will be available at port 6274.

Result:
```bash
The current weather in Barcelona is as follows:
• Temperature: 13.9°C
• Wind Speed: 5.8 km/h coming from the south (180°)
• It is currently nighttime, as indicated by the "is_day" value of 0.
• The weather code is 80, which typically suggests the presence of rain showers.

Please note that the weather code provides a general idea of the conditions but may need additional interpretation for specifics. Enjoy your time in Barcelona!
```

## How it works
The demo consists of three files: 

1. `tools.py`: defines an MCP server with tools.
2. `server.py`: expoes the MCP server over HTTP.
3. `client.py`: uses the MCP server with Pydantic AI.

