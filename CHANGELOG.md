# 更新日志

英文版见 [CHANGELOG.en.md](CHANGELOG.en.md)。

本文件记录本项目所有值得注意的变更。

格式遵循 [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)，版本号遵循 [语义化版本](https://semver.org/spec/v2.0.0.html)。

## [未发布]

### 变更

- 新增 `docs/ROADMAP.md` / `ROADMAP.en.md`：调研同类项目（career-ops、Resume-Matcher、Reactive Resume、JSON Resume、JobSpy）后给出的后续方向、优先级与退出条件；README 增一节指针
- 删除 `preview/`：技术栈看板 HTML 与截图一并移出，仓库只剩 skill 文档、示例与简历工具
- README 去掉「设计预览」小节与看板截图：README 只讲能做什么，看板 HTML 仍留在 `preview/` 自行打开
- 新增独立模块「简历生成」与指令 `/CareerOS build resume`：从档案、项目、课程验收起草，一岗一版，输出结构化 JSON
- 新增 `tools/resume-builder/index.html`：离线单文件简历编辑器，中英双版共享一份数据、A4 实时预览、本地自动保存、JSON 导入导出、打印成 PDF、9 项 ATS 自查
- `references/methodology.md` 增「简历生成口径」；`docs/agent/DESIGN.md` 的工具条目扩为「简历生成与评估」
- 仓库去掉装饰图：横幅、社交预览图、移动端截图与看板体检报告一并删除，只留一张整页截图（README 顶部横幅同步去掉）
- 融合碎片文档：`templates/README.md` 的模板规则并入 `CONTRIBUTING.md` 的「新增领域模板」一节，不再单独成文
- 主文档补齐英文版：新增 `docs/agent/DESIGN.en.md`、`references/methodology.en.md`，CI 的中英配对检查同步覆盖这两对
- 清理 `preview/_shots` 的 6 张派生切片，只保留桌面 / 移动整页截图
- 仓库由 `career-os-skill` 更名为 `career-os-agent`（旧地址自动重定向）：skill 层留在根目录，Agent 规划文档收进 `docs/agent/`，技术栈看板预览放进 `preview/`
- 新增 `docs/agent/DESIGN.md`：能力清单、架构设计、Python 先修合并为一份设计方案
- `README.md` / `README.en.md` 重写为双层门面：上层写 skill 怎么装怎么用，下层写 Agent 要做什么
- 移除 `SKILL.zh-CN.md`（内容已并入中文主文档 `SKILL.md`）
- 文档语言改为**中文优先**：`SKILL.md` 改为中文主文档，原英文版转存为 `SKILL.en.md`，原 `SKILL.zh-CN.md` 移除（助手仍只加载 `SKILL.md`，无需改安装方式）
- `FAQ` / `CONTRIBUTING` / `CODE_OF_CONDUCT` / `CHANGELOG` 改为中文，英文版分别保留为 `*.en.md`
- `templates/` 说明与领域模板、`.github/ISSUE_TEMPLATE/` 模板改为中文
- 校验脚本与单元测试改为检查 `SKILL.md` / `SKILL.en.md` 与中英配对文档

## [0.7.1] - 2026-09-26

### 新增

- 交互指南：心态支持 —— 把"现在开始是不是来不及了""为什么没早点学"这类情绪当真实信号处理：先接住，再重新框定（"你不会再有比今天更年轻的一天"），用"重来一遍结局会不会变"判断是否该放下，把焦虑转成当前最小的下一步，且绝不虚假吹捧
- 第五阶段：抗问穿清单 —— 每个项目都必须扛得住五个深挖问题（为什么用这套技术、极端情况怎么处理、个人贡献边界、重做会改哪里、哪个数字证明有效）；要求真实且可展开，绝不教用户编造经历
- 模拟笔试：每题标注模式（核心代码 / ACM），按时间预算分流的备考策略（模块化题单 vs LeetCode Hot 100、CodeTop 等高频题集，标注为社区常用资源），以及三遍间隔重复刷题法
- 模拟面试：每答一题的反馈里增加"表达提示"（节奏、先结论后细节、被追问时的流畅度）
- 第三阶段：四维技术栈选型框架（岗位存量、可迁移性、竞争与学习成本、社区与生命周期），标注为基于通用经验的推断
- 第四阶段：明确的"行动 → 感知 → 反思 → 调整"学习闭环
- 公司情报：确立设计原则"投递前先查公司，把信息差补上"

### 变更

- `references/methodology.md`：补充技术栈选型维度、笔试备考策略、抗问穿标准、心态支持口径

## [0.7.0] - 2026-09-19

### 新增

- 新能力：公司情报 —— 从公开来源查证目标公司的面试流程、笔试风格与薪资，并定下硬规则：没有公开数据就留空，绝不推断
- 新能力：招聘全流程模拟 —— 走完整招聘流水线（投简历 → 初筛 → 笔试 → 面试 → 结果），由 Skill 扮演招聘方，阶段之间设硬门禁
- 新指令：`/CareerOS company`、`/CareerOS simulate`（含自然语言触发词）
- `SKILL.md` / `SKILL.zh-CN.md`：新增公司情报与招聘全流程模拟两节，并补指令表行
- `references/methodology.md`：补充公司情报数据纪律与流水线评分规则

## [0.6.0] - 2026-09-18

### 新增

- `SKILL.md` / `SKILL.zh-CN.md`：新增"证据、默认值与局限"一节 —— 推荐一律标注为基于通用经验（不是官方岗位数据），区分事实与推断，不承诺 offer，并对信息稀少的领域做明确处理
- 默认档案规则：用户拒绝提供背景时，改用显式标注的默认档（零基础、每周 8 小时、先探索后定方向），而不是默默假设
- 新增 `references/methodology.md`：能力雷达、水平锚点、差距评分、难度校准、课程粒度、简历评估维度、模拟面试反馈与局限的计算口径

### 变更

- README 默认改为简体中文；英文版移到新的 `README.en.md`；删除 `README.zh-CN.md`（两份 README 互相链接）
- README：用更平实的语言重写简介（去掉模板腔），修正安装步骤为克隆整个仓库（templates 与 examples 会被 Skill 引用），并在核心模块列表里补上简历评估与模拟笔试面试
- `CONTRIBUTING.md`：语言规范引用更新为 `README.md` / `README.en.md`

## [0.5.0] - 2026-09-17

### 新增

- 新能力：模拟笔试与面试 —— 限时笔试（默认 5 题，作答后按评分标准批改）与一次一题的面试演练（技术 / 行为 / 系统设计 / HR 轮），每题给反馈，结束时汇总并把强项与缺口写回职业档案
- 新指令：`/CareerOS mock interview`、`/CareerOS mock test`（含自然语言触发词）
- `SKILL.md` / `SKILL.zh-CN.md`：新增模拟笔试与面试一节，并补指令表行

## [0.4.0] - 2026-09-17

### 新增

- 新能力：简历评估 —— 六个维度打分（可扫读性、成果优先于职责、岗位匹配、项目与技术表述、差异化、细节打磨），输出总分 + 按优先级排列的问题 + 改写示例，并把发现回写到职业档案与差距分析
- 新指令：`/CareerOS review resume`（含自然语言触发词）
- `SKILL.md` / `SKILL.zh-CN.md`：新增简历评估一节，并补指令表行

## [0.3.0] - 2026-09-08

### 新增

- 零基础课程示例（[`examples/course-zero/`](examples/course-zero/00-course-overview.md)）：总览 + 前两节课，展示课程如何适配完全零基础的用户
- 学习排期生成：按每周可投入时间生成逐周课程计划，写进课程总览

### 变更

- `SKILL.md` / `SKILL.zh-CN.md`：六轴能力雷达标准化（语言与框架、数据与存储、工程实践、架构与设计、领域知识、软技能）
- `SKILL.md` / `SKILL.zh-CN.md`：初 / 中 / 高三档水平锚点
- `SKILL.md` / `SKILL.zh-CN.md`：成长路径规划 —— 每个目标岗位给一条三项目串行路径（Foundation → Capability → Showcase）
- `SKILL.md` / `SKILL.zh-CN.md`：第四阶段增加课程排期步骤（0.3.0 版）
- CI：版本一致性校验（SKILL ↔ README 徽章 ↔ CHANGELOG）

## [0.2.0] - 2026-09-08

### 新增

- YAML front matter（name、description、version）
- 第四阶段 课程生成器 —— 边做边学的 Markdown 课程
- 指令参考、卡点救援协议、领域模板库三节
- 难度档位校准与里程碑反馈闭环
- 通过 `career-profile.md` 与课程进度实现状态持久化
- 领域模板库（[`templates/`](templates/README.md)）
- 课程示例（[`examples/course/`](examples/course/00-course-overview.md)）
- FAQ（[`FAQ.md`](FAQ.md)）
- CI 工作流：校验 front matter、链接与更新日志
- 行为准则、issue 模板、仓库横幅与社会预览图
- 贡献指南（[`CONTRIBUTING.md`](CONTRIBUTING.md)）
- 中英双语 README，含横幅、徽章、安装说明与新指令

## [0.1.0] - 2026-09-08

### 新增

- 项目初始骨架：仓库、README 说明、MIT LICENSE
