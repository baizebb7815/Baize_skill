# Reference Image Remake (copyright-safe)

Use this when the user provides a reference image and asks to recreate it.

## Rules

- Do not replicate 1:1. Preserve only general style cues.
- Make the output clearly original by changing at least 3 of these:
  - subject (type, shape, or key attribute)
  - composition (angle, framing, lens)
  - environment (location, background elements)
  - color palette (primary and accent colors)
  - lighting (time of day, softness, direction)
  - props (supporting objects)
- Remove any logos, trademarks, and text.
- If the image contains a recognizable person, do not attempt to recreate that person.

## Reverse analysis checklist (write as compact bullets)

- Theme:
- Primary subject:
- Secondary elements:
- Style: (photorealistic / documentary / cinematic / illustration)
- Composition: (rule of thirds, symmetry, leading lines, negative space)
- Camera: (focal length, depth of field, aperture look)
- Lighting: (natural/studio, key direction, softness, shadows)
- Color tone: (warm/cool, saturation, contrast)
- Materials: (surface texture, reflectivity)
- Background: (clean, busy, bokeh, gradient)
- Any in-image text or brand marks: (remove)

## Output requirement

Return JSON only. No prose outside JSON.

### JSON schema

{
  "task": "reference_remake",
  "policy": {
    "goal": "copyright_safe_remake",
    "do_not": [
      "no_1_to_1_replication",
      "no_logos_or_trademarks",
      "no_in_image_text"
    ],
    "deviation_plan": {
      "changed_elements": ["composition", "environment", "color_palette"],
      "notes": ""
    }
  },
  "analysis": {
    "theme": "",
    "style": "",
    "composition": "",
    "lighting": "",
    "color_tone": "",
    "materials": "",
    "details": [""]
  },
  "generation": {
    "style_definition": {
      "primary_style": "photorealistic",
      "rendering_quality": "high-resolution, detailed",
      "textures": "authentic material properties",
      "lighting_style": "natural"
    },
    "technical_specs": {
      "aspect_ratio": "16:9",
      "resolution": "4k",
      "camera": {
        "focal_length": "35mm",
        "depth_of_field": "moderate",
        "aperture_look": "f/2.8"
      }
    },
    "composition_controls": {
      "perspective": "natural human vision",
      "framing": "rule of thirds",
      "subject_placement": "balanced"
    },
    "environmental_factors": {
      "time": "dusk",
      "weather": "clear",
      "atmosphere": "subtle haze"
    },
    "prompt": {
      "prompt": "",
      "negative_prompt": "low quality, watermark, text overlay, blurry, artifacts, distorted, ugly, bad proportions, out of frame, jagged edges"
    }
  }
}

## Enhancement mode (owned image only)

If the user asks to enhance their own low-res image, keep everything the same and only improve clarity.

Return JSON only with:

- task: "image_enhancement"
- instructions focused on: upscaling, sharpening edges, denoise, preserve colors, preserve composition
