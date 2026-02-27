下面是对你提供的 Markdown 的**精准中文翻译**，并按你的要求做到：

- **保留原 Markdown 结构与格式**
- **代码块不翻译**（原样保留）
- **英文 + 中文对照**（逐段对应，便于校对与回溯）

---


---
name: skill-creator  
description: Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Codex's capabilities with specialized knowledge, workflows, or tool integrations.  
metadata:  
  short-description: Create or update a skill  
---

（中文对照）
---
name: skill-creator  
description: 创建高效技能的指南。当用户想要创建一个新 skill（或更新现有 skill），以通过专门知识、工作流或工具集成来扩展 Codex 能力时，应使用该 skill。  
metadata:  
  short-description: 创建或更新一个 skill  
---

# Skill Creator

（中文对照）
# Skill 创建器

This skill provides guidance for creating effective skills.

（中文对照）
本 skill 用于指导如何创建高效的 skills。

## About Skills

（中文对照）
## 关于 Skills

Skills are modular, self-contained folders that extend Codex's capabilities by providing  
specialized knowledge, workflows, and tools. Think of them as "onboarding guides" for specific  
domains or tasks—they transform Codex from a general-purpose agent into a specialized agent  
equipped with procedural knowledge that no model can fully possess.

（中文对照）
Skills 是模块化、自包含的文件夹，通过提供**专门知识、工作流与工具**来扩展 Codex 的能力。  
你可以把它们理解为面向特定领域或任务的“入门/上手指南”——它们能把 Codex 从通用型 agent 转变为具备特定流程知识的专业 agent，而这些流程性知识是任何模型都无法天然、完整具备的。

### What Skills Provide

（中文对照）
### Skills 提供什么

1. Specialized workflows - Multi-step procedures for specific domains  
2. Tool integrations - Instructions for working with specific file formats or APIs  
3. Domain expertise - Company-specific knowledge, schemas, business logic  
4. Bundled resources - Scripts, references, and assets for complex and repetitive tasks  

（中文对照）
1. 专门化工作流 —— 面向特定领域的多步骤流程  
2. 工具集成 —— 针对特定文件格式或 API 的使用说明  
3. 领域知识 —— 公司内部知识、数据 schema、业务逻辑等  
4. 捆绑资源 —— 用于复杂或重复任务的脚本、参考资料与资源文件

## Core Principles

（中文对照）
## 核心原则

### Concise is Key

（中文对照）
### 精炼是关键

The context window is a public good. Skills share the context window with everything else Codex needs: system prompt, conversation history, other Skills' metadata, and the actual user request.

（中文对照）
上下文窗口是一种“公共资源”。Skills 会与 Codex 需要的其它内容共享同一上下文窗口：系统提示词、对话历史、其他 Skills 的元数据，以及用户的实际请求。

**Default assumption: Codex is already very smart.** Only add context Codex doesn't already have. Challenge each piece of information: "Does Codex really need this explanation?" and "Does this paragraph justify its token cost?"

（中文对照）
**默认假设：Codex 已经非常聪明。** 只添加 Codex 原本不具备的上下文信息。对每一段信息都要自问：  
- “Codex 真的需要这段解释吗？”  
- “这段话的 token 成本是否值得？”

Prefer concise examples over verbose explanations.

（中文对照）
尽量用**简洁的示例**替代冗长的解释。

### Set Appropriate Degrees of Freedom

（中文对照）
### 设置合适的自由度

Match the level of specificity to the task's fragility and variability:

（中文对照）
让指令的具体程度与任务的**脆弱性**和**可变性**相匹配：

**High freedom (text-based instructions)**: Use when multiple approaches are valid, decisions depend on context, or heuristics guide the approach.

（中文对照）
**高自由度（文字说明型）**：适用于存在多种合理做法、决策依赖上下文、或主要靠启发式方法指导路线的场景。

**Medium freedom (pseudocode or scripts with parameters)**: Use when a preferred pattern exists, some variation is acceptable, or configuration affects behavior.

（中文对照）
**中等自由度（伪代码或带参数脚本）**：适用于有推荐模式、允许一定变体、或行为受配置影响的场景。

**Low freedom (specific scripts, few parameters)**: Use when operations are fragile and error-prone, consistency is critical, or a specific sequence must be followed.

（中文对照）
**低自由度（特定脚本、参数较少）**：适用于操作脆弱且容易出错、对一致性要求极高、或必须严格遵循固定步骤顺序的场景。

Think of Codex as exploring a path: a narrow bridge with cliffs needs specific guardrails (low freedom), while an open field allows many routes (high freedom).

（中文对照）
可以把 Codex 想象成在探索一条路：  
悬崖边的窄桥需要明确的护栏（低自由度）；开阔原野则允许多条路线（高自由度）。

### Anatomy of a Skill

（中文对照）
### Skill 的结构剖析

Every skill consists of a required SKILL.md file and optional bundled resources:

（中文对照）
每个 skill 由一个必需的 `SKILL.md` 文件以及可选的捆绑资源组成：

```  
skill-name/  
├── SKILL.md (required)  
│   ├── YAML frontmatter metadata (required)  
│   │   ├── name: (required)  
│   │   └── description: (required)  
│   └── Markdown instructions (required)  
├── agents/ (recommended)  
│   └── openai.yaml - UI metadata for skill lists and chips  
└── Bundled Resources (optional)  
    ├── scripts/          - Executable code (Python/Bash/etc.)  
    ├── references/       - Documentation intended to be loaded into context as needed  
    └── assets/           - Files used in output (templates, icons, fonts, etc.)  
```  

#### SKILL.md (required)

（中文对照）
#### SKILL.md（必需）

Every SKILL.md consists of:

（中文对照）
每个 `SKILL.md` 都由以下部分组成：

- **Frontmatter** (YAML): Contains `name` and `description` fields. These are the only fields that Codex reads to determine when the skill gets used, thus it is very important to be clear and comprehensive in describing what the skill is, and when it should be used.
- **Body** (Markdown): Instructions and guidance for using the skill. Only loaded AFTER the skill triggers (if at all).

（中文对照）
- **Frontmatter（YAML）**：包含 `name` 与 `description` 字段。Codex 只读取这两个字段来决定是否触发该 skill，因此必须清晰、全面地描述该 skill 是做什么的、在何时应使用。  
- **正文（Markdown）**：使用该 skill 的指令与指导。只有在 skill 被触发之后才会加载（如果触发了的话）。

#### Agents metadata (recommended)

（中文对照）
#### Agents 元数据（推荐）

- UI-facing metadata for skill lists and chips
- Read references/openai_yaml.md before generating values and follow its descriptions and constraints
- Create: human-facing `display_name`, `short_description`, and `default_prompt` by reading the skill
- Generate deterministically by passing the values as `--interface key=value` to `scripts/generate_openai_yaml.py` or `scripts/init_skill.py`
- On updates: validate `agents/openai.yaml` still matches SKILL.md; regenerate if stale
- Only include other optional interface fields (icons, brand color) if explicitly provided
- See references/openai_yaml.md for field definitions and examples

（中文对照）
- 面向 UI 的元数据，用于 skill 列表与快捷 chip 的展示  
- 在生成字段值前先阅读 `references/openai_yaml.md`，并遵循其中的说明与约束  
- 通过阅读 skill 内容来创建面向人的 `display_name`、`short_description`、`default_prompt`  
- 通过向 `scripts/generate_openai_yaml.py` 或 `scripts/init_skill.py` 传入 `--interface key=value`，以确定性的方式生成  
- 更新时：验证 `agents/openai.yaml` 是否仍与 `SKILL.md` 匹配；若过期则重新生成  
- 仅在用户明确提供时才加入其它可选的 interface 字段（例如图标、品牌色）  
- 字段定义与示例参见 `references/openai_yaml.md`

#### Bundled Resources (optional)

（中文对照）
#### 捆绑资源（可选）

##### Scripts (`scripts/`)

（中文对照）
##### 脚本（`scripts/`）

Executable code (Python/Bash/etc.) for tasks that require deterministic reliability or are repeatedly rewritten.

（中文对照）
用于需要**确定性可靠**或经常被反复编写的任务的可执行代码（Python/Bash 等）。

- **When to include**: When the same code is being rewritten repeatedly or deterministic reliability is needed
- **Example**: `scripts/rotate_pdf.py` for PDF rotation tasks
- **Benefits**: Token efficient, deterministic, may be executed without loading into context
- **Note**: Scripts may still need to be read by Codex for patching or environment-specific adjustments

（中文对照）
- **何时加入**：当同样的代码被重复重写，或需要确定性可靠时  
- **示例**：用于 PDF 旋转的 `scripts/rotate_pdf.py`  
- **收益**：更省 token、确定性更强，并且可能无需加载进上下文就能执行  
- **注意**：脚本仍可能需要被 Codex 阅读，以进行修补或适配环境差异

##### References (`references/`)

（中文对照）
##### 参考资料（`references/`）

Documentation and reference material intended to be loaded as needed into context to inform Codex's process and thinking.

（中文对照）
文档与参考资料，按需加载到上下文中，用于支撑 Codex 的执行过程与推理。

- **When to include**: For documentation that Codex should reference while working
- **Examples**: `references/finance.md` for financial schemas, `references/mnda.md` for company NDA template, `references/policies.md` for company policies, `references/api_docs.md` for API specifications
- **Use cases**: Database schemas, API documentation, domain knowledge, company policies, detailed workflow guides
- **Benefits**: Keeps SKILL.md lean, loaded only when Codex determines it's needed
- **Best practice**: If files are large (>10k words), include grep search patterns in SKILL.md
- **Avoid duplication**: Information should live in either SKILL.md or references files, not both. Prefer references files for detailed information unless it's truly core to the skill—this keeps SKILL.md lean while making information discoverable without hogging the context window. Keep only essential procedural instructions and workflow guidance in SKILL.md; move detailed reference material, schemas, and examples to references files.

（中文对照）
- **何时加入**：当 Codex 在工作时需要查阅相关文档  
- **示例**：财务 schema 的 `references/finance.md`、公司 NDA 模板的 `references/mnda.md`、公司政策的 `references/policies.md`、API 规范的 `references/api_docs.md`  
- **适用场景**：数据库 schema、API 文档、领域知识、公司政策、详细工作流指南  
- **收益**：保持 `SKILL.md` 精简；只有在 Codex 判断需要时才加载  
- **最佳实践**：如果文件较大（>1 万词），在 `SKILL.md` 中提供 grep 搜索模式  
- **避免重复**：信息应当只存在于 `SKILL.md` 或 references 文件之一，而不是两边都有。除非信息确实是 skill 的核心，否则详细内容优先放在 references 中——这样既能让 `SKILL.md` 保持精简，也能让信息可发现且不占用上下文窗口。`SKILL.md` 只保留必要的流程性指令与工作流指导；将详细参考资料、schema 与示例移到 references 文件中。

##### Assets (`assets/`)

（中文对照）
##### 资源文件（`assets/`）

Files not intended to be loaded into context, but rather used within the output Codex produces.

（中文对照）
不打算加载进上下文的文件，而是用于 Codex 产出结果时直接使用的文件。

- **When to include**: When the skill needs files that will be used in the final output
- **Examples**: `assets/logo.png` for brand assets, `assets/slides.pptx` for PowerPoint templates, `assets/frontend-template/` for HTML/React boilerplate, `assets/font.ttf` for typography
- **Use cases**: Templates, images, icons, boilerplate code, fonts, sample documents that get copied or modified
- **Benefits**: Separates output resources from documentation, enables Codex to use files without loading them into context

（中文对照）
- **何时加入**：当 skill 需要在最终输出中使用某些文件  
- **示例**：品牌素材 `assets/logo.png`、PPT 模板 `assets/slides.pptx`、HTML/React 脚手架 `assets/frontend-template/`、字体 `assets/font.ttf`  
- **适用场景**：模板、图片、图标、样板代码、字体、可复制或可修改的示例文档  
- **收益**：将输出资源与文档说明分离；让 Codex 使用这些文件时不必把它们加载进上下文

#### What to Not Include in a Skill

（中文对照）
#### Skill 中不应包含的内容

A skill should only contain essential files that directly support its functionality. Do NOT create extraneous documentation or auxiliary files, including:

（中文对照）
skill 只应包含直接支持其功能的必要文件。不要创建多余的文档或辅助文件，包括但不限于：

- README.md  
- INSTALLATION_GUIDE.md  
- QUICK_REFERENCE.md  
- CHANGELOG.md  
- etc.

（中文对照）
- README.md  
- INSTALLATION_GUIDE.md  
- QUICK_REFERENCE.md  
- CHANGELOG.md  
- 等等

The skill should only contain the information needed for an AI agent to do the job at hand. It should not contain auxiliary context about the process that went into creating it, setup and testing procedures, user-facing documentation, etc. Creating additional documentation files just adds clutter and confusion.

（中文对照）
skill 只应包含 AI agent 完成当前任务所需的信息。不应包含技能创建过程的旁枝背景、安装与测试步骤、面向用户的使用说明等。额外的文档只会带来杂乱与困惑。

### Progressive Disclosure Design Principle

（中文对照）
### 渐进式披露（Progressive Disclosure）设计原则

Skills use a three-level loading system to manage context efficiently:

（中文对照）
Skills 使用三级加载机制来更高效地管理上下文：

1. **Metadata (name + description)** - Always in context (~100 words)  
2. **SKILL.md body** - When skill triggers (<5k words)  
3. **Bundled resources** - As needed by Codex (Unlimited because scripts can be executed without reading into context window)  

（中文对照）
1. **元数据（name + description）**：始终在上下文中（约 100 词）  
2. **SKILL.md 正文**：skill 触发时加载（少于 5000 词）  
3. **捆绑资源**：Codex 按需加载（理论上不受限，因为脚本可在不读入上下文的情况下执行）

#### Progressive Disclosure Patterns

（中文对照）
#### 渐进式披露的常见模式

Keep SKILL.md body to the essentials and under 500 lines to minimize context bloat. Split content into separate files when approaching this limit. When splitting out content into other files, it is very important to reference them from SKILL.md and describe clearly when to read them, to ensure the reader of the skill knows they exist and when to use them.

（中文对照）
将 `SKILL.md` 正文保持为“必要内容”，并控制在 500 行以内，以减少上下文膨胀。接近这个限制时，把内容拆分到独立文件中。拆分后务必在 `SKILL.md` 中引用这些文件，并清晰说明何时需要阅读它们，确保 skill 的使用者知道它们的存在与使用时机。

**Key principle:** When a skill supports multiple variations, frameworks, or options, keep only the core workflow and selection guidance in SKILL.md. Move variant-specific details (patterns, examples, configuration) into separate reference files.

（中文对照）
**关键原则：** 当一个 skill 支持多种变体、框架或选项时，`SKILL.md` 只保留核心工作流与选择指导；把变体特定的细节（模式、示例、配置）移动到单独的参考文件中。

**Pattern 1: High-level guide with references**

（中文对照）
**模式 1：高层指南 + 引用参考文件**

```markdown
# PDF Processing

## Quick start

Extract text with pdfplumber:
[code example]

## Advanced features

- **Form filling**: See [FORMS.md](FORMS.md) for complete guide
- **API reference**: See [REFERENCE.md](REFERENCE.md) for all methods
- **Examples**: See [EXAMPLES.md](EXAMPLES.md) for common patterns
```

Codex loads FORMS.md, REFERENCE.md, or EXAMPLES.md only when needed.

（中文对照）
Codex 只会在需要时加载 `FORMS.md`、`REFERENCE.md` 或 `EXAMPLES.md`。

**Pattern 2: Domain-specific organization**

（中文对照）
**模式 2：按领域组织**

For Skills with multiple domains, organize content by domain to avoid loading irrelevant context:

（中文对照）
对于覆盖多个领域的 skills，应按领域组织内容，避免加载无关上下文：

```  
bigquery-skill/  
├── SKILL.md (overview and navigation)  
└── reference/  
    ├── finance.md (revenue, billing metrics)  
    ├── sales.md (opportunities, pipeline)  
    ├── product.md (API usage, features)  
    └── marketing.md (campaigns, attribution)  
```  

When a user asks about sales metrics, Codex only reads sales.md.

（中文对照）
当用户询问销售指标时，Codex 只读取 `sales.md`。

Similarly, for skills supporting multiple frameworks or variants, organize by variant:

（中文对照）
同样地，对于支持多个框架或变体的 skills，应按变体组织：

```  
cloud-deploy/  
├── SKILL.md (workflow + provider selection)  
└── references/  
    ├── aws.md (AWS deployment patterns)  
    ├── gcp.md (GCP deployment patterns)  
    └── azure.md (Azure deployment patterns)  
```  

When the user chooses AWS, Codex only reads aws.md.

（中文对照）
当用户选择 AWS 时，Codex 只读取 `aws.md`。

**Pattern 3: Conditional details**

（中文对照）
**模式 3：条件式细节披露**

Show basic content, link to advanced content:

（中文对照）
展示基础内容，并链接到高级内容：

```markdown
# DOCX Processing

## Creating documents

Use docx-js for new documents. See [DOCX-JS.md](DOCX-JS.md).

## Editing documents

For simple edits, modify the XML directly.

**For tracked changes**: See [REDLINING.md](REDLINING.md)
**For OOXML details**: See [OOXML.md](OOXML.md)
```

Codex reads REDLINING.md or OOXML.md only when the user needs those features.

（中文对照）
Codex 只会在用户需要这些功能时才读取 `REDLINING.md` 或 `OOXML.md`。

**Important guidelines:**

（中文对照）
**重要指南：**

- **Avoid deeply nested references** - Keep references one level deep from SKILL.md. All reference files should link directly from SKILL.md.
- **Structure longer reference files** - For files longer than 100 lines, include a table of contents at the top so Codex can see the full scope when previewing.

（中文对照）
- **避免深层嵌套引用**：references 与 `SKILL.md` 的引用层级保持“一层深”。所有参考文件都应从 `SKILL.md` 直接链接到。  
- **为长参考文件加结构**：超过 100 行的参考文件，应在顶部加入目录（TOC），便于 Codex 预览时快速掌握范围。

## Skill Creation Process

（中文对照）
## Skill 创建流程

Skill creation involves these steps:

（中文对照）
创建 skill 通常包含以下步骤：

1. Understand the skill with concrete examples  
2. Plan reusable skill contents (scripts, references, assets)  
3. Initialize the skill (run init_skill.py)  
4. Edit the skill (implement resources and write SKILL.md)  
5. Validate the skill (run quick_validate.py)  
6. Iterate based on real usage  

（中文对照）
1. 用具体示例理解该 skill 的使用方式  
2. 规划可复用的 skill 内容（脚本、参考资料、资源文件）  
3. 初始化 skill（运行 `init_skill.py`）  
4. 编辑 skill（实现资源并编写 `SKILL.md`）  
5. 验证 skill（运行 `quick_validate.py`）  
6. 基于真实使用进行迭代优化

Follow these steps in order, skipping only if there is a clear reason why they are not applicable.

（中文对照）
按顺序执行这些步骤；只有在明确不适用时才跳过。

### Skill Naming

（中文对照）
### Skill 命名

- Use lowercase letters, digits, and hyphens only; normalize user-provided titles to hyphen-case (e.g., "Plan Mode" -> `plan-mode`).
- When generating names, generate a name under 64 characters (letters, digits, hyphens).
- Prefer short, verb-led phrases that describe the action.
- Namespace by tool when it improves clarity or triggering (e.g., `gh-address-comments`, `linear-address-issue`).
- Name the skill folder exactly after the skill name.

（中文对照）
- 只使用小写字母、数字与连字符（`-`）；将用户提供的标题规范化为连字符风格（例如 “Plan Mode” -> `plan-mode`）。  
- 生成名称时，长度控制在 64 字符以内（仅字母、数字、连字符）。  
- 优先使用简短、以动词引导的短语来描述动作。  
- 当有助于清晰度或触发效果时，用工具作为命名空间前缀（例如 `gh-address-comments`、`linear-address-issue`）。  
- skill 文件夹名称必须与 skill 名称完全一致。

### Step 1: Understanding the Skill with Concrete Examples

（中文对照）
### 第 1 步：用具体示例理解 Skill

Skip this step only when the skill's usage patterns are already clearly understood. It remains valuable even when working with an existing skill.

（中文对照）
只有当 skill 的使用模式已被非常清楚地理解时，才可以跳过这一步。即使是在维护现有 skill 时，这一步依然很有价值。

To create an effective skill, clearly understand concrete examples of how the skill will be used. This understanding can come from either direct user examples or generated examples that are validated with user feedback.

（中文对照）
要创建高效 skill，首先要清晰理解它会如何被使用的具体示例。这种理解可以来自用户直接提供的例子，也可以来自你生成的例子并通过用户反馈进行验证。

For example, when building an image-editor skill, relevant questions include:

（中文对照）
例如，在构建 `image-editor` skill 时，可以问：

- "What functionality should the image-editor skill support? Editing, rotating, anything else?"
- "Can you give some examples of how this skill would be used?"
- "I can imagine users asking for things like 'Remove the red-eye from this image' or 'Rotate this image'. Are there other ways you imagine this skill being used?"
- "What would a user say that should trigger this skill?"

（中文对照）
- “image-editor skill 需要支持哪些功能？编辑、旋转、还有别的吗？”  
- “你能给一些这个 skill 会如何被使用的例子吗？”  
- “我能想到用户可能会说：‘去掉红眼’或‘旋转图片’。你还设想过哪些用法？”  
- “用户会说什么样的话，才应该触发这个 skill？”

To avoid overwhelming users, avoid asking too many questions in a single message. Start with the most important questions and follow up as needed for better effectiveness.

（中文对照）
为避免让用户负担过重，不要在一条消息里问太多问题。先从最重要的问题开始，再按需追问，以提高效果。

Conclude this step when there is a clear sense of the functionality the skill should support.

（中文对照）
当你已经明确该 skill 需要支持哪些功能时，即可结束本步骤。

### Step 2: Planning the Reusable Skill Contents

（中文对照）
### 第 2 步：规划可复用的 Skill 内容

To turn concrete examples into an effective skill, analyze each example by:

（中文对照）
要把具体示例转化为高效 skill，需要对每个示例做如下分析：

1. Considering how to execute on the example from scratch  
2. Identifying what scripts, references, and assets would be helpful when executing these workflows repeatedly  

（中文对照）
1. 思考如果从零开始，该示例应如何执行  
2. 识别在反复执行这些工作流时，哪些脚本、参考资料与资源文件会有帮助

Example: When building a `pdf-editor` skill to handle queries like "Help me rotate this PDF," the analysis shows:

（中文对照）
示例：构建 `pdf-editor` skill 来处理“帮我旋转这个 PDF”这类请求时，分析会发现：

1. Rotating a PDF requires re-writing the same code each time  
2. A `scripts/rotate_pdf.py` script would be helpful to store in the skill  

（中文对照）
1. 旋转 PDF 往往需要每次重复写同样的代码  
2. 把 `scripts/rotate_pdf.py` 脚本存进 skill 会很有用

Example: When designing a `frontend-webapp-builder` skill for queries like "Build me a todo app" or "Build me a dashboard to track my steps," the analysis shows:

（中文对照）
示例：设计 `frontend-webapp-builder` skill 以处理“做个 todo 应用”或“做个追踪步数的仪表盘”这类请求时，分析会发现：

1. Writing a frontend webapp requires the same boilerplate HTML/React each time  
2. An `assets/hello-world/` template containing the boilerplate HTML/React project files would be helpful to store in the skill  

（中文对照）
1. 编写前端 Web 应用通常需要反复使用同样的 HTML/React 样板代码  
2. 将包含样板工程文件的 `assets/hello-world/` 模板存入 skill 会很有帮助

Example: When building a `big-query` skill to handle queries like "How many users have logged in today?" the analysis shows:

（中文对照）
示例：构建 `big-query` skill 来处理“今天有多少用户登录？”这类请求时，分析会发现：

1. Querying BigQuery requires re-discovering the table schemas and relationships each time  
2. A `references/schema.md` file documenting the table schemas would be helpful to store in the skill  

（中文对照）
1. 查询 BigQuery 往往需要反复重新确认表结构及其关系  
2. 把记录表结构的 `references/schema.md` 放入 skill 会很有帮助

To establish the skill's contents, analyze each concrete example to create a list of the reusable resources to include: scripts, references, and assets.

（中文对照）
为确定 skill 的内容，应分析每个具体示例并产出要纳入 skill 的可复用资源清单：脚本、参考资料与资源文件。

### Step 3: Initializing the Skill

（中文对照）
### 第 3 步：初始化 Skill

At this point, it is time to actually create the skill.

（中文对照）
到这里，就该真正开始创建 skill 了。

Skip this step only if the skill being developed already exists. In this case, continue to the next step.

（中文对照）
只有在该 skill 已经存在时才可以跳过这一步；此时继续下一步。

When creating a new skill from scratch, always run the `init_skill.py` script. The script conveniently generates a new template skill directory that automatically includes everything a skill requires, making the skill creation process much more efficient and reliable.

（中文对照）
当从零创建新 skill 时，应始终运行 `init_skill.py`。该脚本会便捷地生成一个新的模板 skill 目录，自动包含 skill 所需的一切，从而让创建过程更高效、更可靠。

Usage:

（中文对照）
用法：

```bash
scripts/init_skill.py <skill-name> --path <output-directory> [--resources scripts,references,assets] [--examples]
```

Examples:

（中文对照）
示例：

```bash
scripts/init_skill.py my-skill --path skills/public
scripts/init_skill.py my-skill --path skills/public --resources scripts,references
scripts/init_skill.py my-skill --path skills/public --resources scripts --examples
```

The script:

（中文对照）
该脚本会：

- Creates the skill directory at the specified path  
- Generates a SKILL.md template with proper frontmatter and TODO placeholders  
- Creates `agents/openai.yaml` using agent-generated `display_name`, `short_description`, and `default_prompt` passed via `--interface key=value`  
- Optionally creates resource directories based on `--resources`  
- Optionally adds example files when `--examples` is set  

（中文对照）
- 在指定路径创建 skill 目录  
- 生成带有正确 frontmatter 与 TODO 占位的 `SKILL.md` 模板  
- 根据 `--interface key=value` 传入的、由 agent 生成的 `display_name`、`short_description`、`default_prompt` 创建 `agents/openai.yaml`  
- 根据 `--resources` 可选创建资源目录  
- 当设置 `--examples` 时可选添加示例文件

After initialization, customize the SKILL.md and add resources as needed. If you used `--examples`, replace or delete placeholder files.

（中文对照）
初始化后，按需定制 `SKILL.md` 并添加资源。如果使用了 `--examples`，请替换或删除占位文件。

Generate `display_name`, `short_description`, and `default_prompt` by reading the skill, then pass them as `--interface key=value` to `init_skill.py` or regenerate with:

（中文对照）
通过阅读 skill 来生成 `display_name`、`short_description` 与 `default_prompt`，然后以 `--interface key=value` 的形式传给 `init_skill.py`；或通过以下方式重新生成：

```bash
scripts/generate_openai_yaml.py <path/to/skill-folder> --interface key=value
```

Only include other optional interface fields when the user explicitly provides them. For full field descriptions and examples, see references/openai_yaml.md.

（中文对照）
只有在用户明确提供时才包含其它可选 interface 字段。完整字段说明与示例参见 `references/openai_yaml.md`。

### Step 4: Edit the Skill

（中文对照）
### 第 4 步：编辑 Skill

When editing the (newly-generated or existing) skill, remember that the skill is being created for another instance of Codex to use. Include information that would be beneficial and non-obvious to Codex. Consider what procedural knowledge, domain-specific details, or reusable assets would help another Codex instance execute these tasks more effectively.

（中文对照）
在编辑（新生成或现有的）skill 时，请记住：这个 skill 是给另一个 Codex 实例使用的。应包含对 Codex 有益且不显而易见的信息。思考哪些流程性知识、领域细节或可复用资源能帮助另一个 Codex 更高效地完成任务。

#### Start with Reusable Skill Contents

（中文对照）
#### 从可复用内容开始

To begin implementation, start with the reusable resources identified above: `scripts/`, `references/`, and `assets/` files. Note that this step may require user input. For example, when implementing a `brand-guidelines` skill, the user may need to provide brand assets or templates to store in `assets/`, or documentation to store in `references/`.

（中文对照）
开始实现时，先从上面识别出的可复用资源着手：`scripts/`、`references/` 与 `assets/` 文件。注意，这一步可能需要用户输入。例如实现 `brand-guidelines` skill 时，用户可能需要提供品牌资源或模板放入 `assets/`，或提供文档放入 `references/`。

Added scripts must be tested by actually running them to ensure there are no bugs and that the output matches what is expected. If there are many similar scripts, only a representative sample needs to be tested to ensure confidence that they all work while balancing time to completion.

（中文对照）
新增脚本必须通过实际运行来测试，确保无 bug 且输出符合预期。如果存在大量相似脚本，只需抽样测试有代表性的脚本即可，在完成时间与信心之间取得平衡。

If you used `--examples`, delete any placeholder files that are not needed for the skill. Only create resource directories that are actually required.

（中文对照）
如果使用了 `--examples`，请删除 skill 不需要的占位文件。只创建实际需要的资源目录。

#### Update SKILL.md

（中文对照）
#### 更新 SKILL.md

**Writing Guidelines:** Always use imperative/infinitive form.

（中文对照）
**写作规范：** 始终使用祈使/动词原形的表达方式（例如“执行… / 创建… / 验证…”）。

##### Frontmatter

（中文对照）
##### Frontmatter（页首元数据）

Write the YAML frontmatter with `name` and `description`:

（中文对照）
编写包含 `name` 与 `description` 的 YAML frontmatter：

- `name`: The skill name  
- `description`: This is the primary triggering mechanism for your skill, and helps Codex understand when to use the skill.  
  - Include both what the Skill does and specific triggers/contexts for when to use it.  
  - Include all "when to use" information here - Not in the body. The body is only loaded after triggering, so "When to Use This Skill" sections in the body are not helpful to Codex.  
  - Example description for a `docx` skill: "Comprehensive document creation, editing, and analysis with support for tracked changes, comments, formatting preservation, and text extraction. Use when Codex needs to work with professional documents (.docx files) for: (1) Creating new documents, (2) Modifying or editing content, (3) Working with tracked changes, (4) Adding comments, or any other document tasks"  

（中文对照）
- `name`：skill 名称  
- `description`：skill 的主要触发机制，用于帮助 Codex 判断何时使用该 skill。  
  - 既要包含 skill 做什么，也要包含何时使用的具体触发条件/上下文。  
  - 所有“何时使用”的信息都应写在这里——不要写在正文里。因为正文只有在触发后才加载，所以正文中的 “When to Use This Skill” 对 Codex 没帮助。  
  - `docx` skill 的描述示例：  
    “全面的文档创建、编辑与分析能力，支持修订模式（tracked changes）、批注（comments）、格式保留与文本提取。当 Codex 需要处理专业文档（.docx）时使用，包括：(1) 创建新文档，(2) 修改/编辑内容，(3) 处理修订模式，(4) 添加批注，或其它任何文档任务。”

Do not include any other fields in YAML frontmatter.

（中文对照）
不要在 YAML frontmatter 中包含任何其它字段。

##### Body

（中文对照）
##### 正文（Body）

Write instructions for using the skill and its bundled resources.

（中文对照）
编写该 skill 的使用指令，以及如何使用其捆绑资源。

### Step 5: Validate the Skill

（中文对照）
### 第 5 步：验证 Skill

Once development of the skill is complete, validate the skill folder to catch basic issues early:

（中文对照）
skill 开发完成后，验证 skill 文件夹以尽早发现基础问题：

```bash
scripts/quick_validate.py <path/to/skill-folder>
```

The validation script checks YAML frontmatter format, required fields, and naming rules. If validation fails, fix the reported issues and run the command again.

（中文对照）
验证脚本会检查 YAML frontmatter 格式、必填字段与命名规则。如果验证失败，修复报错指出的问题后再重新运行。

### Step 6: Iterate

（中文对照）
### 第 6 步：迭代优化

After testing the skill, users may request improvements. Often this happens right after using the skill, with fresh context of how the skill performed.

（中文对照）
在测试使用 skill 之后，用户可能会提出改进需求。通常这发生在刚用完 skill 之后，因为对效果的感受最为新鲜。

**Iteration workflow:**

（中文对照）
**迭代工作流：**

1. Use the skill on real tasks  
2. Notice struggles or inefficiencies  
3. Identify how SKILL.md or bundled resources should be updated  
4. Implement changes and test again  

（中文对照）
1. 在真实任务中使用该 skill  
2. 观察使用中的卡点或低效之处  
3. 明确应如何更新 `SKILL.md` 或捆绑资源  
4. 实施变更并再次测试  
