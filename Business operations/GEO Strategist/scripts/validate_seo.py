#!/usr/bin/env python3
"""
SEO Validation Script for BASIS SIGN Pages

Checks for:
- Meta tags completeness and length
- H1 uniqueness and optimization
- Keyword density
- Image alt text
- Readability
"""

import re
import sys
from pathlib import Path
from bs4 import BeautifulSoup
from collections import Counter

class SEOValidator:
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')
        self.errors = []
        self.warnings = []
        self.passed = []
        
    def validate_all(self):
        """Run all validation checks"""
        self.check_title_tag()
        self.check_meta_description()
        self.check_h1_tags()
        self.check_heading_hierarchy()
        self.check_images()
        self.check_keyword_density()
        self.check_internal_links()
        
        return self.generate_report()
    
    def check_title_tag(self):
        """Validate title tag"""
        title = self.soup.find('title')
        
        if not title:
            self.errors.append("❌ No <title> tag found")
            return
        
        title_text = title.get_text().strip()
        title_length = len(title_text)
        
        if title_length == 0:
            self.errors.append("❌ Title tag is empty")
        elif title_length < 30:
            self.warnings.append(f"⚠️  Title too short ({title_length} chars, recommend 50-60)")
        elif title_length > 60:
            self.warnings.append(f"⚠️  Title too long ({title_length} chars, recommend 50-60)")
        else:
            self.passed.append(f"✅ Title tag length optimal ({title_length} chars)")
        
        # Check if title includes brand
        if "BASIS SIGN" not in title_text:
            self.warnings.append("⚠️  Title doesn't include brand name 'BASIS SIGN'")
        else:
            self.passed.append("✅ Title includes brand name")
    
    def check_meta_description(self):
        """Validate meta description"""
        meta_desc = self.soup.find('meta', attrs={'name': 'description'})
        
        if not meta_desc or not meta_desc.get('content'):
            self.errors.append("❌ No meta description found")
            return
        
        desc_text = meta_desc['content'].strip()
        desc_length = len(desc_text)
        
        if desc_length == 0:
            self.errors.append("❌ Meta description is empty")
        elif desc_length < 120:
            self.warnings.append(f"⚠️  Meta description too short ({desc_length} chars, recommend 150-160)")
        elif desc_length > 160:
            self.warnings.append(f"⚠️  Meta description too long ({desc_length} chars, recommend 150-160)")
        else:
            self.passed.append(f"✅ Meta description length optimal ({desc_length} chars)")
        
        # Check for CTA in description
        cta_keywords = ['get', 'request', 'design', 'shop', 'contact', 'call', 'order']
        if any(keyword in desc_text.lower() for keyword in cta_keywords):
            self.passed.append("✅ Meta description includes CTA")
        else:
            self.warnings.append("⚠️  Meta description doesn't include a CTA")
    
    def check_h1_tags(self):
        """Validate H1 tags"""
        h1_tags = self.soup.find_all('h1')
        
        if len(h1_tags) == 0:
            self.errors.append("❌ No H1 tag found")
        elif len(h1_tags) > 1:
            self.errors.append(f"❌ Multiple H1 tags found ({len(h1_tags)}), should be exactly 1")
        else:
            h1_text = h1_tags[0].get_text().strip()
            h1_length = len(h1_text)
            
            if h1_length < 20:
                self.warnings.append(f"⚠️  H1 too short ({h1_length} chars, recommend 40-60)")
            elif h1_length > 70:
                self.warnings.append(f"⚠️  H1 too long ({h1_length} chars, recommend 40-60)")
            else:
                self.passed.append(f"✅ H1 length optimal ({h1_length} chars)")
            
            self.passed.append(f"✅ Exactly one H1 found: '{h1_text[:50]}...'")
    
    def check_heading_hierarchy(self):
        """Check heading structure H1 > H2 > H3"""
        h1_count = len(self.soup.find_all('h1'))
        h2_count = len(self.soup.find_all('h2'))
        h3_count = len(self.soup.find_all('h3'))
        
        if h2_count == 0:
            self.warnings.append("⚠️  No H2 tags found - add section headers")
        elif h2_count < 3:
            self.warnings.append(f"⚠️  Only {h2_count} H2 tags - consider adding more sections")
        else:
            self.passed.append(f"✅ Good heading structure: H1({h1_count}), H2({h2_count}), H3({h3_count})")
    
    def check_images(self):
        """Validate image alt text"""
        images = self.soup.find_all('img')
        
        if len(images) == 0:
            self.warnings.append("⚠️  No images found")
            return
        
        missing_alt = 0
        empty_alt = 0
        short_alt = 0
        
        for img in images:
            alt = img.get('alt', '')
            
            if not alt:
                missing_alt += 1
            elif len(alt.strip()) == 0:
                empty_alt += 1
            elif len(alt.strip()) < 10:
                short_alt += 1
        
        if missing_alt > 0:
            self.errors.append(f"❌ {missing_alt} images missing alt attribute")
        if empty_alt > 0:
            self.warnings.append(f"⚠️  {empty_alt} images have empty alt text")
        if short_alt > 0:
            self.warnings.append(f"⚠️  {short_alt} images have very short alt text (<10 chars)")
        
        if missing_alt == 0 and empty_alt == 0:
            self.passed.append(f"✅ All {len(images)} images have alt text")
    
    def check_keyword_density(self):
        """Check keyword density (basic)"""
        # Get all text content
        text = self.soup.get_text().lower()
        words = re.findall(r'\b\w+\b', text)
        
        if len(words) < 300:
            self.warnings.append(f"⚠️  Content is short ({len(words)} words, recommend 800+ for product pages)")
        else:
            self.passed.append(f"✅ Good content length ({len(words)} words)")
        
        # Check for key signage terms
        signage_keywords = [
            'channel letter', 'led', 'neon', 'sign', 'illuminated',
            'install', 'basis sign', 'certified', 'compliant'
        ]
        
        keyword_found = False
        for keyword in signage_keywords:
            if keyword in text:
                keyword_found = True
                # Calculate density
                count = text.count(keyword)
                density = (count / len(words)) * 100
                
                if density > 3:
                    self.warnings.append(f"⚠️  '{keyword}' density high ({density:.2f}%), may seem spammy")
        
        if keyword_found:
            self.passed.append("✅ Relevant keywords present")
    
    def check_internal_links(self):
        """Check for internal linking"""
        links = self.soup.find_all('a', href=True)
        internal_links = [link for link in links if not link['href'].startswith('http')]
        
        if len(internal_links) == 0:
            self.warnings.append("⚠️  No internal links found - add links to related pages")
        else:
            self.passed.append(f"✅ {len(internal_links)} internal links found")
        
        # Check for descriptive anchor text
        generic_anchors = ['click here', 'read more', 'here', 'this', 'link']
        generic_count = 0
        
        for link in links:
            anchor_text = link.get_text().strip().lower()
            if anchor_text in generic_anchors:
                generic_count += 1
        
        if generic_count > 0:
            self.warnings.append(f"⚠️  {generic_count} links use generic anchor text (e.g., 'click here')")
    
    def generate_report(self):
        """Generate validation report"""
        report = []
        report.append("=" * 60)
        report.append("SEO VALIDATION REPORT")
        report.append("=" * 60)
        report.append("")
        
        if self.errors:
            report.append("🚨 ERRORS (Must Fix):")
            report.append("-" * 60)
            for error in self.errors:
                report.append(f"  {error}")
            report.append("")
        
        if self.warnings:
            report.append("⚠️  WARNINGS (Should Fix):")
            report.append("-" * 60)
            for warning in self.warnings:
                report.append(f"  {warning}")
            report.append("")
        
        if self.passed:
            report.append("✅ PASSED:")
            report.append("-" * 60)
            for passed in self.passed:
                report.append(f"  {passed}")
            report.append("")
        
        # Summary
        total_checks = len(self.errors) + len(self.warnings) + len(self.passed)
        score = (len(self.passed) / total_checks * 100) if total_checks > 0 else 0
        
        report.append("=" * 60)
        report.append(f"SCORE: {score:.1f}% ({len(self.passed)} passed, {len(self.warnings)} warnings, {len(self.errors)} errors)")
        report.append("=" * 60)
        
        return "\n".join(report)


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_seo.py <html_file>")
        sys.exit(1)
    
    html_file = Path(sys.argv[1])
    
    if not html_file.exists():
        print(f"Error: File '{html_file}' not found")
        sys.exit(1)
    
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    validator = SEOValidator(html_content)
    report = validator.validate_all()
    
    print(report)
    
    # Exit with error code if there are errors
    if validator.errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
