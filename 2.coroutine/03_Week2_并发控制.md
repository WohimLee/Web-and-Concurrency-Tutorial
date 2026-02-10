# 03 Week2 并发控制

## 学习目标

- 会用 asyncio 控制并发规模、超时、取消和共享状态。

## 核心能力

1. 批量等待：`asyncio.gather`
2. 超时控制：`asyncio.timeout` 或 `wait_for`
3. 并发限流：`asyncio.Semaphore`
4. 流水线：`asyncio.Queue`
5. 互斥保护：`asyncio.Lock`

## 本周代码

- `src/week2_01_gather_vs_sequential.py`
- `src/week2_02_timeout_and_cancel.py`
- `src/week2_03_semaphore_limit.py`
- `src/week2_04_queue_pipeline.py`
- `src/week2_05_lock_race_condition.py`

## 学习重点

- `gather` 不等于无限并发，应配合限流。
- 超时是常态，不是异常场景。
- 共享状态必须默认“不安全”，先加锁后优化。

## 本周验收标准

- 能写出“100 个任务，最多 10 个并发”。
- 能为关键调用加超时与取消处理。
- 能解释何时用 Queue 做背压。
