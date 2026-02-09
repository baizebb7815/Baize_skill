---
name: visual-asset-director
description: Create website image shot lists and universal prompts plus publish metadata (filename, alt, caption). Also create icon packs and reference-image reverse analysis with copyright-safe remakes. Use when the user asks for image prompts, shot lists, recreate/remake a reference image, blog/news/tutorial images, website images, icons, pictograms, Imagen4, nanobanana, image governance, or an Image Pack/Icon Pack for BASIS SIGN pages.
---

# Visual Asset Director

Provide production-ready image guidance for BASIS SIGN website content.

## Operating rules

- Prioritize inquiry conversion clarity over visual flair.
- Do not generate text inside images. If a graphic needs copy, output it as separate plain text (for manual design), and keep the image prompt "no text".
- Do not provide instructions to replicate a copyrighted image 1:1. If a user supplies a reference image, extract the style and rebuild an original image with clear deviations.
- If the user requests enhancement of their own low-res image, keep composition and details unchanged; only improve clarity.
- If the page type or section is unknown, infer the most likely use and proceed.
- Default conversion goal: quote / design mockup / contact.
- If the user asks for 1-2 images or a single block/paragraph, produce a minimal pack with 1-3 shots.
- Default audience:
  - Commercial signage (channel letters, light boxes, metal letters) -> B2B.
  - LED neon for events/home/creators -> B2C.

## Workflow

1. Infer context (page/module/product/audience/conversion goal) from the request.
2. Select a consistent visual style preset from [basis-visual-system.md](references/basis-visual-system.md).
3. Choose the deliverable:
   - If the request is page/blog/news/tutorial imagery: use [image-pack.md](references/image-pack.md).
   - If the request is icons/pictograms/patterns: use [icon-pack.md](references/icon-pack.md).
   - If the request is to recreate/remake a reference image: use [reference-remake.md](references/reference-remake.md) and output JSON prompts.
4. For every image, output one universal prompt.
5. Add publish metadata per image: file name, alt text, optional caption.

## Output format

Always output exactly one pack:

- **Image Pack** for pages, blogs, news, tutorials, blocks, and single paragraphs
- **Icon Pack** for icons/pictograms/patterns

Image Pack template:

- **Context Summary**
- **Style Preset**
- **Shot List**
- **Per-shot Prompt Bundle** (prompt + negative constraints)
- **SEO Publish Pack** (file name + alt + caption)

Icon Pack template:

- **Context Summary**
- **Style System**
- **Icon List**
- **Per-icon Prompt Bundle** (prompt + negative constraints)
- **Export Notes**
- **Publish Pack**

Use [prompt-library.md](references/prompt-library.md) for reusable building blocks and product-specific visual cues.

Use [governance.md](references/governance.md) for naming/alt policy, reuse strategy, and safety.

Use [icon-pack.md](references/icon-pack.md) when the user asks for icons, pictograms, or simple patterns.

Use [reference-remake.md](references/reference-remake.md) when the user provides a reference image and wants a copyright-safe remake.

