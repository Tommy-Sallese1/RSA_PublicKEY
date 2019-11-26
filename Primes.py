import math
import random

#Randomly generate two primes that are 3 or 4 digits

p = int(0)
q = int(0)
def primes(p,q):
    #generate the first prime
    count = 3
    #create a list of all primes from 3 to 10000
    list = []
    #generat the list positions that are to be selected, they cannot
    #be the same
    A = (random.randrange(30, 122, 1))
    B = (random.randrange(30, 122, 1))
    if A == B:
        while A == B:
            B = (random.randrange(30, 122, 1))
    while True:
        isprime = True
        if count > 9999:
            p = list[A]
            q = list[B]
            break
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                isprime = False
                break

        if isprime:
            list.append(count)
        count += 1

    return p,q