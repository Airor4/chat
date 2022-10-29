import asyncio
import logging
from websockets import server
from websockets.server import WebSocketServerProtocol
import secrets


CONNECTIONS = {}

async def handle_message(websocket: WebSocketServerProtocol) -> None:
    """Recieves a message and broadcasts it to the rest of the clients
    params
    """
    join_key = secrets.token_urlsafe(12)
    CONNECTIONS[join_key] = websocket
    logging.info("New player joined!")
    try:
        async for message in websocket:
            logging.debug("message received: %s", message)
            await websocket.send('fuck you')
    finally:
        del CONNECTIONS[join_key]

async def main() -> None:
    logging.basicConfig(format="%(message)s", level=logging.DEBUG)
    async with server.serve(handle_message, "", 8763):
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())

