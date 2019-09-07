import asyncio
import websockets

async def message():
	async with websockets.connect("ws://anant1.herokuapp.com:1234") as socket:
		print('what do you want to send')
		message = input()
		await socket.send(message)
		print(await socket.recv())

asyncio.get_event_loop().run_until_complete(message())
