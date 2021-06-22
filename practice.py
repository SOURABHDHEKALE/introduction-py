

# revers a list

# alist = [100,200,300,400,500]
# print(alist[::-1])
#
# # Concatenate two lists index-wise
# list1 = ['m','na','i','sour']
# list2 = ['y','me','s','abh']
# list3 = [i+j for i, j in zip(list1,list2)]
# print(list3)
#
# #   Given a Python list of numbers. Turn every item of a list into its square
# list = [1,2,3,4,5,6]
# list = [x * x for x in list]
# print(list)


#Concatenate two lists in the following order
# list1 = ['hello','take']
# list2 = ['dear','sir']
# list3 = [x+y for x in list1 for y in list2]
# print(list3)
#
# # Given a two Python list. Iterate both lists simultaneously such that list1 should display
# # item in original order and list2 in reverse order
# list1 = [10,20,30,40]
# list2 = [100,200,300,400]
# for x,y in zip(list1,list2[::-1]):
#     print(x,y)
#
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)
#
#
# list1 = [5, 20, 15, 20, 25, 50, 20]
#
# while 20 in list1:
#     list1.remove(20)
#
# def addition(x,y):
#     z=x+y
#     print("addition is:", z)


# list = [10,20,30,40,50,60,70,80,90]
# print(list[::-1])

# list1 = ['ra','i','go','bo']
# list2 = ['m','s','od','y']
# l3 = [i+j for i, for j in zip(list1,list2)]
# print(l3)


# aList = [1, 2, 3, 4, 5, 6, 7]
# newlist = [x*x for x in aList]
# print(newlist)
#
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# list3 = [x+y for x in list1 for y in list2]
# print(list3)
#
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for x,y in zip(list1,list2[::-1]):
#     print(x,y)
#
#
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# result = dict(zip(keys,values))
# print(result)
#
# sagar = ['a','b','c','d']
# ram = [1,2,3,4]
# res = dict(zip(sagar,ram[::-1]))
# print(res)
#
# dict = {'one':10,'two':20,'three':30,'four':40}
# dict2 = {'three':30,'five':50,'six':60,'seven':70}
# dict3 = {**dict,**dict2 }
# print(dict3)
#
# dict = {'one':10,'two':20,'three':30,'four':40}
# dict2 = {'three':30,'five':50,'six':60,'seven':70}
# dict3 = dict.copy()
# dict3.update(dict2)
# print(dict3)
#
# employees = ['Kelly', 'Emma', 'John']
# defaults = {"designation": 'Application Developer', "salary": 8000}
# res = dict.fromkeys(employees,defaults)
# print(res)
# print(res['Emma'])
#
# a = [10,20,30,40,50,60]
# b = {'a':11,'b':22,'c':33,'d':44,'e':55,'f':66}
# c = dict.fromkeys(a,b)
# print(c)
# print(c[30])

#
# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york" }
#
# keys = ["name", "salary"]
# newdict = {k:sampleDict[k] for k in keys}
# print(newdict)
#
# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york" }
#
# keys = ["name", "salary"]
# dict = {k:sampleDict[k] for k in sampleDict.keys() -keys}
# print(dict)
#
#
# dict2 = {'three':30,'five':50,'six':60,'seven':70}
# print(60 in dict2.values())
#
#
# Dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# print(min(Dict , key = Dict.get))
#
# dict1 ={ 'english':56,'maths':65,'physics':88}
# print(max(dict1, key = dict1.get))
# print(min(dict1, key = dict1.get))
#
#
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.intersection(set2))
# succubus
# set = {10,20,30,50,40,80,90}
# set2 = {20,30,40,50,60,80,99,20,10,60}
# print(set.union(set2))


set1 = {10,60,30,50}
set2= {20,40,30,70}
set1.difference_update(set2)
print(set1)

set = {10,20,30,50,70,80,90}
set.difference_update({20,30,50})
print(set)

set1 = {10,20,30,50,60}
set2 ={20,30,50,70,80,90}
set1.symmetric_difference_update(set2)
print(set1)