# with open('file.py') as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print(line, end='')
#
#
# with open('file.py') as f:
#     print('\n'.join([line.rstrip() for line in f]))

lines = [line.rstrip() for line in open('file.py')]
print(lines)


# l = [1,2,3,4,5]
# print(next(iter(l)))
# print(next(iter(l)))

# I =iter(l)
# print(next(I))



