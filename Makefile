inspector:
	npx @modelcontextprotocol/inspector \
	uv \
	run \
	mcp.server

server:
	uv run uvicorn src.server:app --reload --port 8000