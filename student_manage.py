''''Write a program to build a simple Student Management System using Python which can perform the following operations:

Accept
Display
Search
Delete
Update'''


class Student:
    #Constructor 
    def __init__(self,name,rollno ,m1,m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2
        
    #Fun to create and append new student
    def accept(self,Name,Rollno,marks1,marks2):
        
    #take input from teh user
        ob = Student(Name,Rollno,marks1,marks2)
        ls.append(ob)
        
    def display(self,ob):
        print("Name :",ob.name)
        print("Roll no :",ob.rollno)
        print("Marks1 :",ob.m1)
        print("Marks2 :",ob.m2)
        print("\n")
        
        
    #Search Function
    def search(self,rn):
        for i in range(len(ls)):
            if ls[i].rollno == rn:
                return i
            
    #Delete Function
    def delete(self,rn):
        i = obj.search(rn)
        del ls[i]
        
    #Update Function
    def update(self,rn,No):
        i = obj.search(rn)
        roll = No
        ls[i].rollno = roll
        
        
#Creating a list to add students
ls = []
obj = Student('',0,0,0)

print("\nOperations Used, ")
print("\n1.Accept Student details \n2.Display Student Details\n3.Search Details of Student\n4.Delete Details of a Student\n5.Update Student Details\n6.Exit")


obj.accept("A",1,100,100)
obj.accept("B",2,90,90)
obj.accept("C",3,80,80)

print("\n")
print("\nList of Students\n")
for i in range(len(ls)):
    obj.display(ls[i])
    
print("\n Student Found, ")
s=obj.search(2)
obj.display(ls[s])

obj.delete(2)
print(len())
print("List after deletion")
for i in range(ls.__len__()):
	obj.display(ls[i])
 
obj.update(3,2)
#print(ls.__len__())
print("List after updation")
for i in range(ls.__len__()):
	obj.display(ls[i])

# else:
print("Thank You !")