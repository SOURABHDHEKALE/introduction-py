# class student:
#     pass
#
# harry = student()
# larry = student()
#
#
# harry.name = "harry"
# harry.std = 12
# harry.section = 1
# #print(harry, larry)
# print(harry.name)
# print(harry.std)
# print(harry.section)


#instance & class variabale

class Employee:
    no_of_leaves =8
    pass

harry = Employee()
rohan = Employee()


harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"


rohan.name = "Rohan"
rohan.salary = 4556
rohan.role = "student"
print(Employee.no_of_leaves)
print(rohan.__dict__)
rohan.no_of_leaves = 9
print(Employee.__dict__)
#print(harry.no_of_leaves)
print(Employee.no_of_leaves)








