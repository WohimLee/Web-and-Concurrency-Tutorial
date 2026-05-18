
import asyncio

'''
要并发，需要先把多个协程都“挂到 loop 上”，比如 asyncio.gather(...) 或 create_task(...)
'''

from utils import print_identity, heartbeat

async def mimic_llm(prompt: str):
    print_identity(identifier=prompt)

    heartbeat(identifier=prompt)

async def main():

    print_identity(identifier="run_coroutines")
    # 并发
    await asyncio.gather(
        mimic_llm("coroutine-1"),
        mimic_llm("coroutine-2"),
        mimic_llm("coroutine-3"),
    )




if __name__ == "__main__":

    asyncio.run(main())