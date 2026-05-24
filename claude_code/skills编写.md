# Claude Code Skills 编写指南

## 一、什么是 Skill？

Skill 是 Claude Code 的扩展机制，通过 Markdown 文件定义可复用的指令集、工作流或领域知识。

### 核心价值
- **可复用** - 一次定义，随处使用
- **可分享** - 团队共享最佳实践
- **标准化** - 避免重复解释
- **高效** - 一键完成复杂任务

### Skill vs MCP vs 传统 Prompt

| 维度 | Skill | MCP | 传统 Prompt |
|------|-------|-----|-------------|
| 定位 | Prompt编译器 | 外部工具连接器 | 单次指令 |
| 复用性 | 高 | 中 | 低 |
| 上下文管理 | 按需加载 | 实时调用 | 全量携带 |
| 适用场景 | 领域知识封装 | 外部能力扩展 | 简单任务 |

---

## 二、Skill 目录结构

### 标准结构
```
my-skill/
├── SKILL.md           # 必需：技能定义文件
├── template.md        # 可选：输出模板
├── scripts/           # 可选：辅助脚本
│   └── validate.sh
├── references/        # 可选：参考文档
│   └── coding_standards.md
├── examples/          # 可选：示例文件
│   └── sample.md
└── assets/            # 可选：资源文件
```

### 存储路径

| 路径 | 适用范围 |
|------|----------|
| `~/.claude/skills/` | 个人全局（所有项目可用） |
| `.claude/skills/` | 项目专属（仅当前项目可用） |

---

## 三、SKILL.md 文件结构

SKILL.md 由两部分组成：**YAML frontmatter（元数据）** + **Markdown 正文（执行指令）**

### 3.1 YAML Frontmatter 字段

```yaml
---
name: my-skill                    # 必需：技能名（小写、连字符分隔）
description: 技能描述和触发条件      # 必需：何时触发、做什么
version: "1.0.0"                  # 可选：版本号
author: your-name                 # 可选：作者
tags: [code-review, quality]      # 可选：标签
argument-hint: "[file-path]"      # 可选：参数提示
allowed-tools: [Read, Edit, Bash] # 可选：允许使用的工具
disable-model-invocation: false   # 可选：是否禁用模型调用
---
```

### 3.2 字段详解

#### name（必需）
- 技能标识符，用于 `/技能名` 调用
- 命名规则：小写字母、连字符分隔
- 示例：`code-review`、`api-design`、`git-helper`

#### description（必需）
- 技能描述，**这是主要的触发机制**
- 应包含：做什么 + 何时使用
- 建议：写得"主动"一些，避免"欠触发"

```yaml
# ❌ 欠触发示例
description: 代码审查工具

# ✅ 推荐示例
description: 专业的代码审查专家。当用户提到代码审查、代码质量、代码检查、PR审查时自动触发。
```

#### allowed-tools（可选）
限制技能可使用的工具：

```yaml
allowed-tools: [Read, Grep, Edit, Bash, WebSearch]
```

常用工具列表：
- `Read` - 读取文件
- `Edit` - 编辑文件
- `Write` - 写入文件
- `Grep` - 搜索内容
- `Bash` - 执行命令
- `WebSearch` - 网络搜索
- `WebFetch` - 获取网页

---

## 四、创建第一个 Skill

### 步骤 1：创建目录

```powershell
# 创建个人全局技能目录
mkdir -p ~/.claude/skills/hello-world

# 或创建项目专属技能目录
mkdir -p .claude/skills/hello-world
```

### 步骤 2：编写 SKILL.md

```markdown
---
name: hello-world
description: 我的第一个 Skill - 打印问候语
version: "1.0.0"
argument-hint: "[name]"
---

# Hello World Skill

当用户调用 `/hello-world` 时，执行以下操作：

1. 读取用户提供的 name 参数（默认为 "World"）
2. 生成友好的问候消息
3. 添加欢迎信息

## 输出格式

✨ Hello, {name}!
欢迎来到 Claude Code Skills 的世界。
```

### 步骤 3：测试调用

```bash
# 手动调用
/hello-world

# 带参数调用
/hello-world Alice
```

---

## 五、实战案例

### 案例 1：代码审查 Skill

```markdown
---
name: code-review
description: 专业的代码审查专家。当用户提到代码审查、代码质量、PR审查、代码检查时自动触发。
allowed-tools: [Read, Grep, Edit]
---

# 代码审查专家

你是一位经验丰富的代码审查专家。请对提供的代码进行以下检查：

## 审查清单

### 1. 安全性
- [ ] SQL 注入风险
- [ ] XSS 漏洞
- [ ] 敏感信息硬编码
- [ ] 输入验证完整性

### 2. 性能
- [ ] N+1 查询问题
- [ ] 循环中的性能瓶颈
- [ ] 内存泄漏风险

### 3. 可维护性
- [ ] 命名规范
- [ ] 单一职责原则
- [ ] 重复代码
- [ ] 注释充分性

### 4. 最佳实践
- [ ] 语言/框架惯用法
- [ ] 错误处理规范
- [ ] 测试覆盖

## 输出格式

# 代码审查报告

## 总体评分：X/10

## 🔴 严重问题（必须修复）
- `file:line`：问题描述

## 🟡 警告（建议修复）
- `file:line`：问题描述

## 🟢 建议（可选优化）
- `file:line`：优化建议

## ✅ 优秀实践
- 值得表扬的地方
```

### 案例 2：API 设计审查 Skill

```markdown
---
name: api-design-review
description: API 设计审查专家。当用户提到 API 设计、RESTful、接口设计时自动触发。
allowed-tools: [Read, Grep]
---

# API 设计审查

你是一位 API 设计专家。请检查以下 RESTful API 设计规范：

## 审查要点

### 1. URL 设计
- 使用名词而非动词
- 使用复数形式
- 层级关系清晰
- 避免过深嵌套

### 2. HTTP 方法
- GET：获取资源
- POST：创建资源
- PUT：完整更新
- PATCH：部分更新
- DELETE：删除资源

### 3. 状态码
- 2xx：成功
- 3xx：重定向
- 4xx：客户端错误
- 5xx：服务端错误

### 4. 响应格式
```json
{
  "code": 0,
  "message": "success",
  "data": {}
}
```

## 输出格式

# API 设计审查报告

## 问题列表
| 端点 | 问题 | 建议 |
|------|------|------|
| GET /getUser | URL 使用动词 | 改为 GET /users |

## 改进建议
...
```

### 案例 3：Git 提交助手 Skill

```markdown
---
name: git-commit
description: Git 提交助手，生成规范的 commit message。当用户提到提交代码、commit、git commit 时自动触发。
allowed-tools: [Bash, Read]
argument-hint: "[message]"
---

# Git 提交助手

根据变更内容生成符合 Conventional Commits 规范的提交信息。

## Commit Message 格式

```
<type>(<scope>): <subject>

<body>

<footer>
```

## Type 类型

| 类型 | 说明 |
|------|------|
| feat | 新功能 |
| fix | 修复 bug |
| docs | 文档变更 |
| style | 代码格式 |
| refactor | 重构 |
| perf | 性能优化 |
| test | 测试相关 |
| chore | 构建/工具 |

## 示例

```
feat(auth): implement JWT-based authentication

- Add JWT token generation
- Implement token validation middleware
- Add refresh token support

Closes #123
```

## 执行步骤

1. 运行 `git diff --staged` 查看暂存变更
2. 分析变更类型和范围
3. 生成符合规范的 commit message
4. 执行 `git commit -m "message"`
```

---

## 六、高级特性

### 6.1 渐进式加载

Skill 采用三层加载系统：

| 层级 | 内容 | 加载时机 |
|------|------|----------|
| 1 | 元数据（name + description） | 始终在上下文中 |
| 2 | SKILL.md 正文 | 技能触发时 |
| 3 | 打包资源（scripts/references） | 按需加载 |

**最佳实践**：保持 SKILL.md 在 500 行以内，复杂内容放入 references/

### 6.2 脚本执行

在 `scripts/` 目录下放置可执行脚本：

```bash
# scripts/validate.sh
#!/bin/bash
echo "验证代码规范..."
npm run lint
npm run test
```

在 SKILL.md 中引用：

```markdown
## 验证步骤

执行验证脚本：
```bash
./scripts/validate.sh
```
```

### 6.3 参考文档

在 `references/` 目录下放置参考文档：

```
my-skill/
├── SKILL.md
└── references/
    ├── coding_standards.md
    └── best_practices.md
```

在 SKILL.md 中引用：

```markdown
## 参考文档

详细规范请参考：
- [编码规范](references/coding_standards.md)
- [最佳实践](references/best_practices.md)
```

### 6.4 模板输出

使用 `template.md` 定义输出格式：

```markdown
# template.md
# [项目名称] 分析报告

## 执行摘要
{summary}

## 关键发现
{findings}

## 建议
{recommendations}
```

---

## 七、调试与测试

### 7.1 查看技能加载

```bash
# 查看当前上下文
/context

# 查看 token 消耗
/cost
```

### 7.2 压缩上下文

```bash
# 压缩上下文，保留关键信息
/compact
```

### 7.3 测试技能

创建测试文件 `evals/evals.json`：

```json
{
  "skill_name": "code-review",
  "evals": [
    {
      "id": 1,
      "prompt": "审查 src/auth.js 文件",
      "expected_output": "输出代码审查报告",
      "files": ["src/auth.js"]
    }
  ]
}
```

---

## 八、最佳实践

### 8.1 SKILL.md 大小控制

```markdown
# ❌ 错误示范：200+ 行的 SKILL.md
# 会导致 AI 忽略关键信息

# ✅ 正确做法：控制在 200 行以内
# 复杂逻辑拆分为多个 Skill 或放入 references/
```

### 8.2 描述要"主动"

```yaml
# ❌ 欠触发
description: 代码审查工具

# ✅ 主动触发
description: 代码审查专家。当用户提到代码审查、代码质量、PR审查、代码检查、代码review时自动触发。
```

### 8.3 解释"为什么"

```markdown
# ❌ 硬性规则
ALWAYS 使用驼峰命名

# ✅ 解释原因
使用驼峰命名，因为这是 JavaScript 社区的约定，可以提高代码可读性和团队协作效率。
```

### 8.4 模块化设计

```
team-skills/
├── common/
│   ├── logging.md
│   └── error-handling.md
├── frontend/
│   └── react-review.md
└── backend/
    └── python-review.md
```

---

## 九、安装第三方 Skill

### 从 GitHub 安装

```bash
# 使用 clawhub 安装
clawhub install author/skill-name

# 或手动克隆
git clone https://github.com/author/skill-name.git ~/.claude/skills/skill-name
```

### 从本地安装

```bash
# 复制到技能目录
cp -r ./my-skill ~/.claude/skills/
```

---

## 十、常见问题

### Q1: Skill 没有触发？

检查 description 是否足够"主动"，包含触发关键词。

### Q2: 如何调试 Skill？

使用 `/context` 查看上下文，使用 `/compact` 压缩上下文。

### Q3: 如何共享给团队？

将 `.claude/skills/` 目录提交到 Git 仓库，团队成员 clone 后自动可用。

### Q4: Skill 和 Plugin 的区别？

- **Skill**：最小可复用单元，单个 Markdown 文件
- **Plugin**：完整功能包，包含多个 Skills 和配置
