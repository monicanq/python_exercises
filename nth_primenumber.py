from sympy import isprime

def findPrime (n):
    primeAmount = 0
    primecheck = 1
    while True:
        if isprime(primecheck):
            primeAmount +=1
        if primeAmount >= n:
            return (primecheck)
        primecheck += 1

n = input ('Tell me the order of the prime number you are looking for: ')
print('The prime number with order ' + str(n) + ' is ' + str(findPrime(int(n))))
