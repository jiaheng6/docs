import os

base = '/home/runner/work/docs/docs/src/content/docs/agent-platform'

files = {
    'index.mdx': '''---
title: Agents 概述
description: >-
  Oz 是云端 Agent 的编排平台，为开发工作流提供交互式和自主 Agent 支持。
---

Warp 内置了 **Oz**，即云端 Agent 的编排平台。Warp 提供你日常工作所用的终端和编码界面，而 Oz 则是使大规模运行 Agent 成为可能的底层编排层。

Warp 的客户端在 [AGPL v3](https://github.com/warpdotdev/warp/blob/master/LICENSE-AGPL) 许可下开源，因此托管你的 Agent 的编辑器和终端完全可审计。有关源码和贡献流程，请参阅 [Contributing to Warp](/support-and-community/community/contributing/)。

使用 Oz，你可以：

* 在 Warp 中运行交互式 Agent 对话，获得实时编码辅助
* 部署可从触发器、定时任务或集成中在云端运行的自主 Agent
* 跨机器、代码库和团队同时协调多个 Agent
* 对 Agent 活动进行完整的跟踪、审计和共享，全面了解运行情况及其所做操作

Oz 完全可编程——手动启动 Agent，或利用触发器、定时任务、环境和自选托管（Warp 云或自有基础设施）围绕 Agent 构建自定义逻辑。

---

## 核心功能

* [**Local Agents**](/agent-platform/local-agents/overview/) - 嵌入 Warp 的交互式 Oz Agent。使用自然语言编写代码、调试问题、运行命令，并通过完整的终端访问自动化开发任务。
* [**第三方 CLI Agent**](/agent-platform/cli-agents/overview/) - 在 Warp 中使用 Claude Code、Codex、OpenCode 及其他 CLI 编码 Agent，享有丰富输入、通知、代码审查和远程会话控制功能。
* [**Oz 云端 Agent**](/agent-platform/cloud-agents/overview/) - 响应系统事件、定时任务或集成在后台自主运行的 Oz Agent。
* [**集成**](/agent-platform/cloud-agents/integrations/) - 将外部系统事件连接到自主 Agent 执行。使用 [Slack](/agent-platform/cloud-agents/integrations/slack/)、[Linear](/agent-platform/cloud-agents/integrations/linear/)、[GitHub Actions](/agent-platform/cloud-agents/integrations/github-actions/) 及其他集成在云端触发 Agent。
* [**Oz 平台**](/agent-platform/cloud-agents/platform/) - 支撑 Oz 的底层基础设施，包括 CLI、API/SDK、编排层、环境、密钥以及管理与可观测性。

---

## 快速开始

* [**Warp 中的 Agent**](/agent-platform/getting-started/agents-in-warp/) - 在 Warp 中交互式使用 Oz Agent
* [**Oz Web App**](https://oz.warp.dev) - 创建运行、管理定时任务、浏览技能并配置集成
* [**Oz CLI**](/reference/cli/) - 从命令行、CI 或远程机器运行 Agent
* [**Oz API & SDK**](/reference/api-and-sdk/) - 以编程方式创建和监控 Agent 运行

---

## 了解更多

* [Warp Agents 概述](/agent-platform/local-agents/overview/) - Warp 中的交互式 Agent
* [第三方 CLI Agent](/agent-platform/cli-agents/overview/) - Claude Code、Codex、OpenCode 等
* [云端 Agent 概述](/agent-platform/cloud-agents/overview/) - 大规模自动化的后台 Agent
* [Agent 功能](/agent-platform/capabilities/) - 技能、规划、MCP、规则等
* [Oz 平台](/agent-platform/cloud-agents/platform/) - CLI、API/SDK、编排、环境和主机
* [环境](/agent-platform/cloud-agents/environments/) - 为云端 Agent 配置执行上下文
* [集成](/agent-platform/cloud-agents/integrations/) - Slack、Linear、GitHub Actions 及自定义集成
* [Skills as Agents](/agent-platform/cloud-agents/skills-as-agents/) - 从可复用的技能定义运行 Agent
* [管理云端 Agent](/agent-platform/cloud-agents/managing-cloud-agents/) - 监控和管理 Agent 活动
''',
}

for filename, content in files.items():
    filepath = os.path.join(base, filename)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f'Written: {filepath}')

print('Done batch 1')
