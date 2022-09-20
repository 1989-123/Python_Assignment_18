""" 
Write a python program to convert two lists into a dictionary 
in a way that item from list1 is the key and item from 
list2 is the value.
"""

l1 = [10, 20, 30]
l2 = ['Jayesh', 'Hitesh', 'Paresh']
s1 = {}
i, j = 0, 0
while i < len(l1):
    key = l1[i]
    data = l2[j]
    s1[key] = data
    i += 1
    j += 1
print()
print(s1)
print()
