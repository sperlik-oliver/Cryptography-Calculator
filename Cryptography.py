
p = int (input("\n\n\nEnter p [Enter 0 if not needed]: "))
q = int (input("Enter q [Enter 0 if not needed]: "))
e = int (input("Enter e (public key): "))
n = int (input("Enter n (modulus)[Enter 0 for automatic calculation]: "))
d = int (input("Enter d (private key) [Enter 0 for automatic calculation or 1 if not needed]: "))
fi = int (input("Enter Fi(n) [Enter 0 for automatic calculation or 1 if not needed]: "))
m = int (input("Enter message [Enter 4 if not needed] : "))
import time


def __gcd(x, y):
 
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
              
    return gcd
 

def coprime(a, b):
     
    if ( __gcd(a, b) == 1):
        return True
    

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def rsaEncrypt(p, q, e, n, fi, m):
    print("\n\n\n RSA Encrypt:")
    if (n == 0):
        n = p * q   
        print("\n N = p * q: ", n)
    if (fi == 0):
        fi = (p - 1) * (q - 1)
        print("\n Fi(n) = (p-1) * (q-1): ", fi)
    if (e == 0):
        e = 11
        print("\ne: ", e)
    c = (m**e) % n
    print("\n c = (m**e) % n: ", c)
    return c

def rsaDecrypt(c, p, q, e, n, fi, m, d):
    print("\n\n\n RSA Decrypt:")
    if (n == 0):
        n = p * q
        print("\n N = p * q: ", n)
    if (fi == 0):
        fi = (p - 1) * (q - 1)
        print("\n Fi(n) = (p-1) * (q-1): ", fi)
    if (d == 0):
        d = modinv(e, fi)
        print("\n d = e modinv fi(n): ", d)
    m = c**d % n
    print("\n m = c**d % n: ", m, "\n\n\n")
    return m


c = rsaEncrypt(p, q, e, n, fi, m)
rsaDecrypt(c, p, q, e, n, fi, m, d)






