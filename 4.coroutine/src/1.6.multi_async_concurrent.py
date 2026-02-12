import time
import random
import asyncio
import threading

'''
要并发，需要先把多个协程都“挂到 loop 上”，比如 asyncio.gather(...) 或 create_task(...)
'''

def print_identity(identifier):
    print()

    current = threading.current_thread()
    print(
        "[{}] start, thread_name={}, thread_id={}".format(
            identifier, current.name, threading.get_ident()
        )
    )

async def mimic_llm(prompt: str):
    print_identity(identifier=prompt)

    for i in range(5):
        process_duration = random.uniform(0.2, 1.0)
        print(f"[{prompt}]. Heartbeat tick={i}, sleep={process_duration:.2f}s")
        await asyncio.sleep(process_duration)

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