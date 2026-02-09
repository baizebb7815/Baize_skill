# GreenShift 区块模式库
本文档包含常用的 GreenShift 区块组合模式，可直接参考或修改使用。
阅读顺序建议：先看 **0. 项目参考代码**（锁定你站可导入语法），再套用 **1+ 模式库**。

默认策略：
* **Safe**：优先只用 `greenshift-blocks/element`（兼容与可导入成功率更高）
* **Full**：当需要复刻复杂交互/组件，或参考源码本身包含其它 GreenShift 区块时，允许使用 `container/row/row-column/heading/text/button/swiper` 等已验证区块

说明：文档中若出现 `greenshift-blocks/contentcolumns` 等写法，请视为结构理解用旧例；实际落地请优先用 element 的 `flexColumns_Extra / flexWidths_Extra` 或改写为 Full 档的 `row/row-column` 结构。

---

## 1. Hero Section 模式
### 1.1 全宽 Hero + 居中内容

```html
<!-- wp:greenshift-blocks/element {"id":"gsbp-a1b2c3d","localId":"gsbp-a1b2c3d","tag":"section","type":"inner","align":"full","dynamicAttributes":[{"name":"data-type","value":"section-component"}],"styleAttributes":{"backgroundColor":"var(--wp--preset--color--primary, #000)","paddingTop":["80px","60px","40px","40px"],"paddingBottom":["80px","60px","40px","40px"]}} -->
<section class="gsbp-a1b2c3d" data-type="section-component">
<!-- wp:greenshift-blocks/element {"id":"gsbp-b1c2d3e","localId":"gsbp-b1c2d3e","tag":"div","type":"inner","styleAttributes":{"maxWidth":"var(--wp--style--global--wide-size, 1200px)","marginLeft":"auto","marginRight":"auto","paddingLeft":"20px","paddingRight":"20px","textAlign":"center"}} -->
<div class="gsbp-b1c2d3e">
<!-- wp:greenshift-blocks/element {"id":"gsbp-c1d2e3f","localId":"gsbp-c1d2e3f","tag":"h1","type":"text","textContent":"Your Powerful Headline Here","styleAttributes":{"fontSize":["48px","36px","28px","24px"],"color":"#fff","marginBottom":"20px","fontWeight":700}} -->
<h1 class="gsbp-c1d2e3f">Your Powerful Headline Here</h1>
<!-- /wp:greenshift-blocks/element -->
<!-- wp:greenshift-blocks/element {"id":"gsbp-d1e2f3g","localId":"gsbp-d1e2f3g","tag":"p","type":"text","textContent":"Supporting text that explains your value proposition clearly and concisely.","styleAttributes":{"fontSize":["18px","16px","14px","14px"],"color":"rgba(255,255,255,0.9)","marginBottom":"30px","maxWidth":"600px","marginLeft":"auto","marginRight":"auto"}} -->
<p class="gsbp-d1e2f3g">Supporting text that explains your value proposition clearly and concisely.</p>
<!-- /wp:greenshift-blocks/element -->
<!-- wp:greenshift-blocks/element {"id":"gsbp-e1f2g3h","localId":"gsbp-e1f2g3h","tag":"a","type":"inner","href":"#contact","styleAttributes":{"display":"inline-block","backgroundColor":"#fff","color":"#000","padding":"15px 40px","borderRadius":"8px","textDecoration":"none","fontWeight":600,"backgroundColor_hover":"rgba(255,255,255,0.9)"}} -->
<a class="gsbp-e1f2g3h" href="#contact"><!-- wp:greenshift-blocks/element {"id":"gsbp-f1g2h3i","localId":"gsbp-f1g2h3i","tag":"span","type":"text","textContent":"Get Started"} -->
<span class="gsbp-f1g2h3i">Get Started</span>
<!-- /wp:greenshift-blocks/element --></a>
<!-- /wp:greenshift-blocks/element -->
</div>
<!-- /wp:greenshift-blocks/element -->
</section>
<!-- /wp:greenshift-blocks/element -->
```

---

## 0. 项目参考代码（你站导出，可导入验证）
以下片段来自仓库内的 **`/greenshift_layout.md`** 与 **`/greenshift_Experimental.md`**，用于锁定你站当前 GreenShift 的“真实可导入语法”。
### 0.1 `section-component` + `content-area-component`（最小可用骨架）

```html
<!-- wp:greenshift-blocks/element {"id":"gsbp-e812203","tag":"section","type":"inner","localId":"gsbp-e812203","align":"full","dynamicAttributes":[{"name":"data-type","value":"section-component"}],"styleAttributes":{"display":["flex"],"justifyContent":["center"],"flexDirection":["column"],"alignItems":["center"],"paddingRight":["var(--wp--custom--spacing--side, min(3vw, 20px))"],"paddingLeft":["var(--wp--custom--spacing--side, min(3vw, 20px))"],"paddingTop":["var(--wp--custom--spacing--top, 0px)"],"paddingBottom":["var(--wp--custom--spacing--bottom, 0px)"],"marginTop":["0px"],"marginBottom":["0px"],"paddingLink_Extra":"lr","position":["relative"],"backgroundColor":["#080808"]},"isVariation":"contentwrapper"} -->
<section class="gsbp-e812203 alignfull" data-type="section-component">
<!-- wp:greenshift-blocks/element {"id":"gsbp-1773b6c","metadata":{"name":"Content Area"},"type":"inner","localId":"gsbp-1773b6c","dynamicAttributes":[{"name":"data-type","value":"content-area-component"}],"styleAttributes":{"maxWidth":["100%"],"width":["var(--wp--style--global--wide-size, 1200px)"]},"isVariation":"nocolumncontent"} -->
<div class="gsbp-1773b6c" data-type="content-area-component">...</div>
<!-- /wp:greenshift-blocks/element -->
</section>
<!-- /wp:greenshift-blocks/element -->
```

### 0.2 `interactionLayers`（点击触发 lightbox）
```html
<!-- wp:greenshift-blocks/element {"id":"gsbp-2a03e8f","interactionLayers":[{"actions":[{"actionname":"lightbox"}],"env":"no-action","triggerData":{"trigger":"click","selector":".hk-card-visual"}}],"tag":"a","type":"inner","className":"hk-card-visual","localId":"gsbp-2a03e8f","href":"https://picsum.photos/seed/ny2024/800/1000"} -->
<a class="hk-card-visual" href="https://picsum.photos/seed/ny2024/800/1000"><!-- wp:greenshift-blocks/element {"id":"gsbp-806bdd4","interactionLayers":[],"tag":"img","type":"image","className":"hk-card-img","localId":"gsbp-806bdd4","src":"https://picsum.photos/seed/ny2024/800/1000","alt":"New York Landscape"} --><img class="hk-card-img" src="https://picsum.photos/seed/ny2024/800/1000" alt="New York Landscape" loading="lazy"/><!-- /wp:greenshift-blocks/element --></a>
<!-- /wp:greenshift-blocks/element -->
```

### 0.3 `stylemanager`（dynamicGClasses + customCSS_Extra）
这个模式用于把大量 CSS（含媒体查询）集中管理到一个 block 的 `dynamicGClasses` 里。

```html
<!-- wp:greenshift-blocks/element {"id":"gsbp-a0abcf6","type":"no","localId":"gsbp-a0abcf6","isVariation":"stylemanager","dynamicGClasses":[{"value":"hk-page-wrapper","type":"local","css":".hk-page-wrapper{max-width: 1800px; margin: 0 auto; padding: 0 60px;}@media (max-width: 1200px){.hk-page-wrapper{padding: 0 40px;}}@media (max-width: 768px){.hk-page-wrapper{padding: 0 20px;}}","attributes":{"styleAttributes":{"maxWidth":["1800px"],"margin":["0 auto"],"padding":["0 60px"],"customCSS_Extra":"@media (max-width: 1200px){.hk-page-wrapper{padding: 0 40px;}}@media (max-width: 768px){.hk-page-wrapper{padding: 0 20px;}}"}}}]} -->
<div class="hk-page-wrapper ..."></div>
<!-- /wp:greenshift-blocks/element -->
```

### 0.4 项目模块清单（便于复用/去重）
`greenshift_layout.md`：
* floating-on-scroll-panel
* coupon-popup-with-exit-intent
* featured-products
* Hero section with pulsing hot spots
* slider-with-sections
* banner-vertical
* accordion-two-columns
* featured-product-subscription
* scrollable-native-gallery

`greenshift_Experimental.md`：
* image-grid-with-hovered-text
* synced-custom-slider
* horizontal-timeline
* section-with-interactive-hover-links
* interactive-previos-next
* parallax-slider
* expandable-panels
* video-in-slider
* descalomusker-interaction-layers-demo
* circular-slider
* text-switch-button
* macdock-toolbar
* magnetic-vertical-tabs

### 0.5 `flipstate`（滚动触发的固定浮层）
摘自 `greenshift_layout.md` 的 `floating-on-scroll-panel`：

```html
<!-- wp:greenshift-blocks/flipstate {"id":"gsbp-40f4e86d-e895","triggerstart":"200","positionInit":{"positionType":["fixed","","",""],"positions":{"values":{"left":["0px"],"right":["0px"],"bottom":["-200px"]}},"Zindex":9},"positionActive":{"positionType":["fixed","","",""],"positions":{"values":{"left":["0px"],"right":["0px"],"bottom":["0px"]}},"Zindex":10}} -->
<div id="gspb_gsapflip-gsbp-40f4e86d-e895"><div id="gsbp-40f4e86d-e895" class="gs-flip-wrap wp-block-greenshift-blocks-flipstate" data-duration="1" data-triggertype="scroll" data-triggerstart="200">...</div></div>
<!-- /wp:greenshift-blocks/flipstate -->
```

### 0.6 `slidingPanel`（弹窗 + 退出意图关闭）
摘自 `greenshift_layout.md` 的 `coupon-popup-with-exit-intent`：

```html
<!-- wp:greenshift-blocks/button {"id":"gsbp-4bf44017-a265","buttonContent":"Reveal Coupon","slidingPanel":true,"slidePosition":"popup","width":[700],"closeintent":true} -->
<div class="wp-block-greenshift-blocks-button gspb_button_wrapper gspb_button-id-gsbp-4bf44017-a265"><a class="gspb-buttonbox" rel="noopener"><span class="gspb-buttonbox-textwrap"><span class="gspb-buttonbox-title">Reveal Coupon</span></span></a><div class="gspb_slidingPanel" data-closeintent="true"><div class="gspb_slidingPanel-wrap"><div class="gspb_slidingPanel-inner">...</div></div></div></div>
<!-- /wp:greenshift-blocks/button -->
```

### 0.7 `interactionLayers`（Hotspot 点击打开 Panel）
摘自 `greenshift_layout.md` 的 `Hero section with pulsing hot spots`：

```html
<!-- wp:greenshift-blocks/element {"id":"gsbp-07a3176","localId":"gsbp-07a3176","type":"inner","tag":"div","className":"lumina-hotspot hotspot-1","interactionLayers":[{"actions":[{"actionname":"panel","selector":"#panel_gsbp-07a3176"}],"env":"no-action","triggerData":{"trigger":"click"}}]} -->
<div class="lumina-hotspot hotspot-1"><!-- wp:greenshift-blocks/element {"id":"gsbp-4457ec9","localId":"gsbp-4457ec9","type":"inner","tag":"div","className":"lumina-pulse-center"} -->
<div class="lumina-pulse-center"><!-- wp:greenshift-blocks/element {"id":"gsbp-9e3f2bd","localId":"gsbp-9e3f2bd","type":"empty","tag":"div","className":"lumina-pulse-ring"} -->
<div class="lumina-pulse-ring"></div>
<!-- /wp:greenshift-blocks/element -->
<!-- wp:greenshift-blocks/element {"id":"gsbp-dc45c19","localId":"gsbp-dc45c19","type":"empty","tag":"div","className":"lumina-pulse-ring"} -->
<div class="lumina-pulse-ring"></div>
<!-- /wp:greenshift-blocks/element --></div>
<!-- /wp:greenshift-blocks/element --></div>
<!-- /wp:greenshift-blocks/element -->
```

### 0.8 `isSlider`（自定义控制器联动 Swiper）
摘自 `greenshift_Experimental.md` 的 `synced-custom-slider`：

```html
<!-- wp:greenshift-blocks/element {"id":"gsbp-2ed97f4","localId":"gsbp-2ed97f4","type":"inner","tag":"div","styleAttributes":{"width":["200px"],"marginBottom":["30px"]}} -->
<div class="gsbp-2ed97f4"><!-- wp:greenshift-blocks/element {"id":"gsbp-ad0520b","localId":"gsbp-ad0520b","type":"inner","tag":"div","styleAttributes":{"display":["flex"],"columnGap":["10px"]},"isSlider":true} -->
<div class="gsbp-ad0520b"><!-- wp:greenshift-blocks/element {"id":"gsbp-c61d0de","localId":"gsbp-c61d0de","type":"inner","tag":"div","className":"gs-slider-control-btn gs-slideto-1 circle-slider-cntrl"} -->
<div class="gs-slider-control-btn gs-slideto-1 circle-slider-cntrl"><!-- wp:greenshift-blocks/element {"id":"gsbp-1b0112b","localId":"gsbp-1b0112b","tag":"img","type":"image","src":"https://woocommerce-732526-3966075.cloudwaysapps.com/wp-content/uploads/2026/01/Rectangle-10.webp","alt":"","loading":"lazy","originalWidth":524,"originalHeight":686} -->
<img class="gsbp-1b0112b" src="https://woocommerce-732526-3966075.cloudwaysapps.com/wp-content/uploads/2026/01/Rectangle-10.webp" alt="" width="524" height="686" loading="lazy"/>
<!-- /wp:greenshift-blocks/element --></div>
<!-- /wp:greenshift-blocks/element --></div>
<!-- /wp:greenshift-blocks/element --></div>
<!-- /wp:greenshift-blocks/element -->
```


## 2. Two-Column Layout 模式
### 2.1 图文并排（50/50）

```html
<!-- wp:greenshift-blocks/contentcolumns {"id":"gsbp-g1h2i3j","localId":"gsbp-g1h2i3j","variation":"contentcolumns/contentarea","flexColumns_Extra":["2","2","1","1"],"flexWidths_Extra":[["50%","50%"],["50%","50%"],["100%"],["100%"]],"styleAttributes":{"gap":["40px","30px","20px","20px"]}} -->
<div class="gsbp-g1h2i3j">
<!-- 左列：图片 -->
<!-- wp:greenshift-blocks/element {"id":"gsbp-h1i2j3k","localId":"gsbp-h1i2j3k","tag":"img","type":"image","src":"https://example.com/image.jpg","alt":"Product showcase","originalWidth":600,"originalHeight":400,"loading":"lazy","styleAttributes":{"width":"100%","height":"auto","borderRadius":"12px"}} -->
<img class="gsbp-h1i2j3k" src="https://example.com/image.jpg" alt="Product showcase" width="600" height="400" loading="lazy">
<!-- /wp:greenshift-blocks/element -->
<!-- 右列：文本 --><!-- wp:greenshift-blocks/element {"id":"gsbp-i1j2k3l","localId":"gsbp-i1j2k3l","tag":"div","type":"inner","styleAttributes":{"display":"flex","flexDirection":"column","justifyContent":"center"}} -->
<div class="gsbp-i1j2k3l">
<!-- wp:greenshift-blocks/element {"id":"gsbp-j1k2l3m","localId":"gsbp-j1k2l3m","tag":"h2","type":"text","textContent":"Feature Title","styleAttributes":{"fontSize":["32px","28px","24px","20px"],"marginBottom":"15px","fontWeight":700}} -->
<h2 class="gsbp-j1k2l3m">Feature Title</h2>
<!-- /wp:greenshift-blocks/element -->
<!-- wp:greenshift-blocks/element {"id":"gsbp-k1l2m3n","localId":"gsbp-k1l2m3n","tag":"p","type":"text","textContent":"Detailed description of your feature or service goes here.","styleAttributes":{"fontSize":["16px","15px","14px","14px"],"lineHeight":"1.6","color":"#666"}} -->
<p class="gsbp-k1l2m3n">Detailed description of your feature or service goes here.</p>
<!-- /wp:greenshift-blocks/element -->

</div>
<!-- /wp:greenshift-blocks/element -->

</div>
<!-- /wp:greenshift-blocks/contentcolumns -->
```

---

## 3. Three-Column Grid 模式
### 3.1 特性展示卡片

```html
<!-- wp:greenshift-blocks/contentcolumns {"id":"gsbp-l1m2n3o","localId":"gsbp-l1m2n3o","variation":"contentcolumns/contentarea","flexColumns_Extra":["3","2","1","1"],"flexWidths_Extra":[["33.33%","33.33%","33.33%"],["50%","50%"],["100%"],["100%"]],"styleAttributes":{"gap":["30px","20px","20px","20px"],"paddingTop":"60px","paddingBottom":"60px"}} -->
<div class="gsbp-l1m2n3o">

<!-- 卡片 1 -->
<!-- wp:greenshift-blocks/element {"id":"gsbp-m1n2o3p","localId":"gsbp-m1n2o3p","tag":"div","type":"inner","styleAttributes":{"backgroundColor":"#f9f9f9","padding":"30px","borderRadius":"12px","textAlign":"center"}} -->
<div class="gsbp-m1n2o3p">

<!-- wp:greenshift-blocks/element {"id":"gsbp-n1o2p3q","localId":"gsbp-n1o2p3q","tag":"svg","type":"inner","icon":{"icon":{"svg":"<svg viewBox='0 0 24 24' fill='none' stroke='currentColor'><circle cx='12' cy='12' r='10'/></svg>"}},"styleAttributes":{"width":"48px","height":"48px","color":"var(--wp--preset--color--primary, #000)","marginBottom":"20px"}} -->
<svg class="gsbp-n1o2p3q" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/></svg>
<!-- /wp:greenshift-blocks/element -->

<!-- wp:greenshift-blocks/element {"id":"gsbp-o1p2q3r","localId":"gsbp-o1p2q3r","tag":"h3","type":"text","textContent":"Feature One","styleAttributes":{"fontSize":"20px","fontWeight":700,"marginBottom":"10px"}} -->
<h3 class="gsbp-o1p2q3r">Feature One</h3>
<!-- /wp:greenshift-blocks/element -->

<!-- wp:greenshift-blocks/element {"id":"gsbp-p1q2r3s","localId":"gsbp-p1q2r3s","tag":"p","type":"text","textContent":"Brief description of this feature.","styleAttributes":{"fontSize":"14px","color":"#666","lineHeight":"1.5"}} -->
<p class="gsbp-p1q2r3s">Brief description of this feature.</p>
<!-- /wp:greenshift-blocks/element -->

</div>
<!-- /wp:greenshift-blocks/element -->

<!-- 卡片 2 (复制卡片 1 结构，修改 ID 和内容) -->
<!-- wp:greenshift-blocks/element {"id":"gsbp-q1r2s3t","localId":"gsbp-q1r2s3t","tag":"div","type":"inner","styleAttributes":{"backgroundColor":"#f9f9f9","padding":"30px","borderRadius":"12px","textAlign":"center"}} -->
<div class="gsbp-q1r2s3t"><!-- 内容省略，结构同卡片 1 --></div>
<!-- /wp:greenshift-blocks/element -->

<!-- 卡片 3 -->
<!-- wp:greenshift-blocks/element {"id":"gsbp-r1s2t3u","localId":"gsbp-r1s2t3u","tag":"div","type":"inner","styleAttributes":{"backgroundColor":"#f9f9f9","padding":"30px","borderRadius":"12px","textAlign":"center"}} -->
<div class="gsbp-r1s2t3u"><!-- 内容省略，结构同卡片 1 --></div>
<!-- /wp:greenshift-blocks/element -->

</div>
<!-- /wp:greenshift-blocks/contentcolumns -->
```

---

## 4. CTA (Call-to-Action) 模式
### 4.1 全宽背景 + 居中 CTA

```html
<!-- wp:greenshift-blocks/element {"id":"gsbp-s1t2u3v","localId":"gsbp-s1t2u3v","tag":"section","type":"inner","align":"full","styleAttributes":{"backgroundColor":"var(--wp--preset--color--secondary, #f0f0f0)","paddingTop":"80px","paddingBottom":"80px","textAlign":"center"}} -->
<section class="gsbp-s1t2u3v">

<!-- wp:greenshift-blocks/element {"id":"gsbp-t1u2v3w","localId":"gsbp-t1u2v3w","tag":"div","type":"inner","styleAttributes":{"maxWidth":"var(--wp--style--global--content-size, 800px)","marginLeft":"auto","marginRight":"auto","paddingLeft":"20px","paddingRight":"20px"}} -->
<div class="gsbp-t1u2v3w">

<!-- wp:greenshift-blocks/element {"id":"gsbp-u1v2w3x","localId":"gsbp-u1v2w3x","tag":"h2","type":"text","textContent":"Ready to Get Started?","styleAttributes":{"fontSize":["36px","30px","24px","22px"],"fontWeight":700,"marginBottom":"20px"}} -->
<h2 class="gsbp-u1v2w3x">Ready to Get Started?</h2>
<!-- /wp:greenshift-blocks/element -->

<!-- wp:greenshift-blocks/element {"id":"gsbp-v1w2x3y","localId":"gsbp-v1w2x3y","tag":"p","type":"text","textContent":"Join thousands of satisfied customers today.","styleAttributes":{"fontSize":"18px","marginBottom":"30px","color":"#666"}} -->
<p class="gsbp-v1w2x3y">Join thousands of satisfied customers today.</p>
<!-- /wp:greenshift-blocks/element -->

<!-- wp:greenshift-blocks/element {"id":"gsbp-w1x2y3z","localId":"gsbp-w1x2y3z","tag":"a","type":"inner","href":"#contact","styleAttributes":{"display":"inline-block","backgroundColor":"var(--wp--preset--color--primary, #000)","color":"#fff","padding":"15px 40px","borderRadius":"8px","textDecoration":"none","fontWeight":600,"backgroundColor_hover":"rgba(0,0,0,0.85)"}} -->
<a class="gsbp-w1x2y3z" href="#contact"><!-- wp:greenshift-blocks/element {"id":"gsbp-x1y2z3a","localId":"gsbp-x1y2z3a","tag":"span","type":"text","textContent":"Contact Us Now"} -->
<span class="gsbp-x1y2z3a">Contact Us Now</span>
<!-- /wp:greenshift-blocks/element --></a>
<!-- /wp:greenshift-blocks/element -->

</div>
<!-- /wp:greenshift-blocks/element -->

</section>
<!-- /wp:greenshift-blocks/element -->
```

---

## 5. FAQ Accordion 模式
### 5.1 简单手风琴式 FAQ

```html
<!-- wp:greenshift-blocks/element {"id":"gsbp-y1z2a3b","localId":"gsbp-y1z2a3b","tag":"section","type":"inner","styleAttributes":{"paddingTop":"60px","paddingBottom":"60px"}} -->
<section class="gsbp-y1z2a3b">
<!-- wp:greenshift-blocks/element {"id":"gsbp-z1a2b3c","localId":"gsbp-z1a2b3c","tag":"div","type":"inner","styleAttributes":{"maxWidth":"var(--wp--style--global--content-size, 800px)","marginLeft":"auto","marginRight":"auto","paddingLeft":"20px","paddingRight":"20px"}} -->
<div class="gsbp-z1a2b3c">
<!-- wp:greenshift-blocks/element {"id":"gsbp-a2b3c4d","localId":"gsbp-a2b3c4d","tag":"h2","type":"text","textContent":"Frequently Asked Questions","styleAttributes":{"fontSize":"32px","fontWeight":700,"marginBottom":"40px","textAlign":"center"}} -->
<h2 class="gsbp-a2b3c4d">Frequently Asked Questions</h2>
<!-- /wp:greenshift-blocks/element -->

<!-- FAQ Item 1 -->
<!-- wp:greenshift-blocks/element {"id":"gsbp-b2c3d4e","localId":"gsbp-b2c3d4e","tag":"div","type":"inner","styleAttributes":{"borderBottom":"1px solid #e0e0e0","paddingTop":"20px","paddingBottom":"20px"}} -->
<div class="gsbp-b2c3d4e">
<!-- wp:greenshift-blocks/element {"id":"gsbp-c2d3e4f","localId":"gsbp-c2d3e4f","tag":"h3","type":"text","textContent":"What is your return policy?","styleAttributes":{"fontSize":"18px","fontWeight":600,"marginBottom":"10px"}} -->
<h3 class="gsbp-c2d3e4f">What is your return policy?</h3>
<!-- /wp:greenshift-blocks/element -->
<!-- wp:greenshift-blocks/element {"id":"gsbp-d2e3f4g","localId":"gsbp-d2e3f4g","tag":"p","type":"text","textContent":"We offer a 30-day money-back guarantee on all products.","styleAttributes":{"fontSize":"15px","color":"#666","lineHeight":"1.6"}} -->
<p class="gsbp-d2e3f4g">We offer a 30-day money-back guarantee on all products.</p>
<!-- /wp:greenshift-blocks/element -->
</div>
<!-- /wp:greenshift-blocks/element -->
<!-- FAQ Item 2 (重复结构，修改 ID 和内容) -->
</div>
<!-- /wp:greenshift-blocks/element -->
</section>
<!-- /wp:greenshift-blocks/element -->
```

---

## 6. Testimonial 模式
### 6.1 单个客户评价卡片

```html
<!-- wp:greenshift-blocks/element {"id":"gsbp-e2f3g4h","localId":"gsbp-e2f3g4h","tag":"div","type":"inner","styleAttributes":{"backgroundColor":"#fff","border":"1px solid #e0e0e0","borderRadius":"12px","padding":"30px","boxShadow":"0 4px 6px rgba(0,0,0,0.05)"}} -->
<div class="gsbp-e2f3g4h">
<!-- wp:greenshift-blocks/element {"id":"gsbp-f2g3h4i","localId":"gsbp-f2g3h4i","tag":"p","type":"text","textContent":"\"This product completely changed how we work. Highly recommended!\"","styleAttributes":{"fontSize":"16px","fontStyle":"italic","marginBottom":"20px","lineHeight":"1.6"}} -->
<p class="gsbp-f2g3h4i">"This product completely changed how we work. Highly recommended!"</p>
<!-- /wp:greenshift-blocks/element -->
<!-- wp:greenshift-blocks/element {"id":"gsbp-g2h3i4j","localId":"gsbp-g2h3i4j","tag":"div","type":"inner","styleAttributes":{"display":"flex","alignItems":"center","gap":"15px"}} -->
<div class="gsbp-g2h3i4j">
<!-- wp:greenshift-blocks/element {"id":"gsbp-h2i3j4k","localId":"gsbp-h2i3j4k","tag":"img","type":"image","src":"https://example.com/avatar.jpg","alt":"John Doe","originalWidth":60,"originalHeight":60,"loading":"lazy","styleAttributes":{"width":"60px","height":"60px","borderRadius":"50%","objectFit":"cover"}} -->
<img class="gsbp-h2i3j4k" src="https://example.com/avatar.jpg" alt="John Doe" width="60" height="60" loading="lazy">
<!-- /wp:greenshift-blocks/element -->
<!-- wp:greenshift-blocks/element {"id":"gsbp-i2j3k4l","localId":"gsbp-i2j3k4l","tag":"div","type":"inner"} -->
<div class="gsbp-i2j3k4l">
<!-- wp:greenshift-blocks/element {"id":"gsbp-j2k3l4m","localId":"gsbp-j2k3l4m","tag":"p","type":"text","textContent":"John Doe","styleAttributes":{"fontSize":"16px","fontWeight":600,"marginBottom":"5px"}} -->
<p class="gsbp-j2k3l4m">John Doe</p>
<!-- /wp:greenshift-blocks/element -->
<!-- wp:greenshift-blocks/element {"id":"gsbp-k2l3m4n","localId":"gsbp-k2l3m4n","tag":"p","type":"text","textContent":"CEO, Example Corp","styleAttributes":{"fontSize":"14px","color":"#999"}} -->
<p class="gsbp-k2l3m4n">CEO, Example Corp</p>
<!-- /wp:greenshift-blocks/element -->
</div>
<!-- /wp:greenshift-blocks/element -->
</div>
<!-- /wp:greenshift-blocks/element -->
</div>
<!-- /wp:greenshift-blocks/element -->
```

---

## 7. 滚动动画模式
### 7.1 淡入效果

```html
<!-- wp:greenshift-blocks/element {"id":"gsbp-l2m3n4o","localId":"gsbp-l2m3n4o","tag":"div","type":"inner","animation_keyframes_Extra":{"0%":{"opacity":0,"transform":"translateY(20px)"},"100%":{"opacity":1,"transform":"translateY(0)"}},"animation":"fadeInUp linear forwards","animationTimeline":["view()"],"animationRange":["entry 0%","entry 50%"]} -->
<div class="gsbp-l2m3n4o">
<!-- 内容 -->
</div>
<!-- /wp:greenshift-blocks/element -->
```

### 7.2 缩放效果

```html
<!-- wp:greenshift-blocks/element {"id":"gsbp-m2n3o4p","localId":"gsbp-m2n3o4p","tag":"div","type":"inner","animation_keyframes_Extra":{"0%":{"opacity":0,"transform":"scale(0.8)"},"100%":{"opacity":1,"transform":"scale(1)"}},"animation":"scaleIn 0.6s ease-out forwards","animationTimeline":["view()"],"animationRange":["entry 0%","entry 30%"]} -->
<div class="gsbp-m2n3o4p">
<!-- 内容 -->
</div>
<!-- /wp:greenshift-blocks/element -->
```

---

## 8. 轮播/滑块模式
### 8.1 图片轮播

```html
<!-- wp:greenshift-blocks/swiper {"id":"gsbp-n2o3p4q","localId":"gsbp-n2o3p4q","slidesPerView":1,"spaceBetween":20,"autoplay":true,"loop":true,"pagination":true,"navigation":true} -->
<div class="gsbp-n2o3p4q swiper">

<!-- wp:greenshift-blocks/element {"id":"gsbp-o2p3q4r","localId":"gsbp-o2p3q4r","tag":"div","type":"inner"} -->
<div class="gsbp-o2p3q4r swiper-slide">
<!-- wp:greenshift-blocks/element {"id":"gsbp-p2q3r4s","localId":"gsbp-p2q3r4s","tag":"img","type":"image","src":"https://example.com/slide1.jpg","alt":"Slide 1","loading":"lazy","originalWidth":1200,"originalHeight":600,"styleAttributes":{"width":"100%","height":"auto"}} -->
<img class="gsbp-p2q3r4s" src="https://example.com/slide1.jpg" alt="Slide 1" width="1200" height="600" loading="lazy">
<!-- /wp:greenshift-blocks/element -->
</div>
<!-- /wp:greenshift-blocks/element -->

<!-- wp:greenshift-blocks/element {"id":"gsbp-q2r3s4t","localId":"gsbp-q2r3s4t","tag":"div","type":"inner"} -->
<div class="gsbp-q2r3s4t swiper-slide">
<!-- wp:greenshift-blocks/element {"id":"gsbp-r2s3t4u","localId":"gsbp-r2s3t4u","tag":"img","type":"image","src":"https://example.com/slide2.jpg","alt":"Slide 2","loading":"lazy","originalWidth":1200,"originalHeight":600,"styleAttributes":{"width":"100%","height":"auto"}} -->
<img class="gsbp-r2s3t4u" src="https://example.com/slide2.jpg" alt="Slide 2" width="1200" height="600" loading="lazy">
<!-- /wp:greenshift-blocks/element -->
</div>
<!-- /wp:greenshift-blocks/element -->

</div>
<!-- /wp:greenshift-blocks/swiper -->
```

---

## 9. 使用建议
### 9.1 模式选择原则

| 页面部分 | 推荐模式 |
|---------|---------|
| 首屏 | Hero Section |
| 功能介绍 | Two-Column Layout / Three-Column Grid |
| 社会证明 | Testimonial |
| 常见问题 | FAQ Accordion |
| 转化点 | CTA |
| 动态内容 | Slider |

### 9.2 组合使用
典型落地页结构：
1. Hero Section（首屏）
2. Three-Column Grid（特性展示）
3. Two-Column Layout（详细介绍）
4. Testimonial（客户评价）
5. FAQ（常见问题）
6. CTA（行动号召）

### 9.3 自定义提示
复制模式后记得：
- 替换所有 `gsbp-xxxxxxx` ID（使用 `scripts/generate_block_id.py`）
- 修改文本内容
- 更新图片 URL 和 alt
- 调整颜色/间距以匹配品牌
- 根据响应式数组调整不同设备的样式
