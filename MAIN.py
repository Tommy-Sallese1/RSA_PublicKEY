import math
import random
from Primes import primes
from ComputeGCD import computeGCD

A = True
p = int(0)
q = int(0)
C = int(0)
m_num = int(0)
d = int(0)
p_prime = int(0)
q_prime = int(0)
N_prime = int(0)
pt = int(0)

#Randomly generate two primes that are 3 or 4 digits

p,q = primes(p,q)
N = p*q

#Create encryption exponent e and ensure it is valid
while C != 1:
    e = (random.randrange(5, 15, 1))
    p_prime = p - 1
    q_prime = q - 1
    N_prime = p_prime*q_prime
    C = computeGCD(e,N_prime)

# Find d, the inverse of e mod (p-1*q-1)
while A == True:
    if (((e*d)-1)%N_prime)==0:
        A = False
    elif d == N_prime:
        print("there is no inverse")
        break
    else:
        A = True
        d += 1

#Enter Plaintext and delete whitespace
m = input("input the text you wish to encrypt: ")
m = m.replace(" ","")
list2 = []
list3 = []
list4 = []
list5 = []

#Encrypt the plaintext
for letter in m:
    Z = ord(letter)
    list3.append(Z)
    c = (ord(letter)**e)%N
    list2.append(c)


#Decrypt ciphertext
for element in list2:
    G = ((element**d)%N)
    list4.append(G)

#Convert the numbers back to string using ascii
for item in list4:
    pt = chr(item)
    list5.append(pt)

print("p = ",p)
print("q = ",q)
print("e = ",e)
print("d = ",d)
print("The ciphertext {} decrypts as {}".format(list2,list5))





