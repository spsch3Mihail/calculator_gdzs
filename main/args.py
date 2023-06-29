# def func(*args, **kwargs):
#     summa = 0
#     for i in args:
#         summa +=i
#     return summa, kwargs
#
# print(func(1,2,3, n = 1, a =3))

# def minimum(*args):
#     minn = args[0]
#     for i in args:
#         if minn > i:
#             minn = i
#
#     return minn
#
# print(minimum('a', 'c', 'D'))


def sum_digits(number):
    number = str(number)
    if number.startswith('-'):
        number = number[1:]
    return sum([abs(int(i)) for i in number])


print(sum_digits(-32))