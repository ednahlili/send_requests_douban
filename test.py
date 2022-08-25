# 变量
# 1.变量解包
a, b = [111, 222]
print(a, b)

# 2.动态解包
data = [11, 22, 33, 44, 55, 66, 77, 88]
a, *num, b = data
print(num)
a, num2, b1 = data[0], data[1:-1], data[-1]
print(num)


# 字符串
# 1.遍历字符串
s = "hello world"
for c in s:
    print(c)

# 2.反转字符串：切片；reverse
print(s[::-1])
# reversed函数返回一个可迭代对象，join将它转换成字符串
s_reversed = reversed(s)
print(''.join(s_reversed))

# 3.字符串格式化
user, score = "lily", 10
# str.format
print('welcome {}, your score is {:d}'.format(user, score))
# f-string
print(f'welcome {user}, your score is {score:d}')

# 4.拼接字符串
print("123"+"567")

# 5.split()

