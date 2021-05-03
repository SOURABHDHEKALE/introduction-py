# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

# a=[1,2,3,4,5]
# print(a[3:0:-1])
# fruit=['apple', 'banana', 'papaya', 'cherry']

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]

    for row in m:
        for element in row:
            if v < element: v = element

    return v
print(fun(data[0]))

# colors = ["red", "green", "burnt sienna", "blue"]
# colors[2]
# print(colors)
#
# employee = {
#   "id": 1701,
#   "name": "James T Kirk",
#   "email": "jtkirk@starfleet.com",
#   "position": "captain",
# }
#
# # Add your code below:
# print(employee["email"])


