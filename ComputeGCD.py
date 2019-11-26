def computeGCD(p, q):

    if p > q:
        small = q
    else:
        small = p
    for i in range(1, small+1):
        if((p % i == 0) and (q % i == 0)):
            gcd = i

    return gcd

