# 02 Week1 实验与作业

## 实验 1：最小并发

文件：`src/week1_01_event_loop_demo.py`

要求：

1. 把任务数量从 3 改到 10。
2. 把每个任务的 sleep 时间改成随机值。
3. 观察输出顺序。

结论问题：

- 为什么输出顺序不是任务创建顺序？

## 实验 2：await 的让出行为

文件：`src/week1_02_await_yield_demo.py`

要求：

1. 运行 `busy_no_await` 版本。
2. 运行 `busy_with_await` 版本。
3. 对比心跳任务（heartbeat）是否有机会运行。

结论问题：

- 协程为什么会“饿死”其他任务？

## 实验 3：Task 生命周期

文件：`src/week1_03_task_lifecycle.py`

要求：

1. 在 `cancel()` 之前和之后打印 `task.done()`。
2. 捕获 `CancelledError`。

结论问题：

- 取消是“立刻终止”还是“在下一个 await 点生效”？

## 作业

1. 写一个 `ticker(name, interval, n)` 协程。
2. 同时创建 3 个 ticker，间隔分别为 0.2/0.5/1.0 秒。
3. 让主协程等待全部结束。
4. 提交代码时附带 3 句说明：
- 观察到的执行顺序
- 你对 await 的理解
- 你如何保证主协程不提前退出
