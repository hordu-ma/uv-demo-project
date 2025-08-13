"""Tests for main module."""

import pytest

from uv_demo_project.main import greet


def test_greet_default():
    """测试默认问候语."""
    result = greet()
    assert result == "Hello, World!"


def test_greet_with_name():
    """测试带名称的问候语."""
    result = greet("Python")
    assert result == "Hello, Python!"


def test_greet_empty_string():
    """测试空字符串."""
    result = greet("")
    assert result == "Hello, !"


@pytest.mark.parametrize(
    "name,expected",
    [
        ("Alice", "Hello, Alice!"),
        ("Bob", "Hello, Bob!"),
        ("测试", "Hello, 测试!"),
    ],
)
def test_greet_parametrized(name, expected):
    """参数化测试问候语函数."""
    result = greet(name)
    assert result == expected
