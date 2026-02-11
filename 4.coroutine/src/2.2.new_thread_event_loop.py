import time
import random
import asyncio
import threading

def print_identity(identifier):
    print()

    current = threading.current_thread()
    loop = asyncio.get_running_loop() # 必须在协程上下文里面使用

    print("[{}] start, thread_name={}, thread_id={}".format(
            identifier, current.name, threading.get_ident()
    ))
    print("[Event Loop]: {}, loop_id={}".format(loop, id(loop)))


async def mimic_llm(prompt: str):
    print_identity(identifier=prompt)

    for i in range(5):
        process_duration = random.uniform(0.2, 1.0)
        print(f"[{prompt}]. Heartbeat tick={i}, sleep={process_duration:.2f}s")
        time.sleep(process_duration)


def run_coroutine_in_loop_in_thread(prompt) -> None:
    # 新线程里要显式创建并设置事件循环
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(mimic_llm(prompt=prompt))
    finally:
        loop.close() # 只做 "关闭这个 loop 对象"
        asyncio.set_event_loop(None) # 把当前线程里“已设置的 current event loop 引用”清掉

async def main():
    print_identity(identifier="main")
    
    # 主线程
    await mimic_llm(prompt="mimic_llm in main event loop")

    # 子线程
    t = threading.Thread(target=run_coroutine_in_loop_in_thread, args=("mimic_llm in new event loop",), name="new thread")
    t.start()
    t.join()


if __name__ == "__main__":

    asyncio.run(main())