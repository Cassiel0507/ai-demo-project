def add(a:int, b:int) -> int:
    return a + b

print(add(2, 3))  # Output: 5

# 写一个函数，计算数组标准差，附带单元测试
import math

def calculate_std_dev(numbers):
    if not numbers:
        return 0
    mean = sum(numbers) / len(numbers)
    squared_diffs = [(x - mean) ** 2 for x in numbers]
    variance = sum(squared_diffs) / len(numbers)
    return math.hypot(variance, 0)