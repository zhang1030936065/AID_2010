"""
返回第一个不重复的字母
"ABCACDBEFD"
"""
str01 = "ABCACDBEFD"
for i in str01:
    if str01.count(i) == 1:
        print(i)
        break
