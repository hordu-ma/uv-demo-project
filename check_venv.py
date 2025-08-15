#!/usr/bin/env python
"""
uv 虚拟环境状态检查脚本
用于验证虚拟环境是否已激活以及相关环境信息
"""

import os
import sys
import subprocess
from pathlib import Path


def check_venv_status():
    """检查虚拟环境状态"""
    print("=" * 60)
    print("虚拟环境状态检查")
    print("=" * 60)
    
    # 1. 检查 VIRTUAL_ENV 环境变量
    virtual_env = os.environ.get('VIRTUAL_ENV')
    if virtual_env:
        print(f"✅ 虚拟环境已激活")
        print(f"   路径: {virtual_env}")
    else:
        print("❌ 虚拟环境未激活 (VIRTUAL_ENV 环境变量未设置)")
    
    # 2. 检查 Python 解释器路径
    print(f"\nPython 解释器路径:")
    print(f"   sys.executable: {sys.executable}")
    print(f"   sys.prefix: {sys.prefix}")
    
    # 3. 检查是否在虚拟环境中
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    
    if in_venv:
        print(f"✅ 正在虚拟环境中运行")
    else:
        # 检查是否是 uv run 运行
        if '.venv' in sys.executable:
            print(f"✅ 通过 uv run 在虚拟环境中运行")
        else:
            print(f"⚠️  不在虚拟环境中运行")
    
    # 4. 检查项目中的 .venv 目录
    venv_path = Path.cwd() / '.venv'
    if venv_path.exists():
        print(f"\n📁 项目虚拟环境目录存在: {venv_path}")
        
        # 检查虚拟环境的 Python 版本
        venv_python = venv_path / 'bin' / 'python'
        if venv_python.exists():
            try:
                result = subprocess.run(
                    [str(venv_python), '--version'],
                    capture_output=True, text=True
                )
                print(f"   虚拟环境 Python 版本: {result.stdout.strip()}")
            except Exception as e:
                print(f"   无法获取虚拟环境 Python 版本: {e}")
    else:
        print(f"\n❌ 项目虚拟环境目录不存在: {venv_path}")
    
    # 5. 检查 pip 包的安装位置
    print(f"\n包安装位置:")
    print(f"   site-packages: {', '.join(sys.path[:3])}")
    
    # 6. 建议
    print("\n" + "=" * 60)
    print("建议的最佳实践:")
    print("=" * 60)
    
    if not virtual_env and venv_path.exists():
        print("🔸 激活虚拟环境:")
        print("   source .venv/bin/activate")
        print("\n🔸 或使用 uv run 命令 (推荐):")
        print("   uv run python your_script.py")
        print("   uv run pytest")
        print("   uv run pip list")
    elif not venv_path.exists():
        print("🔸 创建虚拟环境:")
        print("   uv venv")
        print("\n🔸 然后安装依赖:")
        print("   uv pip install -r requirements.txt")
        print("   # 或")
        print("   uv sync  # 如果有 pyproject.toml")
    else:
        print("✅ 虚拟环境已正确配置并激活")


def show_uv_commands():
    """显示常用的 uv 命令"""
    print("\n" + "=" * 60)
    print("uv 常用命令")
    print("=" * 60)
    
    commands = {
        "创建虚拟环境": "uv venv",
        "激活虚拟环境": "source .venv/bin/activate",
        "在虚拟环境中运行命令": "uv run <command>",
        "安装包": "uv pip install <package>",
        "同步依赖": "uv sync",
        "添加依赖": "uv add <package>",
        "移除依赖": "uv remove <package>",
        "列出已安装的包": "uv pip list",
        "显示项目信息": "uv tree",
    }
    
    for desc, cmd in commands.items():
        print(f"🔹 {desc:20} : {cmd}")


if __name__ == "__main__":
    check_venv_status()
    show_uv_commands()
