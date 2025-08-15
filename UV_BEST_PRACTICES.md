# uv 虚拟环境最佳实践指南

## 一、如何判断虚拟环境是否已激活

### 1. 检查环境变量
```bash
# 检查 VIRTUAL_ENV 环境变量
echo $VIRTUAL_ENV
# 如果输出为空，说明虚拟环境未激活
# 如果输出路径（如 /path/to/project/.venv），说明已激活
```

### 2. 检查 Python 解释器路径
```bash
# 查看当前 Python 路径
which python
# 如果显示 .venv/bin/python，说明使用的是虚拟环境
# 如果显示系统 Python 路径，说明未激活虚拟环境
```

### 3. 查看命令提示符
激活虚拟环境后，命令提示符通常会显示虚拟环境名称：
```bash
(.venv) ➜  uv-demo-project   # 已激活
➜  uv-demo-project           # 未激活
```

### 4. 使用验证脚本
```python
import sys
print(f"Python 路径: {sys.executable}")
# 输出包含 .venv 说明在虚拟环境中
```

## 二、进入项目文件夹的标准流程

### 推荐方式：使用 `uv run`（无需手动激活）

**这是 uv 的最大优势之一！** 使用 `uv run` 可以自动在正确的虚拟环境中执行命令，无需手动激活。

```bash
# 进入项目目录
cd /path/to/your/project

# 直接使用 uv run 执行命令（自动使用项目虚拟环境）
uv run python script.py
uv run pytest
uv run pip list
uv run black .
uv run flake8
```

### 传统方式：手动激活虚拟环境

如果你更习惯传统的工作流：

```bash
# 1. 进入项目目录
cd /path/to/your/project

# 2. 检查虚拟环境是否存在
ls -la .venv

# 3. 如果不存在，创建虚拟环境
uv venv

# 4. 激活虚拟环境
source .venv/bin/activate

# 5. 安装/更新依赖
uv sync  # 如果有 pyproject.toml
# 或
uv pip install -r requirements.txt

# 6. 开始工作
python script.py

# 7. 退出虚拟环境（工作结束后）
deactivate
```

## 三、最佳实践建议

### 1. 项目初始化
```bash
# 创建新项目
mkdir my-project && cd my-project

# 初始化 uv 项目（创建 pyproject.toml）
uv init

# 创建虚拟环境（uv init 通常会自动创建）
uv venv

# 添加依赖
uv add pytest black flake8
uv add --dev ipython  # 开发依赖
```

### 2. 依赖管理
```bash
# 添加新依赖
uv add package-name

# 安装所有依赖
uv sync

# 更新依赖
uv lock --upgrade-package package-name

# 查看依赖树
uv tree
```

### 3. 日常开发流程
```bash
# 方式一：使用 uv run（推荐）
cd my-project
uv run python main.py
uv run pytest tests/

# 方式二：激活虚拟环境
cd my-project
source .venv/bin/activate
python main.py
pytest tests/
deactivate
```

### 4. 自动化脚本
在项目根目录创建 `.envrc` 文件（配合 direnv 使用）：
```bash
# .envrc
if [ -d .venv ]; then
    source .venv/bin/activate
fi
```

或者在 shell 配置文件中添加函数：
```bash
# 添加到 ~/.zshrc 或 ~/.bashrc
function cd() {
    builtin cd "$@"
    if [ -f .venv/bin/activate ]; then
        source .venv/bin/activate
    fi
}
```

### 5. CI/CD 集成
```yaml
# GitHub Actions 示例
- name: Set up Python
  uses: actions/setup-python@v4
  with:
    python-version: '3.12'

- name: Install uv
  run: pip install uv

- name: Install dependencies
  run: |
    uv venv
    uv sync

- name: Run tests
  run: uv run pytest
```

## 四、常见问题解答

### Q1: 是否必须激活虚拟环境？
**答：** 使用 uv 时不是必须的。`uv run` 命令会自动在虚拟环境中执行，这是 uv 的核心优势。

### Q2: uv run 和手动激活有什么区别？
**答：**
- `uv run`：每个命令都在隔离的虚拟环境中执行，更安全
- 手动激活：整个 shell 会话都在虚拟环境中，更方便连续操作

### Q3: 如何确保使用正确的 Python 版本？
```bash
# 在 pyproject.toml 中指定
[project]
requires-python = ">=3.12"

# 创建虚拟环境时指定
uv venv --python 3.12
```

### Q4: 多个项目如何管理？
每个项目都有独立的 `.venv` 目录，互不干扰。使用 `uv run` 会自动选择当前项目的虚拟环境。

## 五、性能优化技巧

1. **使用 uv 的缓存机制**
   ```bash
   # uv 会自动缓存下载的包，加速后续安装
   uv cache dir  # 查看缓存位置
   ```

2. **并行安装**
   ```bash
   # uv 默认并行安装，比 pip 快很多
   uv sync  # 自动并行
   ```

3. **使用本地索引**
   ```bash
   # 配置私有 PyPI
   uv pip install --index-url https://your-pypi.com package
   ```

## 六、总结

### 核心要点
1. ✅ **推荐使用 `uv run`** - 无需手动管理虚拟环境激活
2. ✅ **项目级隔离** - 每个项目有独立的 `.venv`
3. ✅ **快速安装** - uv 的性能比 pip 快 10-100 倍
4. ✅ **简化工作流** - 减少虚拟环境管理的心智负担

### 快速参考
```bash
# 最常用的命令
uv init          # 初始化项目
uv venv          # 创建虚拟环境
uv add package   # 添加依赖
uv sync          # 同步依赖
uv run command   # 在虚拟环境中运行命令
uv tree          # 查看依赖树
```

---

*更多信息请参考 [uv 官方文档](https://github.com/astral-sh/uv)*
