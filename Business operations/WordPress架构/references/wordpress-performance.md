# WordPress 速度与性能优化指南

本文档提供 WordPress 速度优化的最佳实践，帮助控制风险，避免"把站改崩"。

---

## 核心原则

> **渐进式优化 > 激进式改造**

- 一次只改一项，观察效果
- 先优化影响大的项目
- 始终保持备份
- 使用 staging 环境测试

---

## 1. 速度指标理解

### 1.1 Core Web Vitals（核心网页指标）

Google 的三大核心指标：

| 指标 | 全称 | 目标 | 影响因素 |
|------|------|------|----------|
| **LCP** | Largest Contentful Paint | < 2.5s | 首屏最大元素加载速度 |
| **FID** | First Input Delay | < 100ms | 首次交互响应时间 |
| **CLS** | Cumulative Layout Shift | < 0.1 | 视觉稳定性（避免跳动） |

### 1.2 其他重要指标

| 指标 | 说明 | 目标 |
|------|------|------|
| **TTFB** | Time to First Byte | < 600ms |
| **FCP** | First Contentful Paint | < 1.8s |
| **TTI** | Time to Interactive | < 3.8s |
| **Speed Index** | 视觉加载速度 | < 3.4s |

### 1.3 测速工具

**推荐工具（按优先级）：**
1. **Google PageSpeed Insights** - 官方工具，最权威
2. **GTmetrix** - 详细分析，瀑布图
3. **Pingdom** - 多地点测速
4. **WebPageTest** - 高级分析

---

## 2. 主机优化（影响最大）

### 2.1 主机选择

**性能排序：**
```
专用服务器 > VPS > 优质共享主机 > 低价共享主机
```

**推荐配置（中小型网站）：**
- CPU: 至少 2 核心
- RAM: 至少 2GB
- SSD 存储
- HTTP/2 支持
- PHP 8.0+

### 2.2 主机优化项

**必做：**
- [ ] 启用 OPcache（PHP 缓存）
- [ ] 启用 Gzip/Brotli 压缩
- [ ] 配置合理的 PHP 内存限制（256MB+）
- [ ] 使用最新稳定版 PHP（8.0+）

**可选：**
- [ ] 启用 Redis/Memcached（对象缓存）
- [ ] 配置 CDN
- [ ] 启用 HTTP/2 或 HTTP/3

---

## 3. 缓存策略（必须掌握）

### 3.1 缓存层级

```
浏览器缓存（最快）
    ↓
CDN 缓存
    ↓
页面缓存（插件）
    ↓
对象缓存（Redis/Memcached）
    ↓
数据库查询缓存
    ↓
OPcache（PHP 代码缓存）
```

### 3.2 推荐缓存插件

**选一个即可，不要同时用多个：**

| 插件 | 特点 | 适用场景 |
|------|------|----------|
| **WP Rocket** | 付费，最简单 | 非技术用户 |
| **W3 Total Cache** | 免费，功能全 | 技术用户 |
| **WP Super Cache** | 免费，轻量 | 小型网站 |
| **LiteSpeed Cache** | 免费，需 LiteSpeed 主机 | LiteSpeed 主机用户 |

### 3.3 缓存配置要点

**页面缓存：**
- ✅ 启用 HTML 缓存
- ✅ 排除登录用户
- ✅ 排除动态页面（购物车/结账）

**浏览器缓存：**
```apache
# .htaccess 示例
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/jpg "access plus 1 year"
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
  ExpiresByType text/css "access plus 1 month"
  ExpiresByType application/javascript "access plus 1 month"
</IfModule>
```

**对象缓存：**
- 使用 Redis 或 Memcached
- 安装对应插件（如 Redis Object Cache）

---

## 4. 图片优化（影响巨大）

### 4.1 图片格式选择

| 格式 | 适用场景 | 压缩率 |
|------|----------|--------|
| **WebP** | 通用（推荐） | 最高 |
| **AVIF** | 新格式（兼容性差） | 极高 |
| **JPEG** | 照片 | 中等 |
| **PNG** | 透明图/图标 | 低 |
| **SVG** | 矢量图标 | 最小 |

### 4.2 优化策略

**必做：**
- [ ] 压缩图片（工具：TinyPNG、ImageOptim）
- [ ] 使用正确尺寸（不要上传 5000px 显示 500px）
- [ ] 启用 lazy loading（延迟加载）
- [ ] 使用响应式图片（srcset）

**推荐插件：**
- **ShortPixel** - 自动压缩，支持 WebP
- **Smush** - 免费版已够用
- **Imagify** - 付费，效果好

### 4.3 代码实现

**Lazy Loading（原生）：**
```html
<img src="image.jpg" loading="lazy" alt="描述">
```

**响应式图片：**
```html
<img 
  src="image-800w.jpg"
  srcset="
    image-400w.jpg 400w,
    image-800w.jpg 800w,
    image-1200w.jpg 1200w
  "
  sizes="(max-width: 600px) 400px, 800px"
  alt="描述"
>
```

---

## 5. CSS/JS 优化

### 5.1 精简与合并

**策略：**
- 合并小文件（减少 HTTP 请求）
- 压缩（Minify）CSS/JS
- 移除未使用的代码

**推荐插件：**
- **Autoptimize** - 自动合并压缩
- **Asset CleanUp** - 按页面禁用不需要的 CSS/JS

### 5.2 关键 CSS 内联

**原理：**
将首屏必需的 CSS 内联到 `<head>`，其余 CSS 延迟加载

**工具：**
- WP Rocket（付费）
- Critical CSS Generator（在线工具）

### 5.3 JavaScript 延迟加载

**策略：**
```html
<!-- 不阻塞渲染 -->
<script src="script.js" defer></script>

<!-- 异步加载 -->
<script src="analytics.js" async></script>
```

**规则：**
- `defer` - 按顺序执行，不阻塞 HTML 解析
- `async` - 立即执行，可能乱序

---

## 6. 数据库优化

### 6.1 常规清理

**必做（定期）：**
- [ ] 删除修订版本（Post Revisions）
- [ ] 清理垃圾评论/待审评论
- [ ] 删除过期的 Transients
- [ ] 优化数据库表

**推荐插件：**
- **WP-Optimize** - 一键清理
- **Advanced Database Cleaner** - 深度清理

### 6.2 限制修订版本

**wp-config.php：**
```php
// 限制修订版本数量
define('WP_POST_REVISIONS', 3);

// 或完全禁用
define('WP_POST_REVISIONS', false);
```

### 6.3 索引优化

大型网站需定期检查数据库索引，使用 phpMyAdmin 或专业 DBA。

---

## 7. 插件管理（风险控制）

### 7.1 插件选择原则

**必查：**
- ✅ 活跃安装数 >10,000
- ✅ 最近更新 <6 个月
- ✅ 兼容当前 WordPress 版本
- ✅ 评分 >4.0

**禁忌：**
- ❌ 同时安装功能重复的插件
- ❌ 安装来历不明的插件
- ❌ 长期不更新的插件

### 7.2 插件数量控制

**建议：**
- 小型网站：<15 个插件
- 中型网站：<25 个插件
- 大型网站：<35 个插件

**核心：功能 > 数量**
- 1 个高质量多功能插件 > 5 个低质量单一插件

### 7.3 已知重量级插件

**小心使用（影响性能）：**
- Elementor（页面构建器）
- Revolution Slider（滑块）
- Jetpack（功能过多）
- Social Sharing 插件（加载外部脚本）

**建议：**
- 能用轻量级替代就换
- 禁用不需要的功能
- 按页面加载（Asset CleanUp）

---

## 8. 主题优化

### 8.1 主题选择

**轻量级主题推荐：**
- **GeneratePress** - 极轻量，高度可定制
- **Astra** - 快速，兼容页面构建器
- **Neve** - 现代设计，性能好

**避免：**
- 臃肿的多功能主题（ThemeForest 常见）
- 内置大量不需要的功能
- 过多动画/特效

### 8.2 主题优化项

**必做：**
- [ ] 移除未使用的 Google Fonts
- [ ] 禁用 emoji 脚本（如不需要）
- [ ] 移除 jQuery（如可替代）
- [ ] 使用子主题（避免更新丢失修改）

**禁用 emoji：**
```php
// functions.php
remove_action('wp_head', 'print_emoji_detection_script', 7);
remove_action('wp_print_styles', 'print_emoji_styles');
```

---

## 9. CDN 配置

### 9.1 CDN 选择

**推荐：**
- **Cloudflare** - 免费，易用，功能全
- **BunnyCDN** - 付费，性价比高
- **KeyCDN** - 付费，专业级

### 9.2 CDN 配置要点

**必配：**
- 静态资源（CSS/JS/图片/字体）
- 缓存规则（浏览器缓存时间）
- HTTPS/SSL

**可选：**
- Brotli 压缩
- 自动 WebP 转换
- 图片优化

---

## 10. GreenShift 区块性能控制

### 10.1 避免过度嵌套

❌ **错误：**
```html
<div>
  <div>
    <div>
      <div>
        <div>内容</div>
      </div>
    </div>
  </div>
</div>
```

✅ **正确：**
```html
<section>
  <div class="content-area">
    <h1>标题</h1>
    <p>内容</p>
  </div>
</section>
```

### 10.2 动画性能

**高性能属性（GPU 加速）：**
- `transform`
- `opacity`

**低性能属性（避免动画）：**
- `width`/`height`
- `top`/`left`
- `margin`/`padding`

**示例：**
```json
// ✅ 好
"animation_keyframes_Extra": {
  "0%": {"opacity": 0, "transform": "translateY(20px)"},
  "100%": {"opacity": 1, "transform": "translateY(0)"}
}

// ❌ 差
"animation_keyframes_Extra": {
  "0%": {"marginTop": "20px"},
  "100%": {"marginTop": "0"}
}
```

### 10.3 首屏优化

**规则：**
- 首屏内容避免复杂动画
- 首屏图片不使用 `loading="lazy"`
- 关键 CSS 内联
- 延迟加载非必需脚本

---

## 11. 测试与监控

### 11.1 上线前检查清单

**必测：**
- [ ] 桌面端 PageSpeed Insights >90
- [ ] 移动端 PageSpeed Insights >80
- [ ] GTmetrix 评分 A/B
- [ ] 实际加载时间 <3 秒（4G 网络）

**跨设备测试：**
- [ ] Chrome（桌面/移动）
- [ ] Safari（iPhone/iPad）
- [ ] Firefox
- [ ] Edge

### 11.2 持续监控

**工具：**
- Google Search Console（Core Web Vitals 报告）
- Google Analytics（页面速度）
- Uptime Robot（宕机监控）

**频率：**
- 每周检查一次 PageSpeed Insights
- 每月检查一次 GTmetrix
- 实时监控宕机情况

---

## 12. 常见错误与修复

### 错误 1: 安装太多缓存插件

**问题：** 同时安装 WP Rocket + W3 Total Cache + WP Super Cache

**影响：** 冲突、缓存失效、甚至网站崩溃

**修复：** 只保留一个缓存插件

---

### 错误 2: 不排除动态页面

**问题：** 缓存了购物车、结账页、用户中心

**影响：** 用户看到别人的数据、购物车不更新

**修复：** 在缓存插件中排除这些页面

---

### 错误 3: 图片尺寸错误

**问题：** 上传 5000x5000px 图片，显示 500x500px

**影响：** 浪费带宽，加载慢

**修复：** 使用正确尺寸 + 压缩

---

### 错误 4: 过度优化

**问题：** 合并所有 CSS/JS，启用所有优化选项

**影响：** 功能失效、样式错乱

**修复：** 渐进式优化，一次改一项

---

## 13. 速度优化优先级清单

**第 1 优先级（影响最大）：**
1. 升级主机（如现在是低价共享主机）
2. 启用页面缓存
3. 优化图片（压缩 + lazy loading）
4. 配置 CDN

**第 2 优先级：**
5. 精简插件（删除不必要的）
6. 启用对象缓存（Redis/Memcached）
7. 压缩 CSS/JS
8. 优化数据库

**第 3 优先级（进阶）：**
9. 关键 CSS 内联
10. 延迟加载 JavaScript
11. 使用轻量级主题
12. 移除不必要的字体

---

## 14. 紧急情况处理

### 网站变慢/崩溃后如何排查

**步骤：**
1. 禁用最近安装的插件
2. 切换到默认主题（Twenty Twenty-Four）
3. 清除所有缓存
4. 检查主机资源使用（CPU/内存）
5. 检查错误日志（wp-content/debug.log）

**恢复方案：**
- 使用备份恢复（UpdraftPlus/VaultPress）
- 联系主机商技术支持

---

## 15. 速度优化 Checklist

**基础优化（必做）：**
- [ ] 选择高性能主机
- [ ] 安装缓存插件并正确配置
- [ ] 压缩并优化所有图片
- [ ] 启用 Gzip/Brotli 压缩
- [ ] 使用最新版 PHP（8.0+）

**进阶优化：**
- [ ] 配置 CDN
- [ ] 启用对象缓存（Redis/Memcached）
- [ ] 精简 CSS/JS
- [ ] 使用轻量级主题
- [ ] 定期清理数据库

**性能监控：**
- [ ] 设置 Google Search Console
- [ ] 每周检查 PageSpeed Insights
- [ ] 监控 Core Web Vitals

---

## 总结

**黄金法则：**
> 测量 → 优化 → 验证 → 重复

永远先测速，再优化，再测速验证效果。不要盲目优化。
