
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
