__author__ = 'student'

i= [1, 3, 4, 6]

print "pythonic: "

for element in reversed(i):
    print element


print "Non pyhonic"

for j in range(0, len(i)):
    print i[j]

print i
