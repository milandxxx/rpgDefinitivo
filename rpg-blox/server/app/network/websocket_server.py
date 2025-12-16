import asyncio
import websockets
import json

clients = set()

async def handler(ws):
    clients.add(ws)
    try:
        async for msg in ws:
            data = json.loads(msg)
            await ws.send(json.dumps({"status":"ok","action":data.get("action")}))
    finally:
        clients.remove(ws)

def start_server():
    print("Servidor iniciado en ws://0.0.0.0:8765")
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(handler, "0.0.0.0", 8765)
    )
    asyncio.get_event_loop().run_forever()
