import time
import random
import asyncio
import threading

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

    print_identity(identifier="run_coroutine")
    # 同步
    await mimic_llm("coroutine-1")
    await mimic_llm("coroutine-2")
    await mimic_llm("coroutine-3")



if __name__ == "__main__":

    asyncio.run(main())