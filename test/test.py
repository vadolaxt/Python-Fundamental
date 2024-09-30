print("hello world")

# for i in range(5):
#     if i==3:
#         break
#     print(i)
# else:
#     print("Loop completed successfully")

print(2**3)
print(4/1)
print(4%1)
print(8//3)

# floor division(//) != classic divison(/)

# cmt trong py có 2 cash
# cách 1: dùng # để single line cmt
# cách 2: cmt nhiều dòng: """ """
"""
"""

# &: bitwise AND
"""
vidu
a = 5
b = 3
a &= b  # Tương đương với a = a & b
print(a)  # Kết quả: 1 (vì 5 & 3 = 1)
"""
# |: bitwise OR
"""
vidu
a = 5
b = 3
a |= b  # Tương đương với a = a | b
print(a)  # Kết quả: 7 (vì 5 | 3 = 7)
"""

# ^: bitwise XỎ
""" vidu
a = 5
b = 3
a ^= b  # Tương đương với a = a ^ b
print(a)  # Kết quả: 6 (vì 5 ^ 3 = 6)
"""
# >>=: Dịch bit sang phải và gán.
# <<=: Dịch bit sang trái và gán.
# :=  tìm hiểu thêm

#khai bao dong thoi nhieu bien
x,y,z =1,2,3
print(x)
print(y)
print(z)
print(x,y,z)
#Python allows you to extract the values (from list, tuples, etc.) into variables ➔ called unpacking

#global scope: keyword: "global"
s= "awesome"
def f():
#    global s #bo cmt ra de thay su khac biet
    s= "fantastic"
    print("FIT is "+ s)
f()
print(s)

# Syntax: range(start=0, stop, step=1)











