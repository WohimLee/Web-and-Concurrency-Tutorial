import asyncio

async def A():
    await asyncio.sleep(1)



async def B():
    await A()



async def C():
    await B()

async def main():
    await C()
