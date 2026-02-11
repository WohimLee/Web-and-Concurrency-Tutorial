import time
import random
import asyncio
import threading

def print_identity(identifier):
    print()

    current = threading.current_thread()
    loop = asyncio.get_running_loop() # 必须在协程上下文才能使用

    print("[{}] start, thread_name={}, thread_id={}".format(
            identifier, current.name, threading.get_ident()
    ))
    print("[Event Loop]: {}, loop_id={}".format(loop, id(loop)))


async def mimic_llm(prompt: str):

    print_identity(identifier=prompt)

    for i in range(5):
        process_duration = random.uniform(0.2, 1.0)
        print("[{}]. Heartbeat tick={}, sleep={:.2f}s".format(
            prompt, i, process_duration
        ))
        await asyncio.sleep(process_duration)

async def main():

    print_identity(identifier="run_coroutine")

    await mimic_llm(prompt="First coroutine.")


if __name__ == "__main__":

    asyncio.run(main())