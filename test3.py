# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
#
# result=factorial(8)
# print(result)


# sum1 = 0
# n = int(input("Please enter number "))
# for i in range(1, n + 1, 1):
#     sum1 += i
# print("\n")
# print("Sum is: ", sum1)

# # print first 10 natural number using while loop
#i = 0
# while i <=10:
#     print(i)
#     i += 1
#
# # using for loop
# for i in range(11):
#     print(i)


# pattern in python

# rows = 6
# for i in range(rows):
#     for j in range(i):
#         print(i,end='')
#     print('')

# aList = [4, 6, 8, 24, 12, 2]
# print(aList[3])
#
# import sys
# print("Python version")
# print (sys.version)
# print("Version info.")
# print (sys.version_info)

# accept the two numbers from the user & calculate the multiplication

# num1 = int(input("enter the first number"))
# num2 = int(input("enter the second number"))
# result = num1 + num2
# print(result)

# display "my name is sourabh"as my**name**is**sourabh" using o/p formatting of a print function
# print("my","name","is","sourabh",sep = "***")
#
# # convert decimal number to octal using print()o/p formatting
# print('%o'%(8))
#
# # display float number with two decimal placeses
# print('%.2f'%458.541315)

# print(123%10)
# print(12%10)
# print(12//10)
# print(1%10)
# print(1//10)

num = 123
while num != 0:
    revrs = num%10
    num = num//10
    print(revrs,end="")

# num = 123
# while num != 0:
#     revrs = num%20
#     num = num//20
#     print(revrs)


# count = 0
# with open("test.txt", "r") as fp:
#     lines = fp.readlines()
#     count = len(lines)
# with open("newFile.txt", "w") as fp:
#     for line in lines:
#         if (count == 3):
#             count -= 1
#             continue
#         else:
#             fp.write(line)
#         count-=1



str1, str2, str3 = input("Enter three string").split()
print(str1, str2, str3)