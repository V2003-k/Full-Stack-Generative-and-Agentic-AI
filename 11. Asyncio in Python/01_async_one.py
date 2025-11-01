import asyncio

async def brew_chai():
    print("Brewing Chai...")
    await asyncio.sleep(2)
    print("Chai is Ready")

asyncio.run(brew_chai())