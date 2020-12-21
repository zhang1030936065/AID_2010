"""
判断二维列表是否存在某个数字
"""
list01 = [1, 2, 3, 4, 5, 6]  # 一维列表
list02 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]  # 二维列表 行 列
number=1
for i in list02:
    if number in i:
        print(True)
        break
else:
    print(False)