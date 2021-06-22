# ## GENERATOR ##
#
# def disp(a,b):
#     yield a
#     yield b
# result = disp(20,30)
# # lst = list(result)
# # print(lst)
# print(result)
# print(type(result))
# print(next(result))
#
#
#
# def show(a,b):
#     while a<=b:
#         yield a
#         a+=1
# result = show(1,5)
# print(result)
# print(type(result))
# print(next(result))
# print(next(result))
#
#
# for i in result:
#     print(i)


file = open("sourabh_dhekale.txt","a")
#file.write("python is a very easy to understand\n")
a = file.write("python is a very easy to understand\n")
print(a)                     # a is represent as a how many carrecter are avalable
file.close()

raws = 5
for i in range(0,raws):
    for j in range(1,i+1):
        print("*",end="")
    print("\r")


raws = 6
for i in range(raws+1,0,-1):
    for j in range(0,i-1):
        print("*", end="")
    print("\r")

file = open("sourabh_dhekale.txt")
# print(file.tell())                # .tell is represent the file pointer kute ahe te sangato
print(file.readline())
# print(file.tell())
#file.seek(0)
print(file.readline())          # next line read karayachi asel tar use kela jato
# print(file.tell())
file.close()


with open("sourabh_dhekale.txt") as file:
    a = file.read(6)
    print(a)                       # ya made close() use karawa lagat nahi



