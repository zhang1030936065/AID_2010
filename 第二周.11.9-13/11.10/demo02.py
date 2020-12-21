"""
删除列表重复元素
[4,35,7,64,7,35]
"""
list01 = [4, 35, 7, 64, 7, 35]
set01 = set(list01)
res = list(set01)
print(res)
