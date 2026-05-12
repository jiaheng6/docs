import os

base = '/home/runner/work/docs/docs/src/content/docs/agent-platform'

# capabilities/index.mdx
cap_index = '''---
title: 功能
description: >-
  探索 Warp 的 Agent 功能，包括技能、规划、MCP、规则、Codebase Context、模型选择等。
---

Warp 内置多种功能，能在编码和工作流自动化中提升 Agent 的效果。以下页面介绍了如何配置和使用这些功能：

* [**Skills**](/agent-platform/capabilities/skills/) — 使用斜杠命令（`/skill-name`）从预先定义的指令启动 Agent 任务。
* [**Planning**](/agent-platform/capabilities/planning/) — 在 Warp 中，Agent 会先提出行动计划，经你批准后再执行。
* [**Rules**](/agent-platform/capabilities/rules/) — 通过工作区、项目或 Agent 层级的规则，为 Agent 设置持久性指令和约束。
* [**MCP Servers**](/agent-platform/capabilities/mcp/) — 通过标准化接口为本地 Agent 扩展自定义工具和数据源。
* [**Codebase Context**](/agent-platform/capabilities/codebase-context/) — Warp 对 Git 追踪的代码库进行索引，帮助 Agent 理解你的代码。
* [**Model choice**](/agent-platform/capabilities/model-choice/) — 为每次对话选择不同的 AI 模型。
* [**Web Search**](/agent-platform/capabilities/web-search/) — 允许 Agent 访问实时网络搜索结果。
* [**Computer Use**](/agent-platform/capabilities/computer-use/) — Agent 以编程方式与 GUI 应用程序和桌面交互。
* [**Full Terminal Use**](/agent-platform/capabilities/full-terminal-use/) — Agent 运行真实的终端命令，包括交互式进程。
* [**Task Lists**](/agent-platform/capabilities/task-lists/) — 通过可视化任务列表跟踪多步骤 Agent 操作。
* [**Slash Commands**](/agent-platform/capabilities/slash-commands/) — 查看所有可用斜杠命令的完整参考。
* [**Agent Notifications**](/agent-platform/capabilities/agent-notifications/) — 配置 Agent 完成、需要输入或出错时如何通知你。
* [**Agent Profiles & Permissions**](/agent-platform/capabilities/agent-profiles-permissions/) — 控制 Agent 可以使用哪些工具以及如何行动。
'''

# capabilities/agent-notifications.mdx
agent_notifs = '''---
title: Agent 通知
description: >-
  配置 Agent 完成任务或需要你关注时的通知方式。
sidebar:
  label: 通知
---

当 Agent 在后台运行时，通知可在 Agent 需要你关注时提醒你。你可以配置以下场景下的通知：

* **Agent 完成** — 任务完成（成功或失败）
* **需要输入** — Agent 停下来请求你的确认或输入
* **错误** — Agent 遇到问题

### 配置通知

在 Warp 中，进入 **Settings** > **Agents** > **Notifications** 配置通知行为。

可用选项包括：

* **System notifications** — 使用 macOS 原生通知，即使 Warp 不在前台也可接收
* **Sound** — 任务完成时播放提示音
* **Warp Drive** — 通过 Warp Drive 将通知分享给队友（仅限团队计划）

:::note
通知权限需在 macOS 系统设置中授予给 Warp。如未收到通知，请检查  > **System Settings** > **Notifications** > **Warp** 中的权限设置。
:::
'''

# capabilities/agent-profiles-permissions.mdx
agent_profiles = '''---
title: Agent Profiles 与权限
description: >-
  创建 Agent Profiles 来控制 Agent 使用的工具、权限和行为——限制危险操作，专注任务，或针对不同用途进行定制。
sidebar:
  label: Profiles 与权限
---

import { Tabs, TabItem } from \'@astrojs/starlight/components\';

Agent Profiles 允许你控制 Agent 能够使用哪些工具、其行为方式，以及对系统操作的访问程度。你可以创建多个 Profile，并根据任务类型或安全需求在它们之间切换。

:::note
Agent Profiles 适用于本地 Oz Agent。如需管理云端 Agent 的权限，请参阅[团队访问权限、计费与身份识别](/agent-platform/cloud-agents/team-access-billing-and-identity/)。
:::

## 什么是 Agent Profile

Agent Profile 是一组可配置的设置，决定了某个 Agent 会话可以使用哪些工具和权限。每个 Profile 可以：

* **启用或禁用特定工具** — 例如网络搜索、文件系统访问或 MCP 服务器
* **设置权限级别** — 控制 Agent 在无需询问的情况下可以执行哪些操作
* **提供自定义系统提示** — 针对特定工作流聚焦 Agent 行为
* **选择默认模型** — 为不同任务选用最合适的模型

## 创建 Agent Profile

1. 在 Warp 中进入 **Settings** > **Agents** > **Agent Profiles**。
2. 点击 **+ New Profile**。
3. 为 Profile 命名，并根据需要配置工具和权限。
4. 点击 **Save**。

## 使用 Agent Profile

创建 Profile 后，可以在 Agent 模式下从输入框切换 Profile。选中的 Profile 将应用于该对话中的所有 Agent 操作。

## 权限级别

每个 Agent Profile 支持为以下操作配置权限级别：

* **文件操作** — 读取、写入或删除文件
* **Shell 命令** — 运行终端命令
* **网络访问** — 发送网络请求
* **MCP 工具** — 调用 MCP 服务器工具

对于每类操作，可设置为：

* **Always ask** — 每次操作前均提示你确认
* **Auto-approve** — 无需提示自动执行
* **Blocked** — 完全禁止该类操作

:::caution
对于涉及文件修改或 Shell 命令的 Agent 任务，建议谨慎使用 Auto-approve，以避免意外更改。
:::
'''

for path, content in [
    ('capabilities/index.mdx', cap_index),
    ('capabilities/agent-notifications.mdx', agent_notifs),
    ('capabilities/agent-profiles-permissions.mdx', agent_profiles),
]:
    filepath = os.path.join(base, path)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f'Written: {path}')

print('Done batch 2')
