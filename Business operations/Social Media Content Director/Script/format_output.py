#!/usr/bin/env python3
"""
Video Content Output Formatter
Standardizes video concept outputs for consistency
"""

import json
from typing import Dict, List, Optional
from datetime import datetime


class VideoOutputFormatter:
    """Format video concepts into standardized deliverable format"""
    
    PLATFORM_SPECS = {
        'instagram': {
            'name': 'Instagram Reels',
            'aspect_ratio': '9:16',
            'ideal_length': '15-30s',
            'max_length': '90s',
            'style_notes': 'Trendy audio, fast pacing, casual tone'
        },
        'tiktok': {
            'name': 'TikTok',
            'aspect_ratio': '9:16',
            'ideal_length': '7-20s',
            'max_length': '60s',
            'style_notes': 'Raw, authentic, conversational'
        },
        'pinterest': {
            'name': 'Pinterest',
            'aspect_ratio': '2:3',
            'ideal_length': '20-30s',
            'max_length': '60s',
            'style_notes': 'Aspirational, clean, informative'
        },
        'youtube_shorts': {
            'name': 'YouTube Shorts',
            'aspect_ratio': '9:16',
            'ideal_length': '15-45s',
            'max_length': '60s',
            'style_notes': 'Slightly polished, educational'
        }
    }
    
    def __init__(self):
        self.output = {}
    
    def format_concept(
        self,
        title: str,
        platform: str,
        target_audience: str,
        video_length: str,
        core_takeaway: str,
        content_type: str = None
    ) -> Dict:
        """Format video concept section"""
        
        platform_info = self.PLATFORM_SPECS.get(platform.lower(), {})
        
        return {
            'title': title,
            'platform': platform_info.get('name', platform),
            'platform_specs': {
                'aspect_ratio': platform_info.get('aspect_ratio', 'N/A'),
                'recommended_length': platform_info.get('ideal_length', video_length)
            },
            'target_audience': target_audience,
            'video_length': video_length,
            'core_takeaway': core_takeaway,
            'content_type': content_type
        }
    
    def format_shot_list(self, shots: List[Dict]) -> str:
        """Format shot list as markdown table"""
        
        table = "| Shot | Visual Description | Camera Logic | On-Screen Text | Duration |\n"
        table += "|------|-------------------|--------------|----------------|----------|\n"
        
        for i, shot in enumerate(shots, 1):
            visual = shot.get('visual', '').replace('|', '\\|')
            camera = shot.get('camera', '').replace('|', '\\|')
            text = shot.get('text', '').replace('|', '\\|')
            duration = shot.get('duration', '')
            
            table += f"| {i} | {visual} | {camera} | {text} | {duration} |\n"
        
        return table
    
    def format_script(
        self,
        hook: str,
        body: List[str],
        cta: str
    ) -> Dict:
        """Format script with hook, body, and CTA"""
        
        return {
            'hook': {
                'timing': '0-3s',
                'text': hook
            },
            'body': [
                {
                    'section': i+1,
                    'text': section
                } for i, section in enumerate(body)
            ],
            'cta': {
                'timing': 'Final 3-5s',
                'text': cta
            }
        }
    
    def format_ai_prompt(
        self,
        prompts: List[str],
        style_notes: Optional[str] = None
    ) -> Dict:
        """Format AI video generation prompts"""
        
        return {
            'model_compatibility': ['Sora 2', 'Veo 3', 'Similar AI video generators'],
            'prompts': prompts,
            'style_enforcement': style_notes or "POV, hands-only, semi-professional smartphone aesthetic, natural lighting",
            'quality_settings': {
                'resolution': 'HD (1080p minimum)',
                'fps': '24-30fps',
                'aspect_ratio': 'Match platform spec'
            }
        }
    
    def format_caption(
        self,
        caption_text: str,
        hashtags: List[str],
        cta_text: Optional[str] = None
    ) -> Dict:
        """Format social media caption"""
        
        return {
            'caption': caption_text,
            'hashtags': hashtags,
            'cta': cta_text,
            'tone': 'Casual, American, conversational',
            'character_count': len(caption_text),
            'full_post': f"{caption_text}\n\n{' '.join(['#' + tag for tag in hashtags])}" + (f"\n\n{cta_text}" if cta_text else "")
        }
    
    def generate_complete_output(
        self,
        concept: Dict,
        shots: List[Dict],
        script: Dict,
        prompts: List[str],
        caption: Dict,
        metadata: Optional[Dict] = None
    ) -> str:
        """Generate complete formatted output"""
        
        output = f"""
# {concept['title']}

---

## 🎬 Video Concept

**Platform:** {concept['platform']}
**Aspect Ratio:** {concept['platform_specs']['aspect_ratio']}
**Recommended Length:** {concept['platform_specs']['recommended_length']}
**Target Audience:** {concept['target_audience']}
**Video Length:** {concept['video_length']}
**Core Takeaway:** {concept['core_takeaway']}
"""
        
        if concept.get('content_type'):
            output += f"**Content Type:** {concept['content_type']}\n"
        
        output += "\n---\n\n## 🎥 Shot List / Storyboard\n\n"
        output += self.format_shot_list(shots)
        
        output += "\n---\n\n## 🧠 Script (Text Overlay / Voiceover)\n\n"
        output += f"**Hook ({script['hook']['timing']}):**\n{script['hook']['text']}\n\n"
        
        output += "**Body:**\n"
        for section in script['body']:
            output += f"{section['section']}. {section['text']}\n"
        
        output += f"\n**CTA ({script['cta']['timing']}):**\n{script['cta']['text']}\n"
        
        output += "\n---\n\n## 🛠️ AI Video Generation Prompts\n\n"
        output += f"**Model Compatibility:** {', '.join(['Sora 2', 'Veo 3', 'Similar AI video generators'])}\n\n"
        output += "**Style Enforcement:**\nPOV, hands-only, semi-professional smartphone aesthetic, natural lighting\n\n"
        
        output += "**Prompts:**\n\n"
        for i, prompt in enumerate(prompts, 1):
            output += f"**Shot {i} Prompt:**\n```\n{prompt}\n```\n\n"
        
        output += "---\n\n## 📲 Caption & Hashtags\n\n"
        output += f"**Caption:**\n{caption['caption']}\n\n"
        output += f"**Hashtags:**\n{' '.join(['#' + tag for tag in caption['hashtags']])}\n\n"
        
        if caption.get('cta'):
            output += f"**CTA:**\n{caption['cta']}\n\n"
        
        output += f"**Character Count:** {caption['character_count']}\n"
        output += f"**Tone:** {caption['tone']}\n"
        
        if metadata:
            output += "\n---\n\n## 📊 Metadata\n\n"
            for key, value in metadata.items():
                output += f"**{key}:** {value}\n"
        
        output += f"\n---\n\n*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"
        
        return output
    
    def export_json(self, data: Dict, filename: str):
        """Export data as JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def export_markdown(self, content: str, filename: str):
        """Export content as Markdown"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)


def example_usage():
    """Example of complete video output formatting"""
    
    formatter = VideoOutputFormatter()
    
    # Define concept
    concept = formatter.format_concept(
        title="Easy LED Sign Installation - No Electrician Needed",
        platform="instagram",
        target_audience="Homeowners (25-45), DIY enthusiasts, renters",
        video_length="23 seconds",
        core_takeaway="LED sign installation is quick, safe, and doesn't require professional help",
        content_type="Installation Demo (Type A1)"
    )
    
    # Define shots
    shots = [
        {
            'visual': 'Unopened shipping box on wooden floor',
            'camera': 'POV looking down, static',
            'text': 'You won\'t believe how easy this is',
            'duration': '3s'
        },
        {
            'visual': 'Hands opening box, revealing LED sign and mounting kit',
            'camera': 'POV closeup, static',
            'text': 'Everything included ✓',
            'duration': '5s'
        },
        {
            'visual': 'Hands marking wall with pencil and level',
            'camera': 'POV over shoulder, slight movement',
            'text': 'Mark your spot',
            'duration': '4s'
        },
        {
            'visual': 'Drilling mounting bracket into wall',
            'camera': 'POV closeup, camera shake from drill',
            'text': 'Quick install',
            'duration': '4s'
        },
        {
            'visual': 'Hands hanging sign on bracket',
            'camera': 'POV medium shot, slow push-in',
            'text': 'Slide it on',
            'duration': '4s'
        },
        {
            'visual': 'Sign illuminating on wall, pull-back reveal',
            'camera': 'POV to wide, slow pull-back',
            'text': 'Done in 3 minutes ✨',
            'duration': '3s'
        }
    ]
    
    # Define script
    script = formatter.format_script(
        hook="Installing a custom LED sign without an electrician? Watch this.",
        body=[
            "Everything you need comes in the box",
            "Mark your wall placement",
            "Mount the bracket (takes 2 minutes)",
            "Hang the sign and plug it in"
        ],
        cta="Save this for your next room makeover!"
    )
    
    # Define AI prompts
    prompts = [
        "POV first-person view looking down at hands opening a cardboard shipping box on a wooden floor. Hands lift the cardboard flaps to reveal a neon-style LED sign wrapped in protective bubble wrap. Natural window light from the left side, soft ambient indoor lighting. Semi-professional smartphone aesthetic, realistic home setting. Static camera, no movement. 3 seconds.",
        
        "Close-up POV of hands unwrapping bubble wrap to reveal a white LED neon sign on wooden floor. Natural daylight, realistic textures. Static camera. 5 seconds.",
        
        "POV downward angle showing hands holding a pencil and small bubble level against a clean white bedroom wall. Fingers mark a light pencil dot where the mounting bracket will go. Minimal camera movement, slight natural handheld shake. Soft afternoon sunlight from nearby window. 4 seconds.",
        
        "Close-up POV of hands operating a cordless drill, driving a screw into white drywall with a small black metal mounting bracket. Slight camera shake from drill vibration. Workshop lighting, natural daylight mixed with overhead bulb. Focus on hands and drill, blurred background. Smartphone aesthetic. 4 seconds.",
        
        "POV shot from installer's perspective, looking at hands lifting a medium-sized white LED sign and carefully sliding it onto a wall-mounted bracket. Both hands visible, guiding the sign into place. Clean bedroom wall background, soft natural light from window to the right. Static camera with slow push-in toward the sign as it settles. 4 seconds.",
        
        "POV medium shot of a white LED neon sign reading 'DREAM BIG' mounted on a light gray bedroom wall. The sign suddenly illuminates with warm white LED glow, creating soft diffused light. Hands visible at bottom of frame, one finger pulling away from switch. Natural evening light fading in room, sign becomes focal point. Slight camera pull-back to reveal the glowing sign. Realistic smartphone footage. 3 seconds."
    ]
    
    # Define caption
    caption = formatter.format_caption(
        caption_text="Who knew installing a custom LED sign could be THIS easy? 😍 No electrician, no hassle, no damage to your walls. Everything you need is in the box. Did this in under 5 minutes!",
        hashtags=['LEDsign', 'DIYhomedecor', 'apartmenttherapy', 'homerenovation', 'customsigns'],
        cta_text="👉 Tap to shop our collection"
    )
    
    # Generate complete output
    markdown_output = formatter.generate_complete_output(
        concept=concept,
        shots=shots,
        script=script,
        prompts=prompts,
        caption=caption,
        metadata={
            'Created By': 'Social Media Content Director Skill',
            'Review Status': 'Ready for approval',
            'Estimated Production Time': '2-3 hours (AI generation + editing)'
        }
    )
    
    # Export
    formatter.export_markdown(markdown_output, 'video_output_example.md')
    
    print("✅ Example video output generated!")
    print("📄 Saved to: video_output_example.md")
    print("\n" + "="*70)
    print(markdown_output)
    print("="*70)


if __name__ == '__main__':
    example_usage()