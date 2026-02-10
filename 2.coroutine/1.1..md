# 01 Week1 打底模型

## 学习目标

- 搞清楚 `event loop`、`coroutine`、`Task`、`await` 的关系。
- 能解释“为什么 `await` 才会让出执行权”。

## 核心概念

1. 协程函数：`async def` 定义，调用后返回协程对象。
2. `await`：挂起当前协程，把控制权交回事件循环。
3. 任务 `Task`：事件循环调度协程的包装对象。
4. 事件循环：负责在“可继续运行”的任务之间切换。

## 先看一个心智模型

- 线程是操作系统调度。
- 协程是事件循环调度。
- 协程必须在 `await` 点主动交棒。

## 本周代码

- `src/week1_01_event_loop_demo.py`
- `src/week1_02_await_yield_demo.py`
- `src/week1_03_task_lifecycle.py`

## 建议练习顺序

1. 先跑 `week1_01`，理解并发输出交错。
2. 跑 `week1_02`，对比“有 await / 无 await”的差异。
3. 跑 `week1_03`，观察 Task 状态与取消行为。

## 本周验收标准

- 你可以口头讲清楚：协程为什么不会自动并行。
- 你可以写出：`asyncio.run(main()) + create_task + await`。
