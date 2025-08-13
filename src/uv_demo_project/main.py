"""Main module for uv-demo-project."""


def greet(name: str = "World") -> str:
    """返回问候语."""
    return f"Hello, {name}!"


def main() -> None:
    """主函数."""
    print(greet("uv-demo-project"))


if __name__ == "__main__":
    main()
