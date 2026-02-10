# 05 Week3 I/O 实战

## 学习目标

- 把同步 I/O 脚本改造成 asyncio 版本。
- 学会重试、超时、背压、批处理。

## 实战主题

1. 同步 vs 异步的吞吐对比。
2. 重试与退避策略。
3. 生产者-消费者流水线。
4. 失败隔离与结果汇总。

## 本周代码

- `src/week3_01_sync_vs_async_io.py`
- `src/week3_02_retry_timeout.py`
- `src/week3_03_backpressure_pipeline.py`

## 关键方法

- `asyncio.to_thread`：把阻塞同步函数放入线程池，便于迁移旧代码。
- `asyncio.as_completed`：先完成先处理，降低尾延迟。
- `Queue(maxsize=N)`：提供背压，防止内存无限增长。

## 本周验收标准

- 能给旧同步脚本做“最小侵入改造”。
- 能写出超时 + 重试 + 限流的组合。
- 能解释为何流水线能提高整体吞吐。
