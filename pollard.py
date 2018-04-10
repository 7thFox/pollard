import sys

def powMod(p,k,N):
    """
    powMod computes p^k mod N using rapid modular exponentiation.

    Args:
        p (int): The number to be exponentiated.
        k (int): The exponental.
        N (int): The modulus.

    Returns:
        The integer result.
    """
    acc = 1
    r = 0
    for s in range(0,65):
        if s == 0:
            r = p
        else:
            r = (r**2) % N
        kk = 2**s

        if k & (0x01 << s):
            acc = (acc * r) % N

        if 2**(s+1) > k:
            break
    return acc % N
        

def twoExpBFactModN(N, B):
    """
    twoExpBFactModN computes 2^(B!) mod N.

    Args:
        N (int): The modulus.
        B (int): The factorial exponent.

    Returns:
        The integer result.
    """
    ck = 2
    for k in range(1,B+1):
        ck = powMod(ck,k,N)
    return ck

def gcd(a,b):
    """
    gcd computes the greatest common denominator of the two given numbers
    using Euclid's algorithm.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        The integer result.
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def factor(N, B=100, Bmax=1000000, printB=False):
    """
    factor factorizes a given number using the Pollard p-1 attack.

    Args:
        N (int): The number to be factored.

        B      (int  optional): The starting value of B.
        Bmax   (int  optional): The maximum value of B before factorization is aborted.
        printB (bool optional): Option to print the values of B being tested.
    
    Returns:
        The factors, p and q. If there is an error, such as the factorization being
        aborted due to a low Bmax, then the factor(s) will be less than zero.
    """
    def debugPrint(s):
        if printB:
            print(s)

    lastB = 0
    while True:
        if B == lastB:
            return -1, -1
        debugPrint(f"trying B = {B}...")
        k = twoExpBFactModN(N,B)
        phi = (k-1) % N
        if phi == 0:
            debugPrint("too big.")
            lastB, B = B, B - abs(B-lastB)//2
            continue

        g = gcd(phi, N)
        if g == 1:
            debugPrint("too small.")
            lastB, B = B, min(B*2, Bmax)
        else:
            return g, N//g

if __name__ == "__main__":
    # Test Values:
    # p = 1237
    # q = 5683
    # N = 7029871
    # e = 15
    # d = 6561213

    N = int(input("Please enter N: "))
    e = int(input("Please enter e: "))

    p,q = factor(N)

    if p < 0 or q < 0:
        print("Could not attack keys.")
        sys.exit(1)

    phi = (p-1)*(q-1) - 1
    d = powMod(e, phi, N)
    privateKey = (d, N)

    print(f"Private Key (d, N): {privateKey}")