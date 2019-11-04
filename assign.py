# -*- coding: utf-8


#creating bubble sorting function
def bubbleSort(lst1):
    n=len(lst1)
    for num in range(n-1,0,-1):
        for i in range(num):
            if lst1[i]>lst1[i+1]:
                temp = lst1[i]
                lst1[i] = lst1[i+1]
                lst1[i+1] = temp
                
array = []
arr = []
n = int(input("number of students to add"))
for i in range(n):
 print("Enter the roll number of the student : ")
 no = int(input())
 print("Enter the name of the student : ")
 name = input()
 values = [no,name]
 print("no:",no,"name:",name)
 array.append(values)
print(array)
for i in range(len(array)):
 arr.append(array[i][0])
print(arr)

bubbleSort(arr)


print ("Sorted array is:")
print (arr) 