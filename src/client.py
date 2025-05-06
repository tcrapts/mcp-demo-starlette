import asyncio

from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerHTTP
from dotenv import load_dotenv
import sys

load_dotenv()

server = MCPServerHTTP(url="http://localhost:8000/sse")

agent = Agent(
    model="o3-mini",
    mcp_servers=[server],
)


async def main():
    prompt = sys.argv[1]
    async with agent.run_mcp_servers():
        result = await agent.run(prompt)
    print(result.output)


if __name__ == "__main__":
    asyncio.run(main())
