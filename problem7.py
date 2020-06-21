"""


By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


"""

# getting factors of a number
def getFactors(number):
    factors = []
    for potentialFactor in range(1, number + 1):
        if number % potentialFactor == 0:
            factors.append(potentialFactor)
    return factors

# a way of determine if a number is prime
def isPrime(number):
    return len(getFactors(number)) == 2





prime = [2, 3, 5, 7, 13]
num = 15

while len(prime)<10001:
    if(isPrime(num) == True):
        prime.append(num)
    num+=2

print(prime[len(prime)-1])
