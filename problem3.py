"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


"""

number  = 600851475143




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


factors = getFactors(number)

