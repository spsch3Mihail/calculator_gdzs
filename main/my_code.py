# squares_odd_nums = {i: i ** 2 for i in range(10) if i % 2}
# squares_even_nums = {i: i ** 2 for i in range(10) if i % 2 == 0}
# squares_odd_nums.update(squares_even_nums)
# # print(squares_odd_nums)
# for key in squares_odd_nums:
#     print(f'{key}: {squares_odd_nums[key]}')


# x = [1,2,3,4,5]

# for num in range(len(x)):
#     x[num] += 1
# print(x)

# i = 0
# while i < len(x):
#     x[i] += 1
#     i += 1
# print(x)

# a = [i + 1 for i in x]
# print(x,a)

# a = 'asdf'
# b = 'zxcv'
# c = 'bnm,'
# d = 'qwer'
# for (x,y,z,v) in zip(a,b,c,d):
#     print(f'{x,y,z,v}-- {x+y+z+v}')

a = 'spam'
# b = list(map(ord, a))
# print(f'{a.upper()} is ord {b}')

# result = []
# for i in a:
#     result.append(ord(i))
# print(result)

# k = ['s', 'e', 't']
# v = [1,2,3]
#
# # di = list(zip(k,v))
# # print(di)
# #
# # d = {}
# # for k,v in di:
# #     d[k] = v
# # print(d)
#
# d = dict(zip(k,v))
# print(d)

# a = 'spam'
# for index,i in enumerate(a,1):
#     print(i,index)


# m = 'FFFAAAAFFDDD'
#
# def unique_elem(string) -> None:
#     a = ''
#     for i in range(len(string)):
#         if i == 0 or string[i] != string[i - 1]:
#             a +=string[i]
#     return a
#
#
#
#
# print(unique_elem('FFFAAAAFFDDD'))
# x = 'asd'
# y = 'qwe'
#
# a = [(i * 2 + j * 2) for i in x for j in y]
# print(a)

# res = []
#
# for i in x:
#     for j in y:
#         res.append(i+j)
# print(res)

# uppers = [line.upper().rstrip() for line in open('file.py')]
# I = iter(uppers)
# print(next(I))
# print(next(I))

# lines = list(map(str.rstrip, open('file.py'))) rstrip без скобок!!!
# print(lines)


# d = {i: line for i, line in enumerate(open('file.py'))} ген-р словаря с исп. enumerate
# print(d)

L = (1, True, None, 4)
def f(a,b,c,d):
    print(a,b,c,d, sep='&')
print(f(*L))