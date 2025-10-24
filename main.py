# 在此文件中实现 isOdd 函数

def isOdd(value):
    """
    判断输入是否为奇整数    
    参数:
    value - 任意类型的输入值    
    返回:
    bool - 如果是整数且为奇数返回 True，否则返回 False
    """
   def isOdd(param):
    if not isinstance(param, int):  # 检查是否为整数类型
        return False
    return param % 2 != 0  # 奇数的判断条件

