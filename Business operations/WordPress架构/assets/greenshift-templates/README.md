# GreenShift 模板使用说明

本目录包含预制的 GreenShift 区块模板，可直接复制粘贴到 WordPress 编辑器使用。

## 📁 可用模板

### 1. hero-section.html
**全宽 Hero Section（首屏大标题区块）**

特点：
- 全宽深色背景
- 居中标题 + 副标题 + CTA 按钮
- 完整响应式设计
- 使用站点颜色变量

适用场景：
- 落地页首屏
- 产品介绍页顶部
- 服务页首屏

---

### 2. cta-section.html
**Call-to-Action 行动号召区块**

特点：
- 浅色背景区块
- 居中内容布局
- 大标题 + 描述 + 按钮
- Hover 动画效果

适用场景：
- 页面底部 CTA
- 转化引导区块
- 产品购买/咨询区

---

### 3. faq-section.html
**FAQ 常见问题区块**

特点：
- 包含 3 个 FAQ 项目
- 清晰的问答结构
- 分割线视觉区分
- Schema Markup 友好

适用场景：
- 产品页 FAQ
- 服务页常见问题
- 博客文章底部 FAQ

---

## 🚀 使用步骤

### 步骤 1: 选择模板
根据需求选择合适的模板文件

### 步骤 2: 复制内容
打开模板文件，复制全部内容

### 步骤 3: 生成新 ID
使用脚本生成唯一 ID：
```bash
python ../scripts/generate_block_id.py 10
```

### 步骤 4: 替换 ID
将模板中的所有 `gsbp-XXXXXXX` 替换为新生成的 ID

**重要：确保每个区块的 `id` 和 `localId` 相同**

### 步骤 5: 修改内容
替换占位文本（标注为 `[...]` 的部分）：
- `[在这里写你的标题]` → 实际标题
- `[CTA 标题]` → 实际 CTA 文案
- `[问题 1]` → 实际问题
- 等等

### 步骤 6: 调整样式（可选）
根据品牌需求调整：
- 颜色（使用站点颜色变量或自定义）
- 间距（padding/margin）
- 字体大小
- 边框圆角

### 步骤 7: 粘贴到 WordPress
在 WordPress 编辑器中：
1. 点击 "+" 添加区块
2. 选择 "代码编辑器" 或直接粘贴
3. 粘贴修改后的模板代码
4. 切换回可视化编辑器查看效果

---

## ⚠️ 重要提醒

### 必须替换的内容
- ✅ **所有 ID**（使用 `generate_block_id.py` 生成）
- ✅ **占位文本**（`[...]` 标记的部分）
- ✅ **链接 href**（如 `#contact` 改为实际链接）

### 可选修改的内容
- 颜色（建议使用站点变量）
- 字体大小（响应式数组）
- 间距
- 动画效果

### 不建议修改的部分
- JSON 结构
- 必需字段（id, localId, type, tag）
- 响应式数组顺序

---

## 🎨 自定义建议

### 使用站点颜色变量
优先使用 WordPress 全局颜色：
```json
"backgroundColor": "var(--wp--preset--color--primary, #000)"
```

好处：
- 统一站点配色
- 一处修改，全站更新
- 更好的主题兼容性

### 响应式调整
模板已包含完整响应式设计：
```json
"fontSize": ["56px", "42px", "32px", "28px"]
// [桌面, 平板, 横屏手机, 竖屏手机]
```

根据需要调整各断点的值。

---

## 🔧 验证模板

修改完成后，验证代码是否正确：
```bash
python ../scripts/validate_greenshift_block.py your-file.html
```

---

## 💡 组合使用示例

**典型落地页结构：**
```
1. hero-section.html (首屏)
   ↓
2. [自定义特性展示区块]
   ↓
3. [自定义客户评价区块]
   ↓
4. faq-section.html (FAQ)
   ↓
5. cta-section.html (底部 CTA)
```

---

## 📚 相关文档

- 完整语法规范: `../references/greenshift-core-rules.md`
- 更多区块模式: `../references/greenshift-block-patterns.md`
- 生成 ID 脚本: `../scripts/generate_block_id.py`
- 验证脚本: `../scripts/validate_greenshift_block.py`
