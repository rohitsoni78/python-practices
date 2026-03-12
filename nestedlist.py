students=[["id","name","grade"],[1,"Ravi","0"],[2,"Mitesh","A+"]]
print(students)
# print(students[0])
# print(students[1])
# print(students[2])
# for i in students:
#     print(i)

#Find students name ans grade whoes id is 2
# print("Student id 2 name is=",students[2][1])
# print("Student id 2 name is=",students[2][2])

# Find student name and grade by entering students id
id=int(input("Enter student id to find name and grade="))
flag=False
for i in students:
    if i[0]==id:
        flag=True
        print("ID=",i[0])
        print("Name=",i[1])
        print("Grade=",i[2])
if flag==False:
    print("Id not found. Try again!!")