import time
import asyncio


async def ofc():
    time.sleep(10)
    print("Sweet sleep")


#async def main():
#   task = asyncio.create_task(ofc())
#   print("Играть")
#   print("Yes")


asyncio.run(ofc())
