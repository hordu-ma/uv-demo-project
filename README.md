# uv-demo-project

使用 uv 初始化的 Python 项目示例。

## 功能特性

- 使用 uv 进行依赖管理
- Python 3.12 支持
- 预配置的开发工具：
  - pytest (测试)
  - black (代码格式化)
  - flake8 (代码检查)
- 标准的 Python 包结构
- 命令行入口点

## 快速开始

### 安装依赖

```bash
# 使用 uv 安装所有依赖（包括开发依赖）
uv sync --dev

# 或者使用 Makefile
make install
```

### 运行项目

```bash
# 直接运行主程序
uv run uv-demo-project

# 或者运行 main.py
python main.py

# 或者使用 Makefile
make run
```

### 开发工作流

```bash
# 运行测试
uv run pytest
# 或者
make test

# 格式化代码
uv run black .
# 或者
make format

# 代码检查
uv run flake8 src tests
# 或者
make lint

# 运行所有检查
make check
```

## 项目结构

```
uv-demo-project/
├── src/
│   └── uv_demo_project/
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── .venv/              # uv 创建的虚拟环境
├── main.py             # 项目入口点
├── pyproject.toml      # 项目配置和依赖
├── Makefile           # 开发任务
├── README.md
├── .gitignore
└── .python-version
```

## 配置说明

所有工具配置都在 `pyproject.toml` 中：

- **black**: 代码格式化，行长度88字符
- **flake8**: 代码质量检查，与 black 兼容的配置
- **pytest**: 测试配置，包含常用选项和标记

## 使用 uv 的优势

1. **快速**: 比 pip 快 10-100 倍
2. **简单**: 一个工具管理 Python 版本和依赖
3. **兼容**: 与现有的 Python 生态系统完全兼容
4. **现代**: 支持最新的 Python 包管理标准
