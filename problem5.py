"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""


n = 20
while True:
    for i in range(1, 21):
        if(i < 20 and i > 1 and n % i != 0):
            break

    if(i == 20):
        break
    else:
        n+=1
print(n)
