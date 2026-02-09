# GreenShift 区块生成核心规则

本文档包含生成 GreenShift/GreenLight Gutenberg 区块的完整技术规范。

---

## 1. 区块结构基础

### 1.1 Gutenberg 注释语法

所有 GreenShift 区块必须遵循 Gutenberg 注释式结构：

```html
<!-- wp:greenshift-blocks/element {JSON属性} -->
<tag class="...">内容</tag>
<!-- /wp:greenshift-blocks/element -->
```

本 Skill 的输出必须是 **可直接粘贴到 Gutenberg 编辑器** 的注释式块标记（不是前端渲染后的 HTML）。

**关键点：**
- 开始注释：`<!-- wp:greenshift-blocks/element`
- JSON 属性：必须是有效的 JSON 对象
- HTML 标签：与 JSON 中的 `tag` 字段对应
- 结束注释：`<!-- /wp:greenshift-blocks/element -->`

### 1.2 兼容性策略（两档）

为兼顾“可导入成功率”和“复刻完整度”，分两档选择区块集合：

**Safe（兼容优先）**
* 只生成 `greenshift-blocks/element`
* 适合：常规模块、无复杂交互、无参考源码时的快速落地

**Full（完整复刻）**
* 允许使用你站可导入验证过的 GreenShift 区块名（以参考代码为准）
* 当前仓库已出现并可作为参考的区块名包含：
  * `greenshift-blocks/container`
  * `greenshift-blocks/row`
  * `greenshift-blocks/row-column`
  * `greenshift-blocks/heading`
  * `greenshift-blocks/text`
  * `greenshift-blocks/button`
  * `greenshift-blocks/swiper`

选择规则：
* 用户明确要求“尽可能复刻/包含交互”，使用 Full
* 用户提供的参考源码里出现了非 `element` 的 GreenShift 区块，使用 Full
* 其他情况默认 Safe

---

## 2. 命名与 ID 规范

### 2.1 区块 ID

**规则：**
- 格式：`gsbp-` + 7位随机字符（字母+数字）
- 示例：`gsbp-a3f9k2m`、`gsbp-7x4b9c1`
- **`id` 和 `localId` 必须相同**

**生成方法：**
使用 `scripts/generate_block_id.py`：
```bash
python scripts/generate_block_id.py
# 输出：gsbp-x7k3m9a
```

或在 JSON 中手动生成：
```json
{
  "id": "gsbp-a3f9k2m",
  "localId": "gsbp-a3f9k2m"
}
```

### 2.2 HTML Class 规范

当区块有 `styleAttributes` 时，HTML class 必须包含 `localId`：

```html
<!-- wp:greenshift-blocks/element {"id":"gsbp-abc123","localId":"gsbp-abc123","styleAttributes":{...}} -->
<div class="gsbp-abc123">内容</div>
<!-- /wp:greenshift-blocks/element -->
```

---

## 3. Tag 标签规范

### 3.1 语义化标签选择

根据内容语义选择正确的 HTML 标签：

| 内容类型 | 推荐标签 |
|---------|---------|
| 容器 | `div`, `section`, `article` |
| 标题 | `h1`, `h2`, `h3`, `h4`, `h5`, `h6` |
| 段落 | `p` |
| 链接 | `a` |
| 按钮 | `button`, `a` |
| 图片 | `img` |
| 视频 | `video` |
| 图标 | `svg`, `span` |

### 3.2 默认标签

未明确指定时，默认 `tag: "div"`

---

## 4. Type 字段规范

### 4.1 Type 类型定义

| type 值 | 用途 | 必需字段 |
|---------|------|----------|
| `inner` | 容器，可嵌套子区块 | `innerBlocks` 或子区块标记 |
| `text` | 文本内容 | `textContent` |
| `no` | 纯视觉占位（无内容） | 无 |
| `image` | 图片 | `tag:"img"` + `src` + `alt`（建议 `loading:"lazy"`） |

> 说明：示例里偶尔会出现 `type:"html"` 或 `type:"empty"`，但本 Skill 默认优先使用 `text/inner/no/image` 四类。

### 4.2 使用规则

**文本块：**
```json
{
  "type": "text",
  "tag": "p",
  "textContent": "这是一段文本"
}
```

**容器块：**
```json
{
  "type": "inner",
  "tag": "div"
}
```
对应 HTML：
```html
<div>
  <!-- 子区块 -->
</div>
```

**混排文本：**
如需在文本中混入不同样式，使用独立 `span` 子块：
```html
<!-- wp:greenshift-blocks/element {"type":"inner","tag":"p"} -->
<p>
  <!-- wp:greenshift-blocks/element {"type":"text","tag":"span","textContent":"粗体文字","styleAttributes":{"fontWeight":700}} -->
  <span>粗体文字</span>
  <!-- /wp:greenshift-blocks/element -->
  普通文字
</p>
<!-- /wp:greenshift-blocks/element -->
```

---

## 5. 样式规范（StyleAttributes）

### 5.1 基本规则

**禁止使用 inline style：**
❌ 错误：
```html
<div style="color: red;">内容</div>
```

✅ 正确：
```json
{
  "styleAttributes": {
    "color": "red"
  }
}
```

**额外约束：**
- 不要用 `dynamicAttributes` 写 `style`（示例里存在这种“偷懒写法”，但规范上不推荐）
- 需要 hover/响应式时，一律用 `styleAttributes`

### 5.2 属性命名（camelCase）

所有 CSS 属性必须使用 camelCase：

| CSS 属性 | JSON 属性 |
|----------|----------|
| `background-color` | `backgroundColor` |
| `font-size` | `fontSize` |
| `margin-top` | `marginTop` |
| `border-radius` | `borderRadius` |
| `flex-direction` | `flexDirection` |

### 5.3 响应式数组

响应式属性使用固定顺序的数组：
```
[desktop, tablet, mobile, mobile_small]
```

**示例：**
```json
{
  "styleAttributes": {
    "fontSize": ["18px", "16px", "14px", "14px"]
  }
}
```

**继承规则：**
- 不足 4 项时，向下继承
- `["18px", "16px"]` = `["18px", "16px", "16px", "16px"]`
- 可省略后续相同值

### 5.4 伪状态（Hover/Focus）

使用 `_hover` 或 `_focus` 后缀：

```json
{
  "styleAttributes": {
    "backgroundColor": "#000",
    "backgroundColor_hover": "#333",
    "color_focus": "#fff"
  }
}
```

**前提：** HTML class 必须包含 `localId`

---

## 6. 布局模式

### 6.1 Section 外层容器

**推荐标准结构（严格对齐 GreenShift 生态）：**
```html
<!-- wp:greenshift-blocks/element {
  "id":"gsbp-xxxxxxx",
  "localId":"gsbp-xxxxxxx",
  "tag":"section",
  "type":"inner",
  "align":"full",
  "dynamicAttributes":[{"name":"data-type","value":"section-component"}],
  "isVariation":"contentcolumns",
  "styleAttributes":{
    "display":["flex"],
    "justifyContent":["center"],
    "flexDirection":["column"],
    "alignItems":["center"]
  }
} -->
<section class="gsbp-xxxxxxx alignfull" data-type="section-component">
  <!-- wp:greenshift-blocks/element {
    "id":"gsbp-yyyyyyy",
    "localId":"gsbp-yyyyyyy",
    "type":"inner",
    "dynamicAttributes":[{"name":"data-type","value":"content-area-component"}],
    "isVariation":"contentarea",
    "styleAttributes":{
      "maxWidth":["100%"],
      "width":["var(--wp--style--global--wide-size, 1200px)"],
      "display":["flex"],
      "flexDirection":["row"],
      "flexWrap":["wrap"],
      "columnGap":["25px"],
      "rowGap":["25px"]
    }
  } -->
  <div class="gsbp-yyyyyyy" data-type="content-area-component">
    <!-- 实际内容 -->
  </div>
  <!-- /wp:greenshift-blocks/element -->
</section>
<!-- /wp:greenshift-blocks/element -->
```

**关键点：**
- 外层 `data-type` 必须通过 `dynamicAttributes` 输出（不要写进 `attributes`）
- Content Area 宽度建议使用：`width:["var(--wp--style--global--wide-size, 1200px)"]`
- 如果需要列布局比例，使用 `flexColumns_Extra` + `flexWidths_Extra`（见你提供的参考代码）

### 6.2 Columns 栅格布局

使用 `flexColumns_Extra` + `flexWidths_Extra`（在 `styleAttributes` 中）控制列比例与断点：

```json
{
  "styleAttributes": {
    "display": ["flex"],
    "flexColumns_Extra": 2,
    "flexWidths_Extra": {
      "desktop": {"name": "50/50", "widths": [50, 50]},
      "tablet": {"name": "100/100", "widths": [100, 100]},
      "mobile": {"name": "100/100", "widths": [100, 100]}
    },
    "flexWrap": ["wrap"]
  }
}
```

> 注意：这不是 `row/column` 生态，而是 **Element + Variation** 的 GS 输出习惯。

---

## 7. 链接与媒体（必须遵循）

### 7.1 链接 href

`<a>` 的链接必须写在 block JSON 顶层：

```html
<!-- wp:greenshift-blocks/element {"id":"gsbp-xxxxxxx","localId":"gsbp-xxxxxxx","tag":"a","type":"inner","href":"/request-a-quote/"} -->
<a class="gsbp-xxxxxxx" href="/request-a-quote/">Request a Quote</a>
<!-- /wp:greenshift-blocks/element -->
```

### 7.2 图片

```html
<!-- wp:greenshift-blocks/element {"id":"gsbp-xxxxxxx","localId":"gsbp-xxxxxxx","tag":"img","type":"image","src":"https://.../image.webp","alt":"Descriptive alt"} -->
<img class="gsbp-xxxxxxx" src="https://.../image.webp" alt="Descriptive alt" loading="lazy"/>
<!-- /wp:greenshift-blocks/element -->
```

---

## 8. 你站实际用法补充（来自 `参考代码.md`）

### 8.1 `interactionLayers`（生成 data-gspbactions）

你站导出的 block 里会在 JSON 中出现 `interactionLayers`，前端渲染时会输出 `data-gspbactions="..."`。

* 仅在用户明确需要交互（Lightbox / 打开面板 / 滚动定位等）时才生成。
* 默认不生成交互，避免引入不可控行为。

### 8.2 `stylemanager` + `dynamicGClasses`（集中样式管理）

你站导出的 block 里存在 `isVariation:"stylemanager"`，并通过 `dynamicGClasses` 承载大量 CSS（含媒体查询），以及 `customCSS_Extra`。

* 优先用 `styleAttributes` 写样式。
* 只有在样式量非常大、或必须集中管理 class 级 CSS 时，才使用 `dynamicGClasses`。
* `customJs/customJsEnabled` 只有在用户明确要求时才生成（默认禁止）。
{
  "variation": "contentcolumns/contentarea",
  "flexColumns_Extra": ["3", "2", "1", "1"],
  "flexWidths_Extra": [
    ["33.33%", "33.33%", "33.33%"],
    ["50%", "50%"],
    ["100%"],
    ["100%"]
  ]
}
```

**说明：**
- `flexColumns_Extra`：每个断点的列数 `[桌面, 平板, 横屏手机, 竖屏手机]`
- `flexWidths_Extra`：每个断点各列的宽度百分比

### 6.3 Slider 轮播

使用 `greenshift-blocks/swiper`：

```html
<!-- wp:greenshift-blocks/swiper {"slidesPerView":1,"autoplay":true} -->
<div class="swiper">
  <!-- wp:greenshift-blocks/element {"type":"inner"} -->
  <div>第一张 slide</div>
  <!-- /wp:greenshift-blocks/element -->
  
  <!-- wp:greenshift-blocks/element {"type":"inner"} -->
  <div>第二张 slide</div>
  <!-- /wp:greenshift-blocks/element -->
</div>
<!-- /wp:greenshift-blocks/swiper -->
```

---

## 7. 动态内容

### 7.1 动态属性

使用 `dynamicAttributes` 数组：

```json
{
  "dynamicAttributes": [
    {
      "name": "textContent",
      "value": "{{POST_TITLE}}"
    },
    {
      "name": "href",
      "value": "{{SITE_URL}}/contact"
    }
  ]
}
```

### 7.2 常用占位符

| 占位符 | 说明 |
|--------|------|
| `{{POST_TITLE}}` | 文章标题 |
| `{{POST_EXCERPT}}` | 文章摘要 |
| `{{SITE_URL}}` | 网站 URL |
| `{{SITE_NAME}}` | 网站名称 |
| `{{GET:param_name}}` | URL 参数 |
| `{{FEATURED_IMAGE}}` | 特色图片 URL |

### 7.3 动态文本/链接

简化写法：
```json
{
  "dynamictext": "{{POST_TITLE}}",
  "dynamiclink": "{{SITE_URL}}/about"
}
```

---

## 8. 站点变量

### 8.1 WordPress 全局变量

优先使用站点级 CSS 变量：

**宽度：**
- `var(--wp--style--global--wide-size, 1200px)` - 最大内容宽度
- `var(--wp--style--global--content-size, 800px)` - 正文宽度

**颜色：**
- `var(--wp--preset--color--primary)` - 主色
- `var(--wp--preset--color--secondary)` - 辅色
- `var(--wp--preset--color--background)` - 背景色

**字体：**
- `var(--wp--preset--font-family--primary)` - 主字体
- `var(--wp--preset--font-size--large)` - 大号字体

### 8.2 自定义变量

使用 `var(--wp--custom--...)` 命名空间：
```json
{
  "styleAttributes": {
    "color": "var(--wp--custom--brand-primary, #000)"
  }
}
```

---

## 9. 动画规范

### 9.1 Keyframes 动画

使用 `animation_keyframes_Extra` + `animation`：

```json
{
  "animation_keyframes_Extra": {
    "0%": {"opacity": 0, "transform": "translateY(20px)"},
    "100%": {"opacity": 1, "transform": "translateY(0)"}
  },
  "animation": "fadeInUp 0.6s ease-out forwards"
}
```

### 9.2 滚动动画

使用 `animationTimeline` + `animationRange`：

```json
{
  "animation_keyframes_Extra": {
    "0%": {"opacity": 0},
    "100%": {"opacity": 1}
  },
  "animation": "fadeIn linear forwards",
  "animationTimeline": ["view()"],
  "animationRange": ["entry 0%", "entry 50%"]
}
```

### 9.3 限制条件

**默认拒绝"炫酷动画"：**
- 除非用户明确要求
- 不影响首屏加载速度
- 不造成视觉干扰

---

## 10. 脚本集成

### 10.1 使用条件

**只有用户明确要求脚本时才允许使用。**

### 10.2 GSAP 集成

```json
{
  "customJsEnabled": true,
  "customJs": "import gsap from 'https://cdn.skypack.dev/gsap@3.12.2';\ngsap.to('.element', {opacity: 1});"
}
```

**GSAP 固定路径：**
```
https://cdn.skypack.dev/gsap@3.12.2
```

---

## 11. 媒体资源

### 11.1 图片

```json
{
  "tag": "img",
  "src": "https://example.com/image.jpg",
  "alt": "图片描述",
  "originalWidth": 1200,
  "originalHeight": 800,
  "loading": "lazy"
}
```

**必需字段：**
- `src` - 图片 URL
- `alt` - 无障碍描述
- `originalWidth` / `originalHeight` - 原始尺寸

### 11.2 视频

```json
{
  "tag": "video",
  "src": "https://example.com/video.mp4",
  "autoplay": true,
  "loop": true,
  "muted": true
}
```

### 11.3 SVG 图标

```json
{
  "tag": "svg",
  "icon": {
    "icon": {
      "svg": "<svg viewBox='0 0 24 24'><path d='...'></path></svg>"
    }
  }
}
```

**注意：** 最终 HTML 中移除 `xmlns` 属性

---

## 12. 表单元素

### 12.1 按钮

```json
{
  "tag": "button",
  "type": "inner",
  "formAttributes": {
    "type": "submit"
  },
  "textContent": "提交"
}
```

**关键点：** `type` 字段写入 `formAttributes.type`，不写到顶层 JSON

### 12.2 输入框

```json
{
  "tag": "input",
  "formAttributes": {
    "type": "email",
    "placeholder": "请输入邮箱",
    "required": true
  }
}
```

---

## 13. 性能优化

### 13.1 减少嵌套

❌ 过度嵌套：
```html
<div>
  <div>
    <div>
      <div>内容</div>
    </div>
  </div>
</div>
```

✅ 扁平化：
```html
<div>内容</div>
```

### 13.2 避免多余 class

只在有 `styleAttributes` 或需要引用时添加 class。

### 13.3 首屏优先

- 首屏内容避免复杂动画
- 图片使用 `loading="lazy"`（除首屏图片外）
- 减少首屏 JavaScript

---

## 14. 验证与调试

### 14.1 语法验证

生成区块后，使用验证脚本检查：
```bash
python scripts/validate_greenshift_block.py block.html
```

### 14.2 常见错误

| 错误 | 原因 | 解决 |
|------|------|------|
| 区块无法渲染 | JSON 格式错误 | 检查逗号、引号、括号 |
| 样式不生效 | 缺少 localId class | 确保 HTML class 包含 localId |
| 响应式失效 | 数组顺序错误 | 使用固定顺序 `[桌面,平板,横屏,竖屏]` |
| 动画不触发 | 缺少 animationTimeline | 滚动动画必须指定 timeline |

---

## 15. 快速参考清单

生成区块前必查：
- [ ] `id` 和 `localId` 已生成且相同
- [ ] `tag` 根据语义选择
- [ ] `type` 正确（inner/text/no/chart）
- [ ] 样式全部在 `styleAttributes` 中（camelCase）
- [ ] 响应式数组顺序正确
- [ ] 有样式时 HTML class 包含 localId
- [ ] 媒体资源有 alt/width/height
- [ ] 动画不影响首屏性能
- [ ] 未使用 inline `style=""`
- [ ] 优先使用站点变量 `var(--wp--...)`
