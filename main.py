def add(a: float, b: float) -> float:
    """
    计算两个数的和。

    Args:
        a: 第一个加数
        b: 第二个加数

    Returns:
        两个数的和

    Raises:
        TypeError: 当参数不是数字类型时抛出
    """
    # 参数类型检查
    if not isinstance(a, (int, float)):
        raise TypeError(f"参数 a 必须是数字类型，当前类型为 {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"参数 b 必须是数字类型，当前类型为 {type(b).__name__}")
    return a + b
