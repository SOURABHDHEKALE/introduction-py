# l1 = [x * x for x in range (5)]
# print(l1)
#
# for x in range(5):
#     print(x * x)
#
# s1 = { x*x for x in range (5)}
# print(s1)
#
# dict = {x:x*x for x in range (5)}
# print(dict)
# #
# tuple =(x*x for x in range (5))
# print(tuple)
# for x in tuple:
#     print(x)

# tuple packing & unpacking

# a = 20
# b = 50
# c = 60
# d = 80
# z = a,b,c,d
# print(z)
# unpacking
# x,y,w,k=z
# print("x=",x,"y=",y,"w=",w,"k=",k)

# Function

# bilt  in function it is allready avalabale in python
# user difined function
# def function_name():

#
# def sourabh():
#     print("hi sourabh")
#     print("how are you")
#     print("have a nice day")
# sourabh()
#
# def xyz(name):
#     print("hi",name)
#     print("how are you", name)
#     print("have a nice day",name)
# xyz("sourabh")
# xyz("sai")
# xyz("avi")
#
# def xyz(name):
#     print("name:=",name*100)
# xyz("\n sourabh")

# addition
# def abc(x,y):
#     return (x+y)
# result=abc(20,50)
# print(result)
#
# # substraction
def abc(x,y):
    return (x-y)
result=abc(40,10)
print(result)
#
# #multipication
# def abc(x,y):
#     return (x*y)
# result=abc(5,5)
# print(result)
#
# #division
# def abc(x,y):
#     return (x/y)
# result=abc(96,12)
# print(result)


# GLOBALE VARIABALE
#
# a = 50
# b = 60
# def add():
#     print(a+b)
# add()
# def sub():
#     print(a-b)
# sub()
# def mul():
#     print(a*b)
# mul()
# def div():
#     print(a/b)
# div()
