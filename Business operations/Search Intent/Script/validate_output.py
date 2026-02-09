#!/usr/bin/env python3
"""
Keyword Research Output Validator

Checks keyword research output for:
- Required table columns present
- B2B pain point coverage
- Decision stage balance
- Natural language phrasing
- Content angle specificity

Usage:
    python validate_output.py <path-to-markdown-file>
"""

import sys
import re
from typing import List, Dict, Tuple

class KeywordValidator:
    # Required B2B pain points that should be covered
    B2B_PAIN_POINTS = [
        "cost",
        "installation",
        "permit",
        "compliance",
        "reliability",
        "maintenance"
    ]
    
    # Decision stages
    DECISION_STAGES = ["awareness", "consideration", "decision"]
    
    # Required table columns
    REQUIRED_COLUMNS = [
        "audience",
        "decision stage",
        "pain point",
        "keyword",
        "search intent",
        "what",
        "content angle"
    ]
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.content = self._read_file()
        self.issues = []
        self.warnings = []
        self.stats = {
            'total_keywords': 0,
            'b2b_keywords': 0,
            'b2c_keywords': 0,
            'awareness': 0,
            'consideration': 0,
            'decision': 0
        }
    
    def _read_file(self) -> str:
        """Read the markdown file content"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"❌ Error: File not found: {self.file_path}")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Error reading file: {e}")
            sys.exit(1)
    
    def validate_table_structure(self) -> bool:
        """Check if markdown table exists and has required columns"""
        # Find markdown tables
        table_pattern = r'\|[^\n]+\|'
        tables = re.findall(table_pattern, self.content)
        
        if not tables:
            self.issues.append("No markdown table found in document")
            return False
        
        # Check first table row (header)
        header = tables[0].lower()
        
        missing_columns = []
        for col in self.REQUIRED_COLUMNS:
            if col not in header:
                missing_columns.append(col)
        
        if missing_columns:
            self.issues.append(f"Missing required columns: {', '.join(missing_columns)}")
            return False
        
        return True
    
    def extract_keywords(self) -> List[Dict]:
        """Extract keyword data from table rows"""
        keywords = []
        
        # Pattern to match table rows (excluding header and separator)
        lines = self.content.split('\n')
        in_table = False
        header_found = False
        
        for line in lines:
            if '|' not in line:
                in_table = False
                continue
            
            # Check if this is a header row
            if not header_found and any(col in line.lower() for col in self.REQUIRED_COLUMNS):
                header_found = True
                in_table = True
                continue
            
            # Skip separator row
            if re.match(r'\s*\|[\s\-:|]+\|\s*$', line):
                continue
            
            # Parse data rows
            if in_table and header_found:
                cells = [cell.strip() for cell in line.split('|')[1:-1]]  # Remove first and last empty cells
                
                if len(cells) >= 7:  # Minimum columns
                    keyword_data = {
                        'audience': cells[0],
                        'stage': cells[1],
                        'pain_point': cells[2],
                        'keyword': cells[3],
                        'intent': cells[4],
                        'user_wants': cells[5],
                        'content_angle': cells[6]
                    }
                    keywords.append(keyword_data)
        
        return keywords
    
    def validate_keywords(self, keywords: List[Dict]) -> None:
        """Validate keyword quality and coverage"""
        if not keywords:
            self.issues.append("No keywords found in table")
            return
        
        self.stats['total_keywords'] = len(keywords)
        
        b2b_pain_points_found = set()
        
        for idx, kw in enumerate(keywords, 1):
            # Count audience types
            if 'b2b' in kw['audience'].lower():
                self.stats['b2b_keywords'] += 1
            if 'b2c' in kw['audience'].lower():
                self.stats['b2c_keywords'] += 1
            
            # Count decision stages
            stage_lower = kw['stage'].lower()
            if 'awareness' in stage_lower:
                self.stats['awareness'] += 1
            elif 'consideration' in stage_lower:
                self.stats['consideration'] += 1
            elif 'decision' in stage_lower:
                self.stats['decision'] += 1
            
            # Check for natural language in keywords
            if self._is_keyword_stuffed(kw['keyword']):
                self.warnings.append(f"Row {idx}: Keyword may be keyword-stuffed: '{kw['keyword']}'")
            
            # Check content angle specificity
            if self._is_content_angle_vague(kw['content_angle']):
                self.warnings.append(f"Row {idx}: Content angle too vague: '{kw['content_angle']}'")
            
            # Track B2B pain points coverage
            if 'b2b' in kw['audience'].lower():
                for pain_point in self.B2B_PAIN_POINTS:
                    if pain_point in kw['pain_point'].lower() or pain_point in kw['keyword'].lower():
                        b2b_pain_points_found.add(pain_point)
        
        # Check B2B pain point coverage
        if self.stats['b2b_keywords'] > 0:
            missing_pain_points = set(self.B2B_PAIN_POINTS) - b2b_pain_points_found
            if missing_pain_points:
                self.warnings.append(f"B2B keywords missing coverage for: {', '.join(missing_pain_points)}")
    
    def _is_keyword_stuffed(self, keyword: str) -> bool:
        """Detect potentially keyword-stuffed phrases"""
        # Check for unnatural patterns
        patterns = [
            r'\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+',  # 6+ words without question words (may be stuffed)
        ]
        
        # Natural question words that indicate real search queries
        question_words = ['how', 'what', 'why', 'when', 'where', 'who', 'do', 'does', 'is', 'are', 'can']
        
        has_question_word = any(qw in keyword.lower() for qw in question_words)
        
        # If it's a long phrase without question words, might be stuffed
        word_count = len(keyword.split())
        if word_count > 6 and not has_question_word:
            return True
        
        return False
    
    def _is_content_angle_vague(self, content_angle: str) -> bool:
        """Detect vague content angle descriptions"""
        vague_terms = [
            'educational content',
            'informational post',
            'blog post about',
            'article on',
            'content about'
        ]
        
        content_lower = content_angle.lower()
        
        # Check if it's too short (less than 30 chars is likely too vague)
        if len(content_angle) < 30:
            return True
        
        # Check for vague terms
        for term in vague_terms:
            if term in content_lower:
                return True
        
        return False
    
    def check_stage_balance(self) -> None:
        """Check if decision stages are reasonably balanced"""
        total = self.stats['total_keywords']
        if total == 0:
            return
        
        awareness_pct = (self.stats['awareness'] / total) * 100
        consideration_pct = (self.stats['consideration'] / total) * 100
        decision_pct = (self.stats['decision'] / total) * 100
        
        # Ideal: Consideration 40-50%, Awareness 25-35%, Decision 25-35%
        if consideration_pct < 30:
            self.warnings.append(f"Low consideration stage coverage ({consideration_pct:.1f}%) - should be 40-50%")
        
        if awareness_pct > 50:
            self.warnings.append(f"High awareness stage coverage ({awareness_pct:.1f}%) - may be too broad")
        
        if decision_pct > 50:
            self.warnings.append(f"High decision stage coverage ({decision_pct:.1f}%) - may be too narrow")
    
    def run_validation(self) -> bool:
        """Run all validation checks"""
        print("🔍 Validating keyword research output...\n")
        
        # Check table structure
        if not self.validate_table_structure():
            return False
        
        # Extract and validate keywords
        keywords = self.extract_keywords()
        self.validate_keywords(keywords)
        self.check_stage_balance()
        
        return True
    
    def print_report(self) -> None:
        """Print validation report"""
        print("=" * 60)
        print("VALIDATION REPORT")
        print("=" * 60)
        
        # Statistics
        print("\n📊 Statistics:")
        print(f"  Total keywords: {self.stats['total_keywords']}")
        print(f"  B2B keywords: {self.stats['b2b_keywords']}")
        print(f"  B2C keywords: {self.stats['b2c_keywords']}")
        print(f"\n  Decision Stages:")
        print(f"    Awareness: {self.stats['awareness']} ({self._pct('awareness')}%)")
        print(f"    Consideration: {self.stats['consideration']} ({self._pct('consideration')}%)")
        print(f"    Decision: {self.stats['decision']} ({self._pct('decision')}%)")
        
        # Issues
        if self.issues:
            print("\n❌ CRITICAL ISSUES:")
            for issue in self.issues:
                print(f"  • {issue}")
        
        # Warnings
        if self.warnings:
            print("\n⚠️  WARNINGS:")
            for warning in self.warnings:
                print(f"  • {warning}")
        
        # Summary
        print("\n" + "=" * 60)
        if not self.issues and not self.warnings:
            print("✅ VALIDATION PASSED - No issues found!")
        elif self.issues:
            print("❌ VALIDATION FAILED - Please fix critical issues")
            return False
        else:
            print("⚠️  VALIDATION PASSED WITH WARNINGS - Review recommendations")
        print("=" * 60)
        
        return True
    
    def _pct(self, stage: str) -> str:
        """Calculate percentage for a decision stage"""
        total = self.stats['total_keywords']
        if total == 0:
            return "0.0"
        return f"{(self.stats[stage] / total * 100):.1f}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_output.py <path-to-markdown-file>")
        sys.exit(1)
    
    validator = KeywordValidator(sys.argv[1])
    
    if validator.run_validation():
        success = validator.print_report()
        sys.exit(0 if success else 1)
    else:
        validator.print_report()
        sys.exit(1)

if __name__ == "__main__":
    main()
