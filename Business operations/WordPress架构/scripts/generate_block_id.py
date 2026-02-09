#!/usr/bin/env python3
"""
GreenShift Block ID Generator

生成符合 GreenShift 规范的唯一区块 ID
格式: gsbp-XXXXXXX (7位随机字符)
"""

import random
import string
import sys

def generate_block_id(count=1):
    """
    生成 GreenShift 区块 ID
    
    Args:
        count: 生成 ID 的数量（默认 1）
    
    Returns:
        list: ID 列表
    """
    ids = []
    chars = string.ascii_lowercase + string.digits
    
    for _ in range(count):
        # 生成 7 位随机字符
        random_part = ''.join(random.choices(chars, k=7))
        block_id = f"gsbp-{random_part}"
        ids.append(block_id)
    
    return ids

def main():
    # 解析命令行参数
    count = 1
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
            if count < 1 or count > 100:
                print("错误：数量必须在 1-100 之间")
                sys.exit(1)
        except ValueError:
            print("错误：请提供有效的数字")
            print("用法: python generate_block_id.py [数量]")
            sys.exit(1)
    
    # 生成 ID
    ids = generate_block_id(count)
    
    # 输出
    if count == 1:
        print(ids[0])
    else:
        for i, block_id in enumerate(ids, 1):
            print(f"{i}. {block_id}")

if __name__ == "__main__":
    main()
