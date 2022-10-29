import websockets
import asyncio
import logging

async def handle_message(websocket):
    """Recieves a message and broadcasts it to the rest of the clients
    params
    """
    logging.info("Listening for messages...")
    async for message in websocket:
        logging.debug("message received: %s", message)

async def main():
    logging.basicConfig(format="%(message)s", level=logging.DEBUG)
    async with websockets.serve(handle_message, "", 8763):
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())

