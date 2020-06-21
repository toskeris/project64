import math as m


"""

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""


a = 1
b = 1
k = 1000

while a + b + m.sqrt(a**2 + b**2) !=k:
    if a + b + m.sqrt(a**2 + b**2) > k:
        a += 1
        b = 1
    else:
        b += 1


c = int(m.sqrt(a**2 + b**2))

print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"The product abc is {a * b * c}")
