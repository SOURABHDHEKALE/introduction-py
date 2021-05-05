# a=input("enter 1st number:")
# # b=input("enter 2nd number:")
# # c=a+b,
# # print("addition=",c)
#
# a = int(input("enter 1st number:"))
# b = int(input("enter 2nd number:"))
# c = a+b,
# print("addition = ",c)

#
def add_sub_mul_div(y):
    x = 20
    a = x + y
    b = x - y
    c = x*y
    d = x/y
    return a,b,c,d
add,sub,mul,div = add_sub_mul_div(40)
print(add)
print(sub)
print(mul)
print(div)



def xyz(y):
    x = 20
    a = x + y
    b = x - y
    c = x*y
    d = x/y
    return a,b,c,d
a,b,c,d = xyz(40)
print(a)
print(b)
print(c)
print(d)