


import asyncio


from utils import print_identity

async def mimic_llm():
    print_identity(identifier="mimic_llm")
    await asyncio.sleep(2)


async def main():
    print_identity(identifier="main")

    await asyncio.gather(mimic_llm())
    return


if __name__ == "__main__":


    asyncio.run(main())