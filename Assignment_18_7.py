"""
Write a python program to create three dictionaries, 
then create one dictionary that
will contain the other three dictionaries. 
"""

s1 = {100 : 'Jayesh', 200 : 'Sonal'}
s2 = {300 : 'Hitesh', 400 : 'Nilesh'}
s3 = {500 : 'Paresh', 600 : 'Piyush'}
s4 = {}
for i in s1:
    s4.setdefault(i, s1[i])
for j in s2:
    s4.setdefault(j, s2[j])
for k in s3:
    s4.setdefault(k, s3[k])

print()
print(s4)
print()
