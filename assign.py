class Student:
    def __init__(self,array=[],lst1=[]):
        self.array=array
        self.lst1=lst1
    
    def add(self):
        for i in range(len(self.lst1)-1,0,-1):
            for j in range(i):
                if self.lst1[j]>self.lst1[j+1]:
                    temp = self.lst1[j]
                    self.lst1[j] = self.lst1[j+1]
                    self.lst1[j+1] = temp
        for i in range(len(self.lst1)):
            for j in range(len(self.lst1)):
                if self.lst1[i]==self.array[j][0]:
                    lst2.append(self.array[j])
        return lst2
array=[]
lst1=[]
lst2=[]
n=int(input('Enter the number of students to add : '))        
for i in range(n):
    print("Enter the roll number of the student : ")
    no = int(input())
    print("Enter the name of the student : ")
    name = input()
    values = [no,name]
    print("no:",no,"name:",name)
    array.append(values)
for i in range(len(array)):
    lst1.append(array[i][0])
student=Student(array,lst1)
print(student.add())
