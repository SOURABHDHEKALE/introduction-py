# f = open("sourabh.txt.py")
# content = f.read()      # this is a function
# print(content)
#
# # content = f.read()      # this is a function
# # print("1", content)
# #
# # content = f.read()      # this is a function
# # print("2", content)
#
# f.close()


import time
print("what shall I remind you about?")
text = str(input())
print("in how many minutes?")
local_time = float(input())
local_time = local_time * 60
time.sleep(local_time)
print(text)