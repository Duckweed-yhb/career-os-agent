# 贡献指南

英文版见 [CONTRIBUTING.en.md](CONTRIBUTING.en.md)。

先说一句：谢谢你愿意花时间参与。

## 可以贡献什么

- **技能提示词改进** —— 让 `/CareerOS` 的指令更聪明，增加新子命令，或打磨判断逻辑。
- **项目推荐规则** —— 为目标岗位、技术栈、难度校准或验收标准补充新模板。
- **示例** —— `examples/` 下的真实对话走查。好的示例要能把从 `init` 到项目推荐的完整流程走一遍。
- **文档** —— 修错别字、把表述讲清楚、改进 README。
- **翻译** —— 维护或补充多语言文档（目前是中文和英文双版）。

## 开始之前

1. **Fork** 仓库并克隆到本地。
2. **建分支**，名字写清楚要干什么：

   ```bash
   git checkout -b feat/your-feature
   ```

3. **改代码 / 文档**。一个 pull request 只做一件事。
4. **提交**，commit message 写清楚：

   ```bash
   git commit -m "feat: add X"        # 新能力
   git commit -m "fix: correct Y"     # 修 bug
   git commit -m "docs: update Z"     # 只改文档
   ```

5. **推送**并向 `main` 开 **Pull Request**。

## 约定

- **一个文件一种语言。** 中英内容不要混在同一个文件里。参照 `README.md`（中文）/ `README.en.md`（英文）的配对方式：主文档中文，英文版加 `.en.md` 后缀。
- **示例要可复现。** 示例对话必须和 README 里当前记录的指令集一致。
- **更新 CHANGELOG。** 凡是用户可见的改动，都在 `[Unreleased]` 下的 `新增` / `变更` / `修复` 里补一条。

## Pull Request 检查清单

- [ ] 这次改动只解决一个明确的问题。
- [ ] 每个被改动的文件内部语言一致。
- [ ] 用户可见的改动已更新 `CHANGELOG.md`。
- [ ] PR 描述说明了*改了什么*和*为什么改*。

## 需要帮助

有疑问或想法还没把握，先开 issue —— 先讨论再动手，大家都省时间。
