import time
import random
import asyncio
import threading

def print_identity(identifier):
    print()

    current = threading.current_thread()
    loop = asyncio.get_running_loop() # 必须在协程上下文里面使用
    task = asyncio.current_task().get_name()

    print("[{}] start, thread_name={}, thread_id={}".format(
            identifier, current.name, threading.get_ident()
    ))
    print("[Event Loop]: {}, loop_id={}".format(loop, id(loop)))
    print("[Task]: {}, task_id={}".format(task, id(task)))


async def mimic_llm(prompt: str):
    print_identity(identifier=prompt)
    for i in range(5):
        process_duration = random.uniform(0.2, 1.0)
        print(f"[{prompt}]. Heartbeat tick={i}, sleep={process_duration:.2f}s")
        time.sleep(process_duration)

async def main():
    
    print_identity(identifier="main")
    task = asyncio.create_task(mimic_llm("First coroutine."))
    await task


if __name__ == "__main__":

    asyncio.run(main())