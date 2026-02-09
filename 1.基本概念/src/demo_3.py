import multiprocessing as mp
import os
import time


def child_task() -> None:
    print(f"[child] pid={os.getpid()} ppid={os.getppid()}")
    time.sleep(1)
    print("[child] done")


if __name__ == "__main__":
    print(f"[parent] pid={os.getpid()}")
    p = mp.Process(target=child_task)
    p.start()
    print(f"[parent] started child pid={p.pid}")
    p.join()
    print("[parent] child joined, parent done")
