# asyncio 系统课程（完整课件）

这是一套按 `概念 -> 小实验 -> 真实场景 -> 工程化` 组织的 asyncio 课程，完全独立于原有文件。

## 课程结构

- `00_环境准备.md`：Python 版本、运行方式、目录说明。
- `01_Week1_打底模型.md`：事件循环、协程、Task、await。
- `02_Week1_实验与作业.md`：Week1 的实验清单和作业。
- `03_Week2_并发控制.md`：gather、timeout、取消、Queue、Semaphore、Lock。
- `04_Week2_实验与作业.md`：Week2 的实验清单和作业。
- `05_Week3_IO实战.md`：批量 I/O、重试、背压、同步改异步。
- `06_Week3_实验与作业.md`：Week3 的实验清单和作业。
- `07_Week4_工程化.md`：生命周期、优雅退出、结构化并发、日志与测试。
- `08_Week4_实验与作业.md`：Week4 的实验清单和作业。
- `09_常见误区与排障.md`：最常见错误与诊断步骤。
- `10_7天冲刺计划.md`：短期高强度学习版本。
- `src/`：所有可运行代码。

## 快速开始

```bash
cd Tools/asyncio库/course
python3 src/week1_01_event_loop_demo.py
```

## 推荐学习节奏

1. 每天 45-90 分钟。
2. 先读当周主课件，再跑代码。
3. 每个实验按顺序做：先正常跑，再故意制造异常，再修复。
4. 每天记录三行：现象、原因、修复。

## Python 版本

建议 Python 3.11+（本仓库是 3.12），因为示例使用了 `asyncio.TaskGroup`。

## 测试（可选）

```bash
pip install pytest pytest-asyncio
pytest -q src/tests
```
