#!/usr/bin/env python
# coding: utf-8

# In[ ]:


knight = {} 
x=input('Enter the student id : ')
y=input('Enter the student id : ')
z=input('Enter the student id : ')
knight[x] = input('Enter the course name : ')
knight[y] = input('Enter the course name : ')
knight[z] = input('Enter the course name : ')

x, y, z = 5, 2, 4

print(knight)
len(knight)

for k,v in knight.items():
    print(k,v)

for f in sorted(set(knight)):
    print(f)
    print(knight)

