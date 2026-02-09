---
name: seo-geo-orchestrator
description: Routes broad or ambiguous SEO/GEO requests to the correct skill(s) in this library and orchestrates multi-skill workflows end-to-end. Use for SEO/GEO strategy, audits, content creation, meta tags, schema/JSON-LD, technical SEO, internal linking, content refresh, rankings, backlinks, reporting, alerts, CORE-EEAT/EEAT content quality. 适用于 关键词研究/竞品分析/内容差距/写作/元标签/结构化数据/技术SEO/站内链接/内容更新/排名/外链/报告/告警/EEAT 等需要“先判断做什么”的请求。
---

# SEO & GEO Orchestrator

This skill is the “router + workflow conductor” for the entire `seo-geo-claude-skills` library. It selects the right underlying skill(s) (and optionally command files) based on user intent, then executes them in the right order while keeping outputs consistent.

## Operating Rules

1. Decide the **primary intent** (one main job) and up to **two secondary intents**.
2. Prefer a **single skill** when the request is narrow; orchestrate **multiple skills** only when the request is explicitly multi-part.
3. If the user provides a **URL** and asks for a **one-shot** deliverable, prefer a matching command in `commands/`. Otherwise use the matching skill(s).
4. After routing, load and follow the target skill(s) in this repository:
   - Skills live under: `research/`, `build/`, `optimize/`, `monitor/`, `cross-cutting/`
   - Commands live under: `commands/`

## Fast Intent Routing

Use this table to pick the best starting point.

| Intent (signals) | Use this | Location |
|---|---|---|
| Keyword discovery, clustering, intent, difficulty, topic map | `keyword-research` | `research/keyword-research/` |
| Competitor strategy, “what are they ranking for”, “steal their keywords”, competitor GEO citations | `competitor-analysis` | `research/competitor-analysis/` |
| “What ranks and why”, SERP features (PAA/snippets), AI Overview triggers, search intent patterns | `serp-analysis` | `research/serp-analysis/` |
| “What content am I missing vs competitors”, opportunity mining | `content-gap-analysis` | `research/content-gap-analysis/` |
| Write new SEO content (post/landing page/guide), outlines + on-page structure | `seo-content-writer` | `build/seo-content-writer/` |
| Make content citable/quotable by AI (ChatGPT/Perplexity/AI Overview), GEO score | `geo-content-optimizer` | `build/geo-content-optimizer/` |
| Title tag/meta description/OG/Twitter cards, CTR uplift | `meta-tags-optimizer` | `build/meta-tags-optimizer/` |
| Schema/structured data/JSON-LD (FAQ/HowTo/Product/Review/etc.) | `schema-markup-generator` | `build/schema-markup-generator/` |
| On-page audit (titles, meta, headers, content, images, links) | `on-page-seo-auditor` | `optimize/on-page-seo-auditor/` |
| Technical SEO (crawl/index, speed/CWV, robots/sitemaps, redirects, security) | `technical-seo-checker` | `optimize/technical-seo-checker/` |
| Internal linking, architecture, link equity flow, anchor text plan | `internal-linking-optimizer` | `optimize/internal-linking-optimizer/` |
| Refresh/update existing content to regain rankings; freshness + GEO/SEO best practices | `content-refresher` | `optimize/content-refresher/` |
| Track keyword rankings (SERP + AI answers), trends, deltas | `rank-tracker` | `monitor/rank-tracker/` |
| Backlink profile, toxic links, link opportunities, competitor link monitoring | `backlink-analyzer` | `monitor/backlink-analyzer/` |
| Stakeholder reports (SEO + GEO), executive summary + deep dive | `performance-reporter` | `monitor/performance-reporter/` |
| Alerts/monitoring thresholds (ranking drops, traffic changes, technical issues) | `alert-manager` | `monitor/alert-manager/` |
| CORE-EEAT 80-item audit, weighted scoring + action plan | `content-quality-auditor` | `cross-cutting/content-quality-auditor/` |
| Persist project context across sessions (hot cache + cold storage) | `memory-management` | `cross-cutting/memory-management/` |

### One-shot Command Routing (when URL + “just do it”)

| Request | Prefer command |
|---|---|
| Full page audit + CORE-EEAT scoring | `commands/audit-page.md` (`/seo:audit-page`) |
| Technical check for a URL | `commands/check-technical.md` (`/seo:check-technical`) |
| Generate schema markup | `commands/generate-schema.md` (`/seo:generate-schema`) |
| Optimize meta tags | `commands/optimize-meta.md` (`/seo:optimize-meta`) |
| Performance report | `commands/report.md` (`/seo:report`) |
| Set up alerts | `commands/setup-alert.md` (`/seo:setup-alert`) |

## Orchestration Patterns (Common Multi-Skill Flows)

Use these when the user request spans multiple jobs.

### New Content End-to-End

1. `keyword-research`
2. `serp-analysis` (for the chosen primary keyword)
3. `seo-content-writer`
4. `geo-content-optimizer`
5. `meta-tags-optimizer`
6. `schema-markup-generator`
7. `content-quality-auditor` (final gate)

### Optimize an Existing Page (SEO + GEO)

1. `on-page-seo-auditor` (baseline + prioritized fixes)
2. `geo-content-optimizer` (make key sections citeable)
3. `meta-tags-optimizer` (CTR)
4. `schema-markup-generator` (rich results + AI comprehension)
5. `technical-seo-checker` (crawl/index/speed blockers)
6. `internal-linking-optimizer` (distribution + crawl paths)

### Diagnose Ranking Drop

1. `rank-tracker` (time window + query set)
2. `technical-seo-checker` (indexing/crawl regressions)
3. `content-refresher` (freshness + intent drift)
4. `backlink-analyzer` (lost links / toxic links)
5. `alert-manager` (prevent recurrence)

## Execution Template (Output Contract)

Always start with a short routing header:

```markdown
### Routing Decision
**Primary intent**: …
**Selected skill(s)**: …
**Why**: …
**Inputs needed**: …
```

Then execute the selected skill(s) by following their `SKILL.md` instructions. Keep output cohesive:

- Reuse the same definitions (primary keyword, page type, target audience, intent) across steps.
- When multiple skills output overlapping artifacts (e.g., FAQ section + FAQ schema), de-duplicate and keep one canonical version.
- If a skill requires data the user didn’t provide, ask only for the minimum missing fields and proceed.

