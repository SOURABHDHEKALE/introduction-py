# def gen(n):
#     for i in range(n):
#         yield  i
#
# g = gen(3)
# print(g.__next__())            iterator
# print(g.__next__())
# print(g.__next__())


# h = "harry"
# ier = iter(h)                 #iterable
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())


list1 = [1, 2, -5, -6, -9, -8, 4, 7, 9]
pop_list = list(filter(lambda x: (x >= 0), list1))
print(pop_list)



