# 07 Week4 工程化

## 学习目标

- 写出可维护的异步服务骨架。
- 做好生命周期管理、优雅退出、日志和测试。

## 工程化主题

1. 结构化并发：`asyncio.TaskGroup`
2. 服务启动与停止流程
3. 信号处理与优雅退出
4. 统一日志与异常收敛
5. 异步单测（`pytest-asyncio`）

## 本周代码

- `src/week4_01_graceful_shutdown.py`
- `src/week4_02_taskgroup_service.py`
- `src/week4_03_structured_logging.py`
- `src/week4_04_cpu_bound_executor.py`
- `src/tests/test_timeout_cancel.py`
- `src/tests/test_queue_pipeline.py`

## 本周验收标准

- 能稳定启动和停止一个异步服务。
- 能在取消时清理资源，不留悬挂任务。
- 能写至少 2 个关键路径异步测试。
