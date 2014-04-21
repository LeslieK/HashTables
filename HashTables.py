"""
4-SUM. Given an array a[] of N integers, the 4-SUM problem is to determine
if there exist distinct indices i, j, k, and l such that a[i]+a[j]=a[k]+a[l].
Design an algorithm for the 4-SUM problem that takes time proportional to N2
(under suitable technical assumptions).

"""
import random
LENGTHARRAY = 20

count = LENGTHARRAY
a = []
while count > 0:
    a.append(random.choice(range(100)))
    count -= 1

print(a)

import itertools


def FOUR_SUM(a):
    st = set()
    pairs = [(i, j) for i, j in itertools.combinations(range(LENGTHARRAY), 2)]
    for i, j in pairs:
        tot = a[i] + a[j]
        if tot in st:
            return True
        else:
            st.add(tot)
    return False

print(FOUR_SUM(a))

# brute force
#n = len(a)
#b = [(i, j, k, l) for i in range(n) \
#    for j in range(n) if j > i \
#    for k in range(n) if k > i if k != j\
#    for l in range(n) if l > k if l != j]
#print(len(b))
#print(b)

"""
Hashing with wrong hashCode() or equals().
Suppose that you implement
a data type OlympicAthlete for use in a java.util.HashMap.

a1 = OlympicAthlete()
a2 = OlympicAthlete()

equals() and hashCode() must be consistent:
case 1: if a1.equals(a2) is True => a1.hashCode() == a2.hashCode() is True
case 2: if a1.hashCode() != a2.hashCode() => a1.equals(a2) is False
case 3: if a1.hashCode() == a2.hashCode() is True => must check equality with
equals()

Q: Describe what happens if you override hashCode() but not equals().
A: case 3 will not give the answer you expect (equals tests for equal-identity)

Q: Describe what happens if you override equals() but not hashCode().
A: a1.hashCode() returns memory address of a1 so a1.hashCode() will never equal
a2.hashCode() even if a1 equals a2 case 1 and case 2 will fail

Q: Describe what happens if you override hashCode() but implement
public boolean equals(OlympicAthlete that)
instead of
public boolean equals(Object that).
A: equals must be able to compare objects of different classes
if keys are of different data types; equals must accept NULL as an argument
"""

"""
Ex. 3.4.4
(a * k) % M to transform kth letter of alphabet to index
no collisions
"""
data = list('SEARCHXMPL')
import string
letters = string.ascii_uppercase
keys = []
it = map(letters.find, keys)
for i in it:
    keys.append(i)
print(keys)


