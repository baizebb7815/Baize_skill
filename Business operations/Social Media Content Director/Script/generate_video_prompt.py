format_output.py#!/usr/bin/env python3
"""
AI Video Prompt Generator for Social Media Content
Generates Sora/Veo-compatible video prompts with style validation
"""

import json
import sys
from typing import Dict, List, Optional


class VideoPromptGenerator:
    """Generate AI video prompts following locked style guidelines"""
    
    STYLE_KEYWORDS = {
        'required': [
            'POV', 'first-person', 'hands', 'realistic', 
            'semi-professional smartphone'
        ],
        'lighting': [
            'natural daylight', 'soft ambient', 'window light',
            'indoor lighting', 'warm overhead'
        ],
        'camera': [
            'static camera', 'slow push-in', 'slight handheld',
            'minimal movement', 'no complex movement'
        ],
        'forbidden': [
            'face', 'person smiling', 'cinematic', 'dramatic lighting',
            'gimbal', 'drone shot', 'studio lighting'
        ]
    }
    
    SHOT_TEMPLATES = {
        'installation': {
            'wall_marking': "POV downward angle showing hands holding {tool} against a {wall_color} {room_type} wall. Fingers mark where the mounting bracket will go. Minimal camera movement, slight natural handheld shake. {lighting}. Semi-pro smartphone look, natural skin texture on hands.",
            
            'drilling': "Close-up POV of hands operating a cordless drill, driving a screw into {wall_type} with a {bracket_description} mounting bracket. Slight camera shake from drill vibration, very realistic and organic feel. {lighting}. Focus on hands and drill, blurred background. Smartphone aesthetic, not cinematic.",
            
            'hanging': "POV shot from installer's perspective, looking at hands lifting a {sign_description} LED sign and carefully sliding it onto a wall-mounted bracket. Both hands visible, guiding the sign into place with precision. {room_description} background, {lighting}. Static camera with slow push-in toward the sign as it settles. Realistic, semi-professional smartphone video style.",
            
            'plugging_in': "Extreme close-up POV of hands holding a {plug_color} power adapter plug, inserting it into a wall outlet below the newly mounted LED sign. Fingers carefully align the prongs and push the plug in. Shallow depth of field, focus on the plug and outlet. {lighting}. Static camera.",
            
            'activation': "POV medium shot of a {sign_color} LED neon sign reading \"{sign_text}\" mounted on a {wall_description}. The sign suddenly illuminates with {led_color} LED glow, creating soft diffused light. Hands visible at bottom of frame, one finger pulling away from an inline switch. {lighting}. Slight camera pull-back to reveal the glowing sign. Realistic smartphone footage, not cinematic."
        },
        
        'unboxing': {
            'opening_box': "POV first-person view looking down at hands opening a cardboard shipping box on a {surface_description}. Hands lift the cardboard flaps to reveal a neon-style LED sign wrapped in protective bubble wrap. {lighting}. Semi-professional smartphone aesthetic, realistic home setting. Static camera, no movement.",
            
            'unwrapping': "Close-up POV shot of hands carefully peeling bubble wrap off an LED neon sign on a {surface_description}. Fingers gently unwrap the protective film, revealing the smooth acrylic surface. {led_color} LED glow begins to show through translucent material. {lighting}. Realistic texture on hands and materials."
        },
        
        'context': {
            'room_static': "Static wide shot of a {room_style} {room_type} with a {sign_color} LED sign reading \"{sign_text}\" mounted {sign_location}. The sign glows softly in a {room_lighting} room, casting gentle light on the {wall_color} wall. {room_details}. {lighting}. No people, no movement. Realistic residential photography style, smartphone camera aesthetic.",
            
            'day_night_day': "Static shot of a {sign_color} LED sign reading \"{sign_text}\" on a {wall_color} wall in a bright, naturally lit room. {time_of_day} sunlight streaming through window. The sign is visible but subtle, blending with the clean, modern decor. Realistic home interior, smartphone camera style.",
            
            'day_night_night': "Same exact framing and angle as previous shot, now at night. The room is dark except for the {sign_color} LED sign \"{sign_text}\" glowing brightly on the {wall_color} wall, creating a warm ambiance. Soft {led_color} light reflects on surrounding wall. Realistic nighttime indoor lighting, smartphone camera aesthetic."
        },
        
        'detail': {
            'cleaning': "Close-up POV of a hand holding a {cloth_color} microfiber cloth, gently wiping the surface of an LED neon sign. Fingers move smoothly across the acrylic, removing dust. The sign is unplugged and not illuminated. {lighting}. Realistic skin texture on hand, fabric texture on cloth. Semi-professional smartphone closeup, slightly shallow depth of field.",
            
            'adjusting': "POV shot from directly in front of a mounted LED sign. Two hands visible from below, reaching up to gently adjust the sign's angle. Fingers press lightly on the sign's edge, tilting it slightly to level it perfectly. {wall_description} background, {lighting}. Static camera, focus on the hands and sign interaction. Realistic, natural movement.",
            
            'led_glow': "Extreme macro close-up of an illuminated LED neon sign, focusing on the {led_color} glow diffusing through frosted acrylic tubing. Camera slowly pushes in on the glowing surface, revealing the smooth, even light distribution. No hands, no people. Shallow depth of field with soft bokeh in background. Realistic lighting, semi-professional smartphone macro style."
        },
        
        'bts': {
            'assembly': "POV overhead shot of hands assembling an LED sign on a clean workbench. Fingers connect thin LED strip wiring to a small power driver board, securing with wire connectors. Tools scattered nearby: {tools_list}. Bright workshop lighting from overhead fluorescent. Focus on hands and components, realistic work environment. Semi-pro smartphone look, slight handheld movement.",
            
            'testing': "POV shot of hands holding a completed LED sign, plugging it into a power strip on a workshop table. The sign illuminates with bright even glow. Hand moves across the sign surface, visually inspecting for defects. Bright workspace lighting, clean industrial setting. Realistic smartphone video, slight natural camera movement as person inspects."
        }
    }
    
    def __init__(self):
        self.generated_prompts = []
    
    def validate_style(self, prompt: str) -> tuple[bool, List[str]]:
        """Validate prompt follows style guidelines"""
        issues = []
        
        # Check for forbidden keywords
        for keyword in self.STYLE_KEYWORDS['forbidden']:
            if keyword.lower() in prompt.lower():
                issues.append(f"❌ Forbidden keyword detected: '{keyword}'")
        
        # Check for required elements
        has_pov = any(kw in prompt.lower() for kw in ['pov', 'first-person'])
        if not has_pov:
            issues.append("⚠️ Missing POV specification")
        
        has_lighting = any(kw in prompt.lower() for kw in self.STYLE_KEYWORDS['lighting'])
        if not has_lighting:
            issues.append("⚠️ Missing lighting description")
        
        is_valid = len(issues) == 0
        return is_valid, issues
    
    def generate_shot(
        self, 
        shot_category: str, 
        shot_type: str, 
        variables: Dict[str, str],
        duration: int = 5
    ) -> Dict:
        """Generate a single shot prompt"""
        
        if shot_category not in self.SHOT_TEMPLATES:
            raise ValueError(f"Unknown category: {shot_category}")
        
        if shot_type not in self.SHOT_TEMPLATES[shot_category]:
            raise ValueError(f"Unknown shot type: {shot_type}")
        
        template = self.SHOT_TEMPLATES[shot_category][shot_type]
        
        # Set default lighting if not provided
        if 'lighting' not in variables:
            variables['lighting'] = "Natural daylight through window, soft ambient indoor lighting"
        
        try:
            prompt = template.format(**variables)
        except KeyError as e:
            raise ValueError(f"Missing required variable: {e}")
        
        # Add duration
        prompt += f" {duration} seconds."
        
        # Validate
        is_valid, issues = self.validate_style(prompt)
        
        return {
            'prompt': prompt,
            'category': shot_category,
            'type': shot_type,
            'duration': duration,
            'valid': is_valid,
            'issues': issues,
            'variables_used': variables
        }
    
    def generate_sequence(
        self, 
        sequence_name: str,
        shots: List[Dict]
    ) -> Dict:
        """Generate a sequence of shots"""
        
        generated_shots = []
        total_duration = 0
        all_valid = True
        
        for shot_spec in shots:
            shot = self.generate_shot(
                shot_category=shot_spec['category'],
                shot_type=shot_spec['type'],
                variables=shot_spec.get('variables', {}),
                duration=shot_spec.get('duration', 5)
            )
            generated_shots.append(shot)
            total_duration += shot['duration']
            
            if not shot['valid']:
                all_valid = False
        
        return {
            'sequence_name': sequence_name,
            'shots': generated_shots,
            'total_duration': total_duration,
            'shot_count': len(generated_shots),
            'all_valid': all_valid
        }


def main():
    """Example usage and CLI interface"""
    
    generator = VideoPromptGenerator()
    
    # Example: Installation video sequence
    installation_sequence = [
        {
            'category': 'installation',
            'type': 'wall_marking',
            'variables': {
                'tool': 'a pencil and small bubble level',
                'wall_color': 'clean white',
                'room_type': 'bedroom',
                'lighting': 'Soft afternoon sunlight from nearby window'
            },
            'duration': 4
        },
        {
            'category': 'installation',
            'type': 'drilling',
            'variables': {
                'wall_type': 'white drywall',
                'bracket_description': 'small black metal',
                'lighting': 'Workshop lighting, natural daylight mixed with overhead bulb'
            },
            'duration': 5
        },
        {
            'category': 'installation',
            'type': 'hanging',
            'variables': {
                'sign_description': 'medium-sized pink',
                'room_description': 'Clean living room wall',
                'lighting': 'Soft natural light from window to the right'
            },
            'duration': 6
        },
        {
            'category': 'installation',
            'type': 'plugging_in',
            'variables': {
                'plug_color': 'white',
                'lighting': 'Natural indoor lighting'
            },
            'duration': 3
        },
        {
            'category': 'installation',
            'type': 'activation',
            'variables': {
                'sign_color': 'white',
                'sign_text': 'GOOD VIBES',
                'wall_description': 'light gray bedroom wall',
                'led_color': 'warm white',
                'lighting': 'Natural evening light fading in room, sign becomes focal point'
            },
            'duration': 5
        }
    ]
    
    result = generator.generate_sequence(
        sequence_name="Installation Demo - 'GOOD VIBES' Sign",
        shots=installation_sequence
    )
    
    # Output results
    print(f"\n{'='*70}")
    print(f"SEQUENCE: {result['sequence_name']}")
    print(f"Total Duration: {result['total_duration']} seconds")
    print(f"Shot Count: {result['shot_count']}")
    print(f"All Valid: {'✅ Yes' if result['all_valid'] else '❌ No'}")
    print(f"{'='*70}\n")
    
    for i, shot in enumerate(result['shots'], 1):
        print(f"\n📹 SHOT {i}: {shot['type'].replace('_', ' ').title()}")
        print(f"Duration: {shot['duration']}s")
        print(f"\nPrompt:")
        print(f"{shot['prompt']}")
        
        if shot['issues']:
            print(f"\n⚠️ Style Issues:")
            for issue in shot['issues']:
                print(f"  {issue}")
        else:
            print(f"\n✅ Style validated")
        
        print(f"\n{'-'*70}")
    
    # Export to JSON
    output_file = 'generated_prompts.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    print(f"\n📄 Prompts exported to: {output_file}\n")


if __name__ == '__main__':
    main()