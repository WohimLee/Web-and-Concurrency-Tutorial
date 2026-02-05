import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor

# 用于执行任务的阻塞函数
def blocking_task():
    print(f"\nRunning in thread ID: {threading.get_ident()}, thread name: {threading.current_thread().name}\n")

async def use_default_executor():
    """使用默认线程池运行任务"""
    loop = asyncio.get_event_loop()

    print("Before running in default executor")
    # 使用默认线程池
    result = await loop.run_in_executor(None, blocking_task)
    print("After running in default executor")

async def use_custom_executor():
    """使用自定义线程池运行任务"""
    loop = asyncio.get_event_loop()

    # 创建自定义线程池
    shadowhunter_executor = ThreadPoolExecutor(max_workers=4, thread_name_prefix="ShadowHunter")
    dealbrain_executor    = ThreadPoolExecutor(max_workers=4, thread_name_prefix="DealBrain")
    

    # 打印线程池对象的类型和内存地址
    print(f"Custom Executor Type: {type(shadowhunter_executor)}")
    print(f"Custom Executor ID: {id(shadowhunter_executor)}")

    print("Before running in custom executor")
    # 使用自定义线程池
    result = await loop.run_in_executor(shadowhunter_executor, blocking_task)
    print("After running in custom executor")

def main():
    print("Testing with asyncio default executor:")
    asyncio.run(use_default_executor())
    
    print("\nTesting with custom ThreadPoolExecutor:")
    asyncio.run(use_custom_executor())

if __name__ == "__main__":
    main()
