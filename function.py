#DETA TYPE : IT IS REPRESENT THE TYPE OF DETA STORE IN TO THE MEMORY OR VARIABALE.

# BILT IN DETA TYPE
# NUMERICAL:
#   INT - It is a numeracal number like 20,22,250,-20,-250 etc and also in ths without desimal point are accured
#   in python there is no any limit to store the value . how much long number is not matter to the size for ex- 54587978459745
#     is limit is not difined in this python.

y=10
print(type(y))

# float - it is represent flotting point number and it  number contain the desimal number
# ex- 20.3,56.3,48.56,-48.9,-98.7 etc
y=56.8
print(type(y))
x=5.2e5
print(x)

# FUNCTION :
#write once and use it as many time as you need
#define a function
def disp():
    name = "geekyshows"
    print("welcome to", name)
disp()
disp()
disp()

# FOR ADDITION :
def add():
    x = 10
    y = 20
    c = x+y
    print(c)
add()

# FOR SUBSTRATCTION :
def sub():
    x = 10
    y = 20
    c = y-x
    print(c)
sub()

# for multiply :
def mul():
    x = 10
    y = 20
    c = x*y
    print(c)
mul()

#for division :

def div():
    x = 25
    y = 5
    c = x/y
    print(c)
div()

# function with argument and parameter
# defining function without parameter:

def add(y):
    x = 20
    c = x + y # y is a argument
    print(c)
add(30)


#RETURN FUNCTION: with argument

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
print( div)
