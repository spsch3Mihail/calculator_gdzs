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

# L = {1, 2, 3, 4}
# def f(a, b, c, d):
#     print(a, b, c, d, sep='&')
# print(f(*L))

# x = (1, 2)
# y = (3, 4)
# print(list(zip(x, y)))
# print(list(zip(*zip(x, y))))

# a = '_'.join(list(map(str, [1,2,3])))
# print(a)

# a = range(0,11)
# I = iter(a)
# I_2 = iter(a)
# print(next(I))
# print(next(I))
# print(next(I_2))


# d = dict(a=1, b=2, c=3)
# K = list(d.keys())
# V = list(d.values())
# I = list(d.items())
# print(tuple(zip(K,V)))
# print(list(d.items()))

# d = dict(b=1, a=2, c=3)

# for K, V in d.items():
#     print(K, V, end='; ')

# for key in sorted(d.keys()):    сортировка словаря. ф-я sorted ВСЕГДА возвр. список
#     print(key, d[key], end='; ')

# for key in sorted(d):
#     print(key, d[key], end='; ')

# lst_methods = ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# string_methods = ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# dictonary_methods = ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# set_methods = ['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
# tuple_methods = ['count', 'index']
# int_methods = ['as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
# for i in int_methods:
#     print(i)

# d_set_methods = dir(set)
# for method in d_set_methods:
#     if not method.startswith('__'):
#         print(method)