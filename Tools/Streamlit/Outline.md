## Outline
### 第一篇：入门篇（认识 Streamlit & 基础用法）
#### 第 1 章：初识 Streamlit

##### 什么是 Streamlit

- 与传统 Web 框架（Flask/Django）的对比
- 典型应用场景：数据可视化面板、模型 Demo、内部工具、原型验证

##### 环境搭建与快速上手

- 安装：pip install streamlit
- 新建第一个应用 hello.py
- 用命令运行：streamlit run hello.py
- 项目结构：单文件 vs 多文件项目

##### 基础脚本结构

- 线性脚本执行机制（非 request-response）
- st.title, st.header, st.write 等最常用函数
- Markdown 支持：st.markdown 和简单排版

### 第二篇：基础组件篇（常用控件与布局）
#### 第 2 章：文本、媒体与布局

##### 文本与基础显示

- st.title, st.header, st.subheader
- st.text, st.markdown, st.code
- 展示数据：st.write, st.dataframe, st.table

##### 媒体展示

- st.image, st.audio, st.video
- 本地文件 vs 网络资源

##### 布局控制

- st.sidebar：侧边栏的使用
- st.columns：多列布局
- st.expander：折叠区域
- st.tabs：多页签布局（简单分区）

#### 第 3 章：交互组件（Widgets）

##### 输入控件总览

- 文本输入：st.text_input, st.text_area
- 数字输入：st.number_input, st.slider
- 选择类：st.selectbox, st.multiselect, st.radio
- 日期 / 时间：st.date_input, st.time_input
- 文件上传：st.file_uploader

##### 按钮 & 表单

- st.button, st.checkbox 的基本使用
- st.form, st.form_submit_button：表单式交互（防止每次改动都重算）
- 典型模式：参数在 sidebar 中，结果在主区展示

### 第三篇：数据与可视化篇（数据处理 & 图表）
#### 第 4 章：数据加载与预处理

##### 读取数据

- 读取本地 CSV/Excel
- 通过 st.file_uploader 上传文件后读取
- 从网络接口 / 数据库读取数据（简单示例即可）

##### 数据预览与清洗

- 利用 pandas 进行简单数据处理（缺失值、筛选、排序）
- 在页面上展示处理后的数据表

#### 第 5 章：可视化库整合

##### 内置图表

- st.line_chart, st.bar_chart, st.area_chart
- 快速展示时间序列 / 分类数据

##### matplotlib / seaborn 集成

- 在 Streamlit 中展示 matplotlib 图
- 注意：plt 图像刷新与多图展示

##### plotly / altair 等交互图表

- 用 plotly.express 画交互图
- st.plotly_chart 的参数与使用
- 交互式图表与控件（下拉框）联动

### 第四篇：状态管理与多页面应用
#### 第 6 章：状态管理（Session State）

##### 为什么需要状态


- treamlit 的脚本重跑机制
- 在交互中「记住」用户操作 / 中间结果

##### st.session_state 使用

- 基本语法与读写
- 与 widgets 交互：key 的用法
- 示例：计数器、购物车、简单表单的状态保存

##### 缓存机制

- st.cache_data：缓存数据加载与计算结果
- st.cache_resource：缓存模型 / 客户端
- 失效策略与参数（ttl, max_entries 等）

#### 第 7 章：多页面 & 项目结构化

##### 多页面应用

- 官方多页面结构（pages 文件夹）
- 每个页面一个脚本的模式
- 页面间共享状态（使用 session_state）

##### 模块化项目

- 将逻辑、数据处理函数拆分到独立模块
- 公共组件函数的封装（如：画图函数、布局函数）

##### 导航设计

- 侧边栏导航 vs 顶部 tabs
- 页面路由与用户体验

### 第五篇：性能优化与部署
#### 第 8 章：性能与用户体验

##### 性能问题常见原因

- 重复读取大文件 / 大模型
- 每次交互都全量重算

##### 性能优化技巧

- 合理使用 st.cache_data / st.cache_resource
- 减少不必要的重绘
- 控制刷新频率：st.empty, st.progress
- 分步展示：st.tabs, st.expander 等减少信息拥挤

##### 更好的交互体验

- st.spinner 提示加载中
- 自定义提示信息、错误信息展示

#### 第 9 章：部署与线上运维（概念级）

根据你们环境选择重点讲解 1–2 种方式即可：

##### 常见部署方式简介

- Streamlit Community Cloud
- 本地服务器 / 内网服务器部署（streamlit run + 反向代理）
- 容器化部署：Docker 基本思路

##### Streamlit Community Cloud

- 通过 GitHub 导入项目
- 配置 requirements.txt
- 环境变量、Secrets 管理（如 API keys）

##### 生产级部署要点（简聊）

- 访问限制（密码 / 内网）
- 日志记录与错误排查
- 版本管理与回滚思路

### 第六篇：进阶与最佳实践
#### 第 10 章：与机器学习 / 深度学习集成

##### 典型 ML 工作流

- 加载训练好的模型（sklearn / xgboost / LightGBM 等）
- 前端输入特征 → 后端预测 → 可视化结果

##### 模型 Demo 实战示例

- 分类模型 Demo：上传 CSV 或手动输入参数
- 回归模型 Demo：预测结果 + 不确定性展示（误差条）

##### 与深度学习模型的集成（概念 + 简单示例）

- 例如：文本分类 / 情感分析、图像分类 Demo
- 模型加载缓存（st.cache_resource 避免每次重新加载）

#### 第 11 章：页面美化与自定义组件（视课程深度可选）

##### 页面主题与配置

- config.toml 中设置页面标题、图标和主题
- st.set_page_config 设置页面布局和初始状态

##### 样式与 CSS

- 使用 st.markdown + HTML / CSS 做简单美化
- 插入图标、颜色样式

##### （可选）自定义组件

- 介绍 streamlit-component-template
- 示例：嵌入第三方 JS 组件的基本思路

### 第七篇：综合项目实战
#### 第 12 章：综合项目 1 – 数据仪表盘

>目标： 从零构建一个可交互的数据分析仪表盘
>要点：

- 数据上传 / 选择
- 参数选择（时间区间、维度、指标）
- 多个图表联动（折线图 + 柱状图 + 数据表）
- 导出结果（下载 CSV / 图片思路介绍）

#### 第 13 章：综合项目 2 – ML 模型在线 Demo

>目标： 将一个已训练的模型部署为交互式 Web 应用。
>要点：

- 加载模型（sklearn / pickle / joblib）
- 参数输入界面设计（表单 + 默认值）
- 显示预测结果 + 置信度/概率
- 简单日志记录（记录预测历史在页面上展示）

