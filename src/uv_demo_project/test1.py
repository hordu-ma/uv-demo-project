#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
打印圣诞树的Python程序
"""


def print_christmas_tree(height=7):
    """
    打印一棵指定高度的圣诞树
    
    Args:
        height (int): 圣诞树的高度，默认为7层
    """
    # 打印树冠
    for i in range(height):
        # 打印空格（居中对齐）
        spaces = ' ' * (height - i - 1)
        # 打印星号
        stars = '*' * (2 * i + 1)
        print(f"{spaces}{stars}")
    
    # 打印树干
    trunk_height = max(2, height // 3)
    trunk_width = max(1, height // 4)
    
    for _ in range(trunk_height):
        trunk_spaces = ' ' * (height - trunk_width // 2 - 1)
        trunk_stars = '*' * trunk_width
        print(f"{trunk_spaces}{trunk_stars}")


def print_decorated_tree(height=7):
    """
    打印装饰的圣诞树
    
    Args:
        height (int): 圣诞树的高度，默认为7层
    """
    import random
    
    decorations = ['O', '@', '+', '&', '%']
    
    print("🎄 装饰版圣诞树 🎄")
    print()
    
    # 打印树冠
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        line = ""
        
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:
                line += '*'
            elif random.random() < 0.3:  # 30% 概率添加装饰
                line += random.choice(decorations)
            else:
                line += '*'
        
        print(f"{spaces}{line}")
    
    # 打印树干
    trunk_height = max(2, height // 3)
    trunk_width = max(1, height // 4)
    
    for _ in range(trunk_height):
        trunk_spaces = ' ' * (height - trunk_width // 2 - 1)
        trunk_stars = '|' * trunk_width
        print(f"{trunk_spaces}{trunk_stars}")
    
    print("\n🎁 圣诞快乐！🎁")


if __name__ == "__main__":
    print("🎄 简单圣诞树 🎄")
    print()
    print_christmas_tree()
    
    print("\n" + "="*20 + "\n")
    
    print_decorated_tree()
