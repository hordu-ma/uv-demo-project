"""
斐波那契数列实现
"""


def fibonacci_recursive(n):
    """
    使用递归方法计算斐波那契数列的第n项
    
    Args:
        n (int): 要计算的项数（从0开始）
    
    Returns:
        int: 斐波那契数列的第n项
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    """
    使用迭代方法计算斐波那契数列的第n项
    
    Args:
        n (int): 要计算的项数（从0开始）
    
    Returns:
        int: 斐波那契数列的第n项
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_sequence(count):
    """
    生成斐波那契数列的前count项
    
    Args:
        count (int): 要生成的项数
    
    Returns:
        list: 包含前count项斐波那契数的列表
    """
    if count <= 0:
        return []
    elif count == 1:
        return [0]
    elif count == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, count):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence


def fibonacci_generator(count):
    """
    使用生成器生成斐波那契数列
    
    Args:
        count (int): 要生成的项数
    
    Yields:
        int: 斐波那契数列的每一项
    """
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    # 示例用法
    n = 10
    
    print("斐波那契数列示例:")
    print(f"前{n}项数列: {fibonacci_sequence(n)}")
    
    print(f"\n使用递归计算第{n}项: {fibonacci_recursive(n)}")
    print(f"使用迭代计算第{n}项: {fibonacci_iterative(n)}")
    
    print(f"\n使用生成器生成前{n}项:")
    fib_gen = list(fibonacci_generator(n))
    print(fib_gen)
    
    # 性能比较示例
    import time
    
    test_n = 30
    print(f"\n性能比较 (n={test_n}):")
    
    start = time.time()
    result_recursive = fibonacci_recursive(test_n)
    time_recursive = time.time() - start
    print(f"递归方法: {result_recursive}, 耗时: {time_recursive:.6f}秒")
    
    start = time.time()
    result_iterative = fibonacci_iterative(test_n)
    time_iterative = time.time() - start
    print(f"迭代方法: {result_iterative}, 耗时: {time_iterative:.6f}秒")
