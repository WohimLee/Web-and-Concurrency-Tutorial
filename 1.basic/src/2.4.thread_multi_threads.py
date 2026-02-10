import random
import threading
import time


def mimic_llm(prompt: str):
    current = threading.current_thread()
    print(f"[{prompt}] start, thread_name={current.name}, thread_id={threading.get_ident()}")

    for i in range(5):
        process_duration = random.uniform(0.2, 1.0)
        print(f"[{prompt}]. Heartbeat tick={i}, sleep={process_duration:.2f}s")
        time.sleep(process_duration)

    print(f"[{prompt}] done")


def run_multi_threads() -> None:
    worker_count = 4
    threads = []

    start_at = time.perf_counter()

    for i in range(worker_count):
        worker_name = f"worker-{i + 1}"
        prompt = worker_name
        t = threading.Thread(
            target=mimic_llm,
            args=(prompt,),
            name=worker_name,
        )
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    elapsed = time.perf_counter() - start_at
    print(f"All workers finished, elapsed={elapsed:.2f}s")


if __name__ == "__main__":
    run_multi_threads()
