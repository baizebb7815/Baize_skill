# Rank Math SEO 使用指南

本文档帮助非技术站长正确使用 Rank Math 优化 WordPress 页面的 SEO。

---

## 核心理念

> **Rank Math 是 SEO 清单，不是裁判。**
> 
> 真正影响排名的是：
> - 语义结构（H1/H2/FAQ）
> - 意图匹配（内容解决用户问题）
> - 速度（Core Web Vitals）
> - 用户行为（点击率/停留时间/跳出率）

不要为了追求 100 分而牺牲用户体验。

---

## 1. Focus Keyword（焦点关键词）

### 1.1 选择策略

**规则：1-2 个关键词，优先主关键词**

| 页面类型 | Focus Keyword 示例 |
|---------|-------------------|
| 产品页 | `AI chatbot for customer service` |
| 博客文章 | `how to improve website speed` |
| 服务页 | `web design services` |
| 本地业务 | `plumber in San Francisco` |

### 1.2 如何找关键词

**工具：**
- Google Keyword Planner
- Ahrefs / SEMrush
- Google Search Console（已有流量数据）

**原则：**
- 搜索意图匹配：产品页用购买意图词（`buy`/`best`/`service`）
- 难度适中：新站避开竞争超高的词
- 长尾优先：`wordpress speed optimization tips` 优于 `seo`

### 1.3 填写位置

Rank Math 面板 → **Focus Keyword** 字段

**示例：**
```
Focus Keyword: AI customer service chatbot
Additional Keyword: automated customer support
```

---

## 2. Title Tag（标题标签）

### 2.1 公式

```
主关键词 + 吸引点击的修饰词 + 品牌名
```

**长度：50-60 字符（避免被截断）**

### 2.2 模板库

| 类型 | 模板 | 示例 |
|------|------|------|
| 产品页 | `[Keyword] - [Benefit] | Brand` | `AI Chatbot - 24/7 Customer Support | BASIS SIGN` |
| 博客文章 | `How to [Action] - [Year] Guide | Brand` | `How to Optimize WordPress Speed - 2025 Guide | BASIS SIGN` |
| 服务页 | `[Service] in [Location] - [USP] | Brand` | `Web Design in SF - Fast & Affordable | BASIS SIGN` |
| 首页 | `Brand - [Value Proposition]` | `BASIS SIGN - Professional WordPress Development` |

### 2.3 优化技巧

✅ **好的 Title：**
- `Best AI Chatbot for E-commerce - Free Trial | ChatBotPro`
  - 包含关键词 ✓
  - 吸引点击（Best/Free Trial）✓
  - 长度合适（54 字符）✓

❌ **差的 Title：**
- `Home - ChatBotPro` （没关键词、没吸引力）
- `The Ultimate Revolutionary AI-Powered Chatbot Solution for All Your Customer Service Needs` （太长，67+ 字符）

### 2.4 动态变量

Rank Math 支持变量：
- `%title%` - 页面标题
- `%sep%` - 分隔符（| 或 -）
- `%sitename%` - 网站名称
- `%currentyear%` - 当前年份

**示例：**
```
%title% %sep% %sitename%
```

---

## 3. Meta Description（元描述）

### 3.1 公式

```
问题 + 解决方案 + 行动号召（CTA）
```

**长度：150-160 字符**

### 3.2 模板库

| 类型 | 模板 |
|------|------|
| 产品页 | `Looking for [keyword]? Our [product] helps you [benefit]. [CTA].` |
| 博客文章 | `Learn how to [action] with our step-by-step guide. Includes [bonus]. Read now!` |
| 服务页 | `Get professional [service] in [location]. [USP]. Contact us for a free quote.` |

### 3.3 示例

**产品页：**
```
Looking for an AI chatbot for customer service? Our ChatBotPro helps you automate 80% of inquiries and boost satisfaction. Try free for 14 days!
```
（159 字符）

**博客文章：**
```
Learn how to optimize WordPress speed with our 2025 guide. Includes plugin recommendations and Core Web Vitals tips. Read now!
```
（148 字符）

### 3.4 注意事项

- **不要关键词堆砌**：自然语言 > 机械重复
- **包含 CTA**：`Try now` / `Learn more` / `Get started`
- **匹配搜索意图**：用户搜什么，描述就回答什么

---

## 4. H1/H2/H3 结构

### 4.1 黄金规则

**每页只能有 1 个 H1**

| 标签 | 用途 | 数量 |
|------|------|------|
| H1 | 页面主标题（与 Title 类似但可更详细） | 1 个 |
| H2 | 主要章节标题 | 2-5 个 |
| H3 | 子章节标题 | 按需 |

### 4.2 示例结构

**博客文章：**
```
H1: How to Optimize WordPress Speed in 2025

  H2: Why Website Speed Matters
  
  H2: Top 5 Speed Optimization Techniques
    H3: 1. Enable Caching
    H3: 2. Optimize Images
    H3: 3. Minify CSS/JS
    H3: 4. Use a CDN
    H3: 5. Choose Fast Hosting
  
  H2: Measuring Your Site Speed
  
  H2: FAQ
    H3: What is a good page load time?
    H3: Do plugins slow down WordPress?
```

**产品页：**
```
H1: AI Customer Service Chatbot - Automate Support 24/7

  H2: Key Features
  
  H2: How It Works
  
  H2: Pricing
  
  H2: Customer Testimonials
  
  H2: FAQ
```

### 4.3 Rank Math 检查点

Rank Math 会检查：
- ✅ Focus Keyword 出现在 H1
- ✅ Focus Keyword 出现在至少 1 个 H2
- ❌ 多个 H1（扣分）

**修复多 H1 问题：**
如果 Rank Math 提示"Found 2 H1 tags"，检查：
- Logo 是否被错误包裹在 `<h1>` 中
- 页面标题是否重复使用 H1
- 使用浏览器开发者工具搜索 `<h1>` 定位问题

---

## 5. 内部链接（Internal Links）

### 5.1 为什么重要

- 帮助 Google 理解网站结构
- 分散页面权重
- 降低跳出率
- 引导转化路径

### 5.2 链接策略

**至少 2-3 条内链，遵循以下结构：**

```
博客文章 → 相关博客文章
博客文章 → 产品/服务页
产品/服务页 → 联系/询盘页
```

### 5.3 示例

**博客文章：** "How to Optimize WordPress Speed"

内链建议：
1. → 相关文章：`Best WordPress Caching Plugins in 2025`
2. → 服务页：`Our WordPress Speed Optimization Service`
3. → 转化页：`Get a Free Speed Audit`

### 5.4 锚文本规则

✅ **好的锚文本：**
- `learn more about WordPress caching plugins` （描述性）
- `our speed optimization service` （相关性）

❌ **差的锚文本：**
- `click here` （无语义）
- `this link` （无描述）
- `AI chatbot AI chatbot AI chatbot` （关键词堆砌）

---

## 6. 可忽略的 Rank Math 提示

### 6.1 不必追求的 100 分

某些建议对排名影响极小，可以忽略：

| 提示 | 是否必须 | 说明 |
|------|---------|------|
| "关键词未出现在 URL" | ❌ | URL 简洁即可，不必强行塞词 |
| "关键词密度不足" | ❌ | 自然写作 > 机械重复关键词 |
| "图片缺少关键词" | ⚠️ | alt 描述真实内容即可，不必堆砌 |
| "段落太长" | ⚠️ | 可读性优先，不必强行拆段 |
| "关键词未出现在前 10% 内容" | ⚠️ | 自然融入即可，不必刻意提前 |

### 6.2 真正重要的指标

关注这些：
- ✅ H1 只有 1 个
- ✅ Title 和 Meta Description 已填写
- ✅ Focus Keyword 在 Title/H1/H2 中
- ✅ 至少 2-3 条内链
- ✅ 图片有 alt 属性
- ✅ 内容长度 >300 字（根据页面类型调整）

---

## 7. 不同页面类型的 SEO 模板

### 7.1 首页

**Focus Keyword：** `品牌名 + 核心业务`

**Title：**
```
BASIS SIGN - Professional WordPress Development & Design
```

**Meta Description：**
```
BASIS SIGN offers custom WordPress development, speed optimization, and design services. Trusted by 500+ clients. Get a free consultation today!
```

**H1：**
```
Professional WordPress Development That Grows Your Business
```

---

### 7.2 产品/服务页

**Focus Keyword：** `具体产品/服务名`

**Title：**
```
AI Customer Service Chatbot - Automate 80% of Inquiries | ChatBotPro
```

**Meta Description：**
```
Automate customer support with our AI chatbot. Reduce response time by 90%, boost satisfaction, and save costs. Try free for 14 days!
```

**H1：**
```
AI Customer Service Chatbot - 24/7 Automated Support
```

**结构：**
```
H1: 产品名 + 核心卖点
H2: Key Features
H2: How It Works
H2: Pricing
H2: Customer Reviews
H2: FAQ
```

---

### 7.3 博客文章

**Focus Keyword：** `具体问题/主题`

**Title：**
```
How to Optimize WordPress Speed - 10 Proven Tips (2025 Guide)
```

**Meta Description：**
```
Learn how to make your WordPress site load faster with our expert guide. Includes caching, CDN, image optimization, and more. Read now!
```

**H1：**
```
How to Optimize WordPress Speed in 2025
```

**结构：**
```
H1: 主题
H2: 为什么重要
H2: 解决方案（分步骤）
  H3: 步骤 1
  H3: 步骤 2
  ...
H2: 常见错误
H2: FAQ
```

---

### 7.4 本地业务页

**Focus Keyword：** `服务 + 地区`

**Title：**
```
Plumber in San Francisco - 24/7 Emergency Service | QuickFix
```

**Meta Description：**
```
Need a plumber in San Francisco? QuickFix offers 24/7 emergency plumbing services. Licensed, insured, and 5-star rated. Call now!
```

**H1：**
```
Trusted Plumber in San Francisco - Same-Day Service
```

**结构：**
```
H1: 服务 + 地区 + USP
H2: Our Services
H2: Service Areas
H2: Why Choose Us
H2: Customer Reviews
H2: Contact Us
```

---

## 8. Rank Math 填写清单

每次发布页面前，检查：

- [ ] **Focus Keyword** 已设置（1-2 个）
- [ ] **Title Tag** 长度 50-60 字符，包含关键词
- [ ] **Meta Description** 长度 150-160 字符，包含 CTA
- [ ] **H1** 只有 1 个，包含关键词
- [ ] **H2** 至少 2 个，1 个包含关键词
- [ ] **内链** 至少 2-3 条
- [ ] **图片 alt** 已填写（描述真实内容）
- [ ] **URL** 简洁易读（可选：包含关键词）

---

## 9. 常见问题解答

### Q1: Rank Math 分数只有 60 分，怎么办？

**A:** 不必担心。检查上面清单的必选项是否完成。如果都完成了，60-80 分已经足够好。过度优化（如关键词堆砌）反而有害。

---

### Q2: 多个页面用同一个 Focus Keyword 会被惩罚吗？

**A:** 不会直接惩罚，但会导致"关键词蚕食"（Keyword Cannibalization）—— Google 不知道推哪个页面。

**解决方案：**
- 主关键词只给 1 个最重要的页面
- 其他页面用长尾变体（如 `wordpress speed` vs `wordpress speed optimization tips`）

---

### Q3: 需要每个段落都加关键词吗？

**A:** 不需要。Rank Math 提示"关键词密度"是过时的 SEO 思维。现代 Google 看的是语义和意图，不是机械重复。

**正确做法：**
- Title/H1/第一段包含关键词
- 其余自然写作，用同义词和相关词

---

### Q4: 图片 alt 必须包含关键词吗？

**A:** 不必须。alt 的作用是：
1. 无障碍访问（屏幕阅读器）
2. 图片无法加载时显示

**最佳实践：**
- 描述图片真实内容
- 如果图片确实和关键词相关，可以自然包含
- ❌ 不要：`alt="wordpress speed wordpress speed wordpress"`
- ✅ 可以：`alt="Screenshot of WordPress caching plugin settings"`

---

### Q5: URL 需要包含关键词吗？

**A:** 非必需，但有帮助。

**优先级：**
1. 简洁易读 > 堆砌关键词
2. ✅ `example.com/ai-chatbot` （好）
3. ❌ `example.com/best-ai-chatbot-for-customer-service-automation-2025` （过长）

---

## 10. 快速参考卡

### Title Tag 公式
```
[Keyword] + [Modifier] + | + [Brand]
长度：50-60 字符
```

### Meta Description 公式
```
[Problem] + [Solution] + [CTA]
长度：150-160 字符
```

### H1/H2 规则
```
H1: 1 个，包含主关键词
H2: 2-5 个，至少 1 个包含关键词
```

### 内链策略
```
博客 → 博客
博客 → 产品
产品 → 转化页
```

### 必做清单
```
✓ Focus Keyword
✓ Title (50-60 字符)
✓ Meta (150-160 字符)
✓ 单个 H1
✓ 2-3 条内链
✓ 图片 alt
```
