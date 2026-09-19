# CareerOS

![CareerOS banner](assets/careeros-banner.jpg)

> 一套为你的职业成长而设计的操作系统。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.7.0-blue.svg)](CHANGELOG.md)
[![Last Commit](https://img.shields.io/github/last-commit/Duckweed-yhb/career-os-skill)](https://github.com/Duckweed-yhb/career-os-skill)

**[English](README.en.md) | [简体中文](README.md)**

---

## 简介

**CareerOS** 是一个给 AI 助手的职业成长技能。输入你的背景和目标，它输出一条可执行的路线：先锁定目标岗位，对照岗位要求找出你的技能差距，再用一个真实项目把这些差距补上——项目会拆成一节节 Markdown 课程，边做边学，最后攒成能写进简历的作品。

整个流程会根据你的领域、经验水平和每周能投入的时间调整，不会给你塞超出能力范围的东西。

## 安装

1. **克隆仓库**（或下载后解压）：

   ```bash
   git clone https://github.com/Duckweed-yhb/career-os-skill.git
   ```

2. **找到你所用 AI 助手的 skills 目录：**

   | 助手 | Skills 目录 |
   |---|---|
   | Claude Code | `~/.claude/skills/` |
   | 豆包 Agent | `<workspace>/.skills/` |
   | 其他助手 | 查阅对应助手的文档，确认 skills 目录位置 |

3. **把 Skill 放进该目录下的 `career-os/` 文件夹**——整个仓库一起放，课程模板和示例也会被用到：

   ```bash
   # 示例（Claude Code）：直接把整个仓库克隆到 skills 目录
   git clone https://github.com/Duckweed-yhb/career-os-skill.git ~/.claude/skills/career-os
   ```

   仓库里同时有 `SKILL.md`（英文）和 `SKILL.zh-CN.md`（简体中文），助手会自动加载对应语言版本，不需要手动挑文件。

4. **重启助手会话**并验证：

   ```text
   /CareerOS init
   ```

   看到初始化欢迎语，就说明安装成功了。

## 核心模块

就像操作系统管理硬件资源一样，CareerOS 管理你的职业资源：

### 1. 目标定位
- 解析你的兴趣与背景，锁定高潜力的目标岗位。
- 生成该岗位的能力雷达图。

### 2. 技能差距分析
- 对比你当前的简历/技能与目标岗位的要求。
- 识别出关键的缺失环节。

### 3. 项目生成器
- **拒绝玩具项目。** 根据缺失的技能点，生成具有工业级复杂度的实战项目构思。
- 包含技术栈建议、难点预测和验收标准。

### 4. 课程生成器
- 把选定项目变成一步步**边做边学**的课程。
- 生成技术栈学习路线与项目开发路线，再把整个项目拆成一节节 Markdown 课程——每节都带动手任务和验收标准。

### 5. 作品集构建
- 将项目转化为面试中的亮点。
- 提供简历描述优化建议和 GitHub README 撰写指南。

### 6. 简历评估
- 从可扫读性、成果量化、岗位匹配、技术表述等 6 个维度给你的简历打分。
- 按"必修 / 建议 / 可选"列出问题清单，高优先级问题附"原文 → 改写"示例。

### 7. 模拟笔试与面试
- **模拟面试**：一次一题、等你回答后再出下一题，每答一题给反馈，结束汇总强项与缺口。
- **模拟笔试**：按目标岗位出限时题目，作答后逐题打分并给改进方向。

### 8. 公司情报
- 针对目标公司，查证它的面试流程、笔试风格与薪资待遇——每条信息带来源和时效。
- 查不到公开信息的字段一律留空，绝不编造。

### 9. 招聘全流程模拟
- 从投简历开始走完整流程：简历初筛 → 笔试 → 面试 → 综合结果，每阶段通过才进入下一阶段。
- Skill 全程扮演招聘方，反馈区分"模拟判定"与"真实建议"。

## 使用方式

在你的 AI 助手中加载 `CareerOS` Skill，然后尝试：

```text
/CareerOS init
/CareerOS analyze [你的简历内容或当前技能列表]
/CareerOS generate project --focus=[具体技术点，如 Redis/微服务]
/CareerOS generate course [项目]  # 把选定项目拆成边做边学的课程
/CareerOS review resume [简历]    # 评估简历，找出还能完善的地方
/CareerOS mock interview [岗位]   # 一次一题的面试演练，带反馈
/CareerOS mock test [岗位]        # 限时笔试练习，带评分
/CareerOS company [公司] [岗位]   # 查证某公司的面试流程、笔试题方向与薪资
/CareerOS simulate [公司] [岗位]  # 走一遍"投简历→初筛→笔试→面试"完整流程
```

完整流程示例见 [examples/frontend-to-fullstack.md](examples/frontend-to-fullstack.md)。有问题？看 [FAQ](FAQ.md)。

## 为什么选择 CareerOS？

- **行动导向** —— 从"输入模式"切换到"输出模式"。
- **语境感知** —— 理解你的经验水平，不推荐过难或过简单的任务。
- **结果驱动** —— 一切为了那个能写在简历上的作品。

## 许可证

[MIT License](LICENSE)

---

Made with ❤️ by Duckweed-yhb
