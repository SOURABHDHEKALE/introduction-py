# # give two integer number their product,if product is grater than 1000,
# # then return their sum
# #
# # def multiplication_or_sum(num1,num2):
# #     product = num1 * num2
# #     result = product
# #     if product <= 1000:
# #         return product
# #     else:
# #         return num1 + num2
# # result = multiplication_or_sum(20,30)
# # print("the result is", result)
# # result = multiplication_or_sum(40,20)
# # print("the result is",result)
# #
# # #reverce each world of the string
# #
# # myster = "my name is sourabh"
# # print(myster[::-1])
#
# # with open('sample.txt', 'r') as file:
# #     data = file.read().replace('\n', ' ')
# #     print(data)
#
# # # remove iteam from the list while intiratting/
#    # remove number gater tha 50
#
# # list = [10,20,30,40,50,60,70,80,90,100]
#
# # i = 0
# # n = len(list)
# # while i < n:
# #     if list[i] > 50:
# #         del list[i]
# #         n = n-1
# #     else:
# #         i = i+1
# #         print(list)
# #
# # for i in range(len(list)-1,-1,-1):
# #     if list[i]>50:
# #         del list[i]
# #         print(list)
# #
# #
# # # # reverse dictionary mapping
# # dict = {"A": 65 , "B": 66, "C":67, "D":68}
# # new_dict = {value: key for key, value in dict.items()}
# # print(new_dict)
#
#
#
# # # display all iteams in the list
#
# # list = [10,20,40,20,30,10,30,40,60,70,80,70,90,90]
# # exist= {}
# # duplicates = []
# # for x in list:
# #  if x not in exist:
# #      exist[x] = 1
# #  else:
# #      duplicates.append(x)
# # print(duplicates)
#
#
# # 13/05/2021
# # sampleDict = {
# #   "name": "Kelly",
# #   "age":25,
# #   "salary": 8000,
# #   "city": "New york"
# # }
# # print(sampleDict.pop("city"))
#
#
# # # TUPLE
#
# # REVERSE THE TUPLE
#
# tuple = (10,20,30,40,50)
# print(tuple[::-1])
#
# # ACCESS THE VALE 20 FROM  THE FOLLOWING TUPLE
#
# tuple = ( " ORANGRE", [10,20,30],(5,15,25))
# print(tuple[1][1])
#
# # creat a tuple with single iteam 50
#
# a = (50,)
# print(a)
#
# # unpacking the followin tuple in 4 variabale
#
# tuple = (10,20,30,40)
# a, b, c, d = tuple
# print(a)
# print(b)
# print(c)
# print(d)
#
# # swap the follwing tuple
#
# tuple1 = (11,22)
# tuple2 = (99,88)
# tuple1, tuple2 = tuple2, tuple1
# print(tuple1)
# print(tuple2)
#
# # copy element 44 and 55 from the following tuple in to a new tuple
#
# tuple1 = (11,22,33,44,55,66)
# tuple2 = tuple1[3:5]
# print(tuple2)
#
# # modify the first iteam (22) of a list inside a following tuple to 222
#
# tuple1 = (11, [22,33],44,55)
# tuple1[1][0] = 222
# print(tuple1)
#
# # count the number of occurrences of iteam 50 from atuple
# tuple = (50,10,60,50,50,70,50)
# print(tuple.count(50))
#
# # check if all iteams in the following tuples are the same
# # tuple = (45,45,45,45,45)
#
# def check(sample_tuple):
#   return all(i == sample_tuple[0] for i in sample_tuple)
# tuple = (45,45,45,45,45)
# print(check(tuple))
# # another way
# tuple1 = (45, 45, 45, 45)
# tuple2 = tuple1[::-1]
# if tuple1 == tuple2:
#     print("True")
# else:
#     print("False")
#
# # sampleSet = {"Yellow", "Orange", "Black"}
# # print(sampleSet)
#
# # sampleSet = {"Yellow", "Orange", "Black"}
# # sampleSet.discard("Blue")
# # print(sampleSet)
# #
# # aSet = {1, 'PYnative', ('abc', 'xyz'), True}
# # print(aSet)
#
# # sampleSet = {"Yellow", "Orange", "Black"}
# # sampleSet.add("Blue")
# # sampleSet.add("Orange")
# # print(sampleSet)
# #
# # set1 = {10, 20, 30, 40, 50}
# # set2 = {60, 70, 10, 30, 40, 80, 20, 50}
# #
# # print(set1.issubset(set2))
# # print(set2.issuperset(set1))
# #
# # sampleSet = {"Yellow", "Orange", "Black"}
# # sampleSet.update(["Blue", "Green", "Red"])
# # print(sampleSet)
#
#
# # set1 = {"Yellow", "Orange", "Black"}
# # set2 = {"Orange", "Blue", "Pink"}
# #
# # set3 = set2.difference(set1)
# # print(set3)
#
# # set1 = {10, 20, 30, 40}
# # set2 = {50, 20, "10", 60}
# #
# # set3 = set1.union(set2)
# # print(set3)
#
#
# # l1 = [4,5,7,8,9,10]
# # l1[3]=22
# # print(l1)
#
#
# aTuple = (100,)
# print(aTuple * 2)
#
# aTuple = (100, 200, 300, 400, 500)
# print(aTuple[-2])
# print(aTuple[-4:-1])
#
# aTuple = (10, 20, 30, 40, 50, 60, 70, 80)
# print(aTuple[2:5], aTuple[:4], aTuple[3:])
#
# aTuple = "Yellow", 20, "Red"
# a, b, c = aTuple
# print(a)


# # 14/05/2021

# i = 1
# while i <= 5:
#     print("*"*i)
#     i = i + 1
#     print("done")
#
# i = 5
# while i >=1:
#     print('*'*i)
#     i= i - 1

# a = int(input("enter the first number:"))
# b = int(input("enter the second number:"))
# c = int(input("enter third number:"))
# d= []
# d.append(a)
# d.append(b)
# d.append(c)
# for i in range(0,3):
#     for j in range(0,3):
#         for k in range(0,3):
#             if (i!=j & j!=k & k!=i):
#                 print(d[i],d[j],d[k])

   
# l=[4,2,1,4,3,2,66,2]
# s=[i for i in l if i%2==0]
# print(len(s))


# add a list of a element to give set

set = {"yellow","orange","black"}
list = ["blue", "green","read"]
set.update(list)
print(set)


# return a new set of identicaliteam fro a given two set
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))
#print(set1
