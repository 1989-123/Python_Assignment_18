"""
Write a python program to merge two python dictionaries 
into one dictionary. 
"""

d1 = { 100 : 'Jayesh', 200 : 'Hitesh'}
d2 = { 300 : 'Paresh', 400 : 'Nilesh'}
d3 = {}
for e in d1:
    d3.setdefault(e, d1[e])
for k in d2:
    d3.setdefault(k, d2[k])

print()
print(d3)
print()
