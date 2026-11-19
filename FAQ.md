# 常见问题

英文版见 [FAQ.en.md](FAQ.en.md)。

## ArmilGrid 是什么？

ArmilGrid 是一个给 AI 助手用的职业成长 Skill。它把职业成长变成动作：先锁定目标岗位，分析技能差距，推荐工业级复杂度的项目，再把项目拆成一步步**边做边学**的 Markdown 课程。

## 怎么安装？

完整步骤见 README 的「安装」一节。简单说：把整个仓库放进助手 skills 目录下的 `armilgrid/` 文件夹，重启会话，然后执行 `/armil init`。

## 支持哪些助手？

任何从目录里加载 `SKILL.md` 的助手都支持（例如 Claude Code、豆包 Agent 及同类框架）。具体目录路径各家不同，以对应助手的文档为准。

## 中文还是英文？

主文档都是中文。`SKILL.md` 是中文主文档，英文版在 `SKILL.en.md`；README 中文主文档是 `README.md`，英文版是 `README.en.md`；其余文档同理（`FAQ.md` / `FAQ.en.md`、`CONTRIBUTING.md` / `CONTRIBUTING.en.md`、`CHANGELOG.md` / `CHANGELOG.en.md`、`CODE_OF_CONDUCT.md` / `CODE_OF_CONDUCT.en.md`）。命令两边完全一致。助手默认只加载 `SKILL.md`，想用英文指令就把 `SKILL.en.md` 改名替换过去。

## `generate project` 和 `generate course` 有什么区别？

- `/armil generate project` 给出 2–3 个项目构思，对准你的技能差距。
- `/armil generate course` 拿你选定的项目，拆成一个 `course/` 文件夹的 Markdown 课程——每节课都有学习目标、最小知识、动手任务（项目的一个真实部分）和验收标准。

## 我是完完全全的零基础，能用吗？

可以，这是核心场景之一。生成课程前 ArmilGrid 会先问你的基础水平；零基础用户拿到的是更小、脚手架更多的课时，从环境搭建开始。

## 我卡在某节课上了怎么办？

把准确报错信息和卡住的步骤告诉 ArmilGrid。它会先给最小提示——不是完整答案——你仍然卡住才会升级到具体修法。卡住的地方才是学习发生的地方。

## 会话之间会记住我的进度吗？

会。ArmilGrid 会写一份 `career-profile.md`（目标岗位、技能矩阵、项目、难度偏好），课程进度通过每节课验收标准里的勾选项记录。

## 怎么卸载？

把 skills 目录下的 `armilgrid/` 文件夹删掉即可。`career-profile.md` 和你自己的 `course/` 文件夹都是普通 Markdown 文件，留着就好——那是你自己的成果。

## 怎么报 bug 或提需求？

用仓库里的 Issue 模板（Bug report / Feature request）开 issue。

## 可以贡献吗？

可以，见 [CONTRIBUTING.md](CONTRIBUTING.md)。新领域模板、示例课程和翻译尤其受欢迎。

## 我还有别的问题。

开 issue，或者在使用 ArmilGrid 时直接问助手，它会带你走对应流程。
