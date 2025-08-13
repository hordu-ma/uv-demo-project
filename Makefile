.PHONY: help install test format lint clean run
.DEFAULT_GOAL := help

help: ## 显示此帮助信息
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## 安装项目依赖
	uv sync --dev

test: ## 运行测试
	uv run pytest

format: ## 格式化代码
	uv run black .

lint: ## 代码检查
	uv run flake8 src tests

check: ## 运行所有检查 (格式化检查 + 代码检查 + 测试)
	uv run black --check .
	uv run flake8 src tests
	uv run pytest

run: ## 运行主程序
	uv run uv-demo-project

clean: ## 清理构建文件
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
