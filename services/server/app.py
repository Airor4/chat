import websockets
import asyncio

async def handle_message(websocket):
    """Recieves a message and broadcasts it to the rest of the clients
    params
    """
    print('blahhhh')
    async for message in websocket:
        print(message)

async def main():
    async with websockets.serve(handle_message, "", 8763):
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())