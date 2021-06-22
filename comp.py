ls = []
for i in range (80):
    if i%3 == 0:
        ls.append(i)
print(ls)


ls = [i for i in range(80) if i%3==0]
print(ls)