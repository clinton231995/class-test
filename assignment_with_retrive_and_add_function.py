def add(n):

    for i in range(n):
     print("Enter the roll number of the student : ")
     no = int(input())
     print("Enter the name of the student : ")
     name = input()
     values = [no,name]
     print("no:",no,"name:",name)
     array.append(values)
    return array


def bubbleSort(lst1):
    for num in range(len(lst1)-1,0,-1):
        for i in range(num):
            if lst1[i]>lst1[i+1]:
                temp = lst1[i]
                lst1[i] = lst1[i+1]
                lst1[i+1] = temp
                
                
                
def retrieve(array,arr):
 arr1=[]
 for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]==array[j][0]:
            arr1.append(array[j])
 return arr1


array=[]
arr=[]
n = int(input("number of students to add"))
array=add(n)
print(array)
for i in range(len(array)):
 arr.append(array[i][0])
print(arr)

bubbleSort(arr)

arr1=retrieve(array,arr)
print ("Sorted array is:")
print (arr1) 

