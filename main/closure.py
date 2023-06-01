# def outer(name):
#     def inner():
#         print(f'Hello, {name}')
#
#     return inner
#
# a = outer('ALIK')
# print(a())
# b = outer('BRED')
# print(b())


# def outer(a):
#     def inner(b):
#         return a + b
#
#     return inner
#
# a2 = outer(2)
# print(a2(2))
# a3 = outer(3)
# print(a3(3))

def outer():
    counter = 0
    def inner():
        nonlocal counter
        counter += 1
        return counter

    return inner

c = outer()
print(c())
print(c())
b = outer()
print(b())