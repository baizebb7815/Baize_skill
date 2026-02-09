# Icon Pack Template

Use this when the request is for icons, pictograms, small UI illustrations, or simple repeating patterns.

## Context Summary

- Brand: BASIS SIGN
- Use case: (website UI / blog callouts / product specs / process steps)
- Audience mode: (B2B / B2C)
- Icon count:
- Target sizes:
  - 24px (navigation)
  - 48px (feature cards)
  - 96px (hero badges)
- Format targets:
  - SVG (preferred)
  - PNG (fallback)

## Style System

- Style type: (outline / solid / duotone)
- Stroke weight: (e.g., 2px on a 24px grid)
- Corner radius: (consistent)
- Fill rules:
- Color usage:
  - Default: single color, transparent background
  - Optional accent: one secondary color max
- Do not include any text.

## Icon List

List each icon with a single purpose.

1. Icon ID:
   - Label (human):
   - Meaning:
   - Must show:
   - Must avoid:
   - Primary placement:

## Per-icon Prompt Bundle

For each Icon ID, output:

- **Prompt**:
- **Negative / Guardrails**:
  - no text, no letters, no numbers
  - no gradients unless specified
  - no shadows unless specified
  - transparent background or plain white background
- **Consistency notes**:
  - stroke weight
  - corner radius
  - visual metaphor

## Export Notes

- If generated as raster, trace to SVG for crisp scaling.
- Keep padding consistent (safe area).

## Publish Pack

For each Icon ID, output:

- File name:
  - icon-[name]-24.svg
  - icon-[name]-48.svg
  - icon-[name]-96.svg
- Alt text (if used inline as image):
- Title (optional):
