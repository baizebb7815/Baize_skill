#!/usr/bin/env python3
"""
GreenShift Block Validator

验证生成的 GreenShift 区块是否符合规范
"""

import re
import json
import sys
from typing import List, Tuple

class BlockValidator:
    def __init__(self):
        self.errors = []
        self.warnings = []
    
    def validate_file(self, filepath: str) -> Tuple[bool, List[str], List[str]]:
        """
        验证 HTML 文件中的 GreenShift 区块
        
        Returns:
            (is_valid, errors, warnings)
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            return False, [f"文件不存在: {filepath}"], []
        except Exception as e:
            return False, [f"读取文件错误: {str(e)}"], []
        
        return self.validate_content(content)
    
    def validate_content(self, content: str) -> Tuple[bool, List[str], List[str]]:
        """验证内容"""
        self.errors = []
        self.warnings = []
        
        # 查找所有 GreenShift 区块
        block_pattern = r'<!--\s*wp:greenshift-blocks/([a-zA-Z0-9_-]+)\s+(\{[\s\S]*?\})\s*-->'
        blocks = re.finditer(block_pattern, content, re.DOTALL)
        
        block_count = 0
        seen_ids = set()
        
        for match in blocks:
            block_count += 1
            block_type = match.group(1)
            json_str = match.group(2)
            
            # 验证 JSON
            try:
                block_data = json.loads(json_str)
            except json.JSONDecodeError as e:
                self.errors.append(f"区块 {block_count}: JSON 格式错误 - {str(e)}")
                continue
            
            # 验证必需字段
            self._validate_required_fields(block_type, block_data, block_count)
            
            # 验证 ID 格式
            self._validate_id(block_type, block_data, block_count, seen_ids)
            
            # 验证样式规范
            self._validate_styles(block_data, block_count)
            
            # 验证 type 字段
            self._validate_type(block_data, block_count)
        
        if block_count == 0:
            self.warnings.append("未找到任何 GreenShift 区块")
        
        is_valid = len(self.errors) == 0
        return is_valid, self.errors, self.warnings
    
    def _validate_required_fields(self, block_type: str, block_data: dict, block_num: int):
        """验证必需字段"""
        if 'id' not in block_data:
            self.errors.append(f"区块 {block_num}: 缺少 'id' 字段")
            return

        if block_type == 'element':
            if 'localId' not in block_data:
                self.errors.append(f"区块 {block_num}: element 缺少 'localId' 字段")
                return
            if block_data['id'] != block_data['localId']:
                self.errors.append(f"区块 {block_num}: element 的 'id' 和 'localId' 必须相同")
    
    def _validate_id(self, block_type: str, block_data: dict, block_num: int, seen_ids: set):
        """验证 ID 格式和唯一性"""
        if 'id' not in block_data:
            return
        
        block_id = block_data['id']
        
        if block_type == 'element':
            id_pattern = r'^gsbp-[a-z0-9]{7}$'
            if not re.match(id_pattern, block_id):
                self.errors.append(
                    f"区块 {block_num}: element ID '{block_id}' 格式不正确 "
                    f"(应为 gsbp-XXXXXXX，7位小写字母+数字)"
                )
        else:
            id_pattern = r'^gsbp-[a-z0-9-]{7,}$'
            if not re.match(id_pattern, block_id):
                self.warnings.append(
                    f"区块 {block_num}: 区块 {block_type} 的 ID '{block_id}' 格式不常见"
                )
        
        # 检查唯一性
        if block_id in seen_ids:
            self.errors.append(f"区块 {block_num}: ID '{block_id}' 重复")
        else:
            seen_ids.add(block_id)
    
    def _validate_styles(self, block_data: dict, block_num: int):
        """验证样式规范"""
        if 'styleAttributes' not in block_data:
            return
        
        styles = block_data['styleAttributes']
        
        # 检查是否使用了 camelCase
        for key in styles.keys():
            if '-' in key and not key.endswith('_hover') and not key.endswith('_focus'):
                self.errors.append(
                    f"区块 {block_num}: 样式属性 '{key}' 应使用 camelCase "
                    f"(如 backgroundColor 而非 background-color)"
                )
            
            # 检查响应式数组
            value = styles[key]
            if isinstance(value, list):
                if len(value) > 4:
                    self.warnings.append(
                        f"区块 {block_num}: 响应式数组 '{key}' 长度超过 4 "
                        f"(应为 [desktop, tablet, mobile, mobile_small])"
                    )
    
    def _validate_type(self, block_data: dict, block_num: int):
        """验证 type 字段"""
        if 'type' not in block_data:
            return
        
        block_type = block_data['type']
        valid_types = ['inner', 'text', 'no', 'image', 'empty', 'html', 'chart']
        
        if block_type not in valid_types:
            self.errors.append(
                f"区块 {block_num}: type '{block_type}' 无效 "
                f"(应为 {', '.join(valid_types)} 之一)"
            )
        
        # 检查 text type 是否有 textContent
        if block_type == 'text' and 'textContent' not in block_data:
            self.warnings.append(
                f"区块 {block_num}: type 为 'text' 但缺少 'textContent' 字段"
            )

def main():
    if len(sys.argv) < 2:
        print("用法: python validate_greenshift_block.py <文件路径>")
        print("示例: python validate_greenshift_block.py hero-section.html")
        sys.exit(1)
    
    filepath = sys.argv[1]
    validator = BlockValidator()
    is_valid, errors, warnings = validator.validate_file(filepath)
    
    # 输出结果
    print("=" * 60)
    print(f"验证文件: {filepath}")
    print("=" * 60)
    
    if errors:
        print("\n❌ 错误:")
        for error in errors:
            print(f"  - {error}")
    
    if warnings:
        print("\n⚠️  警告:")
        for warning in warnings:
            print(f"  - {warning}")
    
    if is_valid:
        print("\n✅ 验证通过！区块符合 GreenShift 规范。")
        sys.exit(0)
    else:
        print(f"\n❌ 验证失败！发现 {len(errors)} 个错误。")
        sys.exit(1)

if __name__ == "__main__":
    main()
