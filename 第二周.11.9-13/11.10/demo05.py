"""
质数:大于一的整数,除了1和他本身以外不能再被其他数字整除
获取指定范围的质数
输入2,20
输出 [2,3,5,7,11,13,17,19]
"""


# res = []
# start=int(input("请输入开始值:"))
# stop=int(input("请输入终止值:"))
# for number in range(start,stop+1):
#     for i in range(2, number):
#         if number % i == 0:
#             break
#     else:
#         res.append(number)
# print(res)

def is_zhishu(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

#各司其职 便于查找,提到代码可读性

def find_zhishu(start, stop):
    res = []
    for i in range(start, stop + 1):
        if is_zhishu(i):
            res.append(i)



