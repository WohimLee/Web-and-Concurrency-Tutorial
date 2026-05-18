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


async def heartbeat(identifier=None):
    for i in range(5):
        process_duration = random.uniform(0.2, 1.0)
        print(f"[{identifier}] Heartbeat tick={i}, sleep={process_duration:.2f}s")
        await asyncio.sleep(process_duration)

# 心跳任务：用于观察事件循环有没有被卡住
async def ticker():
    start = time.perf_counter()
    while time.perf_counter() - start < 8:
        print(".", end="", flush=True)
        await asyncio.sleep(0.2)