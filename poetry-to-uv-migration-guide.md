# Poetry项目迁移到uv详细指南

## 步骤1：备份现有项目

### 1.1 创建项目备份
```bash
# 备份整个项目目录
cp -r /path/to/your-poetry-project /path/to/your-poetry-project-backup

# 或者使用git创建备份分支
cd /path/to/your-poetry-project
git checkout -b backup-before-uv-migration
git add .
git commit -m "backup: 迁移到uv之前的项目状态备份"
```

### 1.2 特别备份关键文件
```bash
# 备份Poetry配置文件
cp pyproject.toml pyproject.toml.poetry-backup
cp poetry.lock poetry.lock.backup
```

### 1.3 导出Poetry依赖信息
```bash
# 导出所有依赖（包括开发依赖）到requirements文件
poetry export -f requirements.txt --output requirements-all.txt --dev

# 导出生产依赖
poetry export -f requirements.txt --output requirements-prod.txt

# 导出开发依赖
poetry export -f requirements.txt --output requirements-dev.txt --only dev
```

## 步骤2：使用uv init初始化项目

### 2.1 安装uv（如果尚未安装）
```bash
# 使用Homebrew安装
brew install uv

# 或使用pip安装
pip install uv
```

### 2.2 初始化uv项目
```bash
# 在现有项目目录中初始化uv项目
cd /path/to/your-poetry-project
uv init --no-readme  # 使用--no-readme避免覆盖现有README

# 或者在新目录初始化后迁移代码
mkdir /path/to/new-uv-project
cd /path/to/new-uv-project
uv init your-project-name
# 然后将源代码复制过来
```

### 2.3 设置Python版本
```bash
# 设置项目使用的Python版本（根据Poetry项目的python版本要求）
uv python pin 3.12  # 替换为您项目需要的版本
```

## 步骤3：迁移Poetry依赖到uv配置

### 3.1 分析Poetry的pyproject.toml
以下是典型的Poetry配置结构：
```toml
[tool.poetry]
name = "my-project"
version = "0.1.0"
description = "项目描述"
authors = ["Your Name <your.email@example.com>"]

[tool.poetry.dependencies]
python = "^3.12"
requests = "^2.28.0"
fastapi = "^0.68.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.0.0"
black = "^22.0.0"
flake8 = "^4.0.0"
```

### 3.2 转换为uv的pyproject.toml格式
```toml
[project]
name = "my-project"
version = "0.1.0"
description = "项目描述"
authors = [{name = "Your Name", email = "your.email@example.com"}]
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "requests>=2.28.0",
    "fastapi>=0.68.0",
]

[dependency-groups]
dev = [
    "pytest>=7.0.0",
    "black>=22.0.0",
    "flake8>=4.0.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

### 3.3 版本约束转换规则
| Poetry语法 | uv/PEP 621语法 | 说明 |
|------------|----------------|------|
| `"^2.28.0"` | `">=2.28.0,<3.0.0"` | 兼容版本约束 |
| `"~2.28.0"` | `">=2.28.0,<2.29.0"` | 补丁版本约束 |
| `">=2.28.0"` | `">=2.28.0"` | 最小版本约束 |
| `"==2.28.0"` | `"==2.28.0"` | 精确版本约束 |

### 3.4 使用命令行添加依赖
```bash
# 添加生产依赖
uv add requests fastapi

# 添加开发依赖
uv add --dev pytest black flake8

# 从requirements文件添加依赖
uv add -r requirements-prod.txt
uv add --dev -r requirements-dev.txt
```

## 步骤4：迁移开发和生产配置

### 4.1 迁移工具配置
保留Poetry项目中的工具配置部分，这些在uv中同样有效：

```toml
# 保留这些配置不变
[tool.black]
line-length = 88
target-version = ['py312']

[tool.flake8]
max-line-length = 88
extend-ignore = ["E203", "W503"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
```

### 4.2 迁移脚本配置
```toml
# Poetry格式
[tool.poetry.scripts]
my-script = "my_package.main:main"

# 转换为uv/PEP 621格式
[project.scripts]
my-script = "my_package.main:main"
```

### 4.3 迁移其他元数据
```toml
[project]
# 基本信息
name = "my-project"
version = "0.1.0"
description = "项目描述"
readme = "README.md"
license = {text = "MIT"}
authors = [{name = "Your Name", email = "your.email@example.com"}]
maintainers = [{name = "Maintainer Name", email = "maintainer@example.com"}]
keywords = ["keyword1", "keyword2"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.12",
]

# URL信息
[project.urls]
Homepage = "https://github.com/username/my-project"
Documentation = "https://my-project.readthedocs.io/"
Repository = "https://github.com/username/my-project.git"
"Bug Tracker" = "https://github.com/username/my-project/issues"
```

## 步骤5：验证迁移结果

### 5.1 检查依赖安装
```bash
# 创建虚拟环境并安装依赖
uv sync

# 检查安装的包
uv pip list

# 验证开发依赖
uv run pytest --version
uv run black --version
uv run flake8 --version
```

### 5.2 运行测试
```bash
# 运行测试套件
uv run pytest

# 运行代码格式化
uv run black .

# 运行代码检查
uv run flake8 .
```

### 5.3 验证脚本
```bash
# 测试项目脚本
uv run my-script
```

## 步骤6：清理Poetry文件

### 6.1 移除Poetry特定文件
```bash
# 备份后删除Poetry锁文件
rm poetry.lock

# 如果使用pyproject.toml.poetry-backup作为备份
# 可以删除原有的poetry相关配置
```

### 6.2 更新CI/CD配置
如果项目有CI/CD流程，需要更新配置文件：

```yaml
# GitHub Actions示例（.github/workflows/test.yml）
- name: Set up Python
  uses: actions/setup-python@v4
  with:
    python-version: '3.12'

- name: Install uv
  run: pip install uv

- name: Install dependencies
  run: uv sync

- name: Run tests
  run: uv run pytest
```

## 步骤7：常见问题和解决方案

### 7.1 依赖版本冲突
```bash
# 查看依赖树
uv tree

# 解决版本冲突
uv add "package-name>=1.0.0,<2.0.0"
```

### 7.2 开发环境配置
```bash
# 创建开发环境的shell脚本
cat > scripts/dev-setup.sh << 'EOF'
#!/bin/bash
# 安装开发依赖
uv sync --group dev

# 安装pre-commit hooks（如果使用）
uv run pre-commit install
EOF

chmod +x scripts/dev-setup.sh
```

### 7.3 环境变量和配置
```bash
# 创建.env文件模板
cat > .env.example << 'EOF'
# 开发环境配置
DEBUG=True
DATABASE_URL=sqlite:///./dev.db
SECRET_KEY=your-secret-key-here
EOF
```

## 步骤8：文档更新

### 8.1 更新README.md
更新项目文档，将Poetry命令替换为uv命令：

```markdown
# 项目名称

## 安装

```bash
# 克隆项目
git clone https://github.com/username/my-project.git
cd my-project

# 安装依赖
uv sync
```

## 开发

```bash
# 运行测试
uv run pytest

# 代码格式化
uv run black .

# 代码检查
uv run flake8 .
```

## 构建和发布

```bash
# 构建项目
uv build

# 发布到PyPI
uv publish
```
```

### 8.2 更新贡献指南
如果有CONTRIBUTING.md文件，更新其中的开发环境设置说明。

## 完成迁移检查清单

- [ ] 备份原项目和关键文件
- [ ] 成功运行`uv init`
- [ ] 迁移所有生产依赖
- [ ] 迁移所有开发依赖
- [ ] 迁移工具配置（black, flake8, pytest等）
- [ ] 迁移脚本和入口点
- [ ] 迁移项目元数据
- [ ] 验证测试通过
- [ ] 验证代码格式化工具正常
- [ ] 验证脚本可以正常运行
- [ ] 更新CI/CD配置
- [ ] 更新项目文档
- [ ] 清理Poetry相关文件

## 性能和优势对比

使用uv相比Poetry的主要优势：
- 更快的依赖解析和安装速度（10-100倍）
- 标准的PEP 621项目配置格式
- 更小的锁文件体积
- 与Python生态系统更好的兼容性
- 更简洁的命令行界面

迁移完成后，您的项目将获得更快的开发体验和更好的标准兼容性。
