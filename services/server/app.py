import websockets
import asyncio

async def handle_message(websocket, payload):
    """Recieves a message and broadcasts it to the rest of the clients
    params
    """
    payload = await websocket.recv()
    # broadcast
    # maybe store in sqlite

start_server = websockets.serve(handle_message, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
