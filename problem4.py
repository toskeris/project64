"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""



def palindromic(n):
    nstring = str(n)
    pstring = ""
    for i in range(0, len(nstring)):
        pstring += nstring[len(nstring)-1-i]
    return nstring == pstring


a = 100

palindromic_num = 101



while(a < 1000):
    for b in range(0, 1000):
        c=a*b
        if palindromic(c) == True and c > palindromic_num:
            palindromic_num = c
    a+=1

print("The largest palindromic number is %d" % palindromic_num)
