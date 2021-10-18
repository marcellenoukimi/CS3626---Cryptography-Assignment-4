# Course ID:        CS3626
# Course name:      Cryptography
# Student name:     Marcelle Kembou Noukimi
# StudentID:        001024342
# Assignment #:     #4
# Due Date:         04/30/2021

import random
from random import randint


# This function helps in finding the GCD of two numbers
def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)


# This is the function to calculate the multiplicative inverse
def multiplicativeInverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1


# Here we initialize two random numbers p and q from range 1 to 100
p = randint(1, 100)
q = randint(1, 100)


# This function helps to generate the public/private key pair
def KeyGen(p, q):
    # The keysize is the bit length of n comprised in the in range(nMin,nMax+1).
    keysize = 2 ** 5

    # This helps to make p and q having similar bit length.
    nMin = 1 << (keysize - 1)
    nMax = (1 << keysize) - 1

    # Array of prime numbers
    primesArr = [2]
    # Here we pick two primes in range(start, stop) in such a way that
    # 2 is the maximum difference of the bit lengths.
    start = 1 << (keysize // 2 - 1)
    stop = 1 << (keysize // 2 + 1)

    if start >= stop:
        return []

    for i in range(3, stop + 1, 2):
        for p in primesArr:
            if i % p == 0:
                break
        else:
            primesArr.append(i)

    while primesArr and primesArr[0] < start:
        del primesArr[0]

    # Here we pick two large primes p and q from the generated prime numbers such that p!=q.
    while primesArr:
        p = random.choice(primesArr)
        primesArr.remove(p)
        qPrime = [q for q in primesArr if nMin <= p * q <= nMax]
        if qPrime:
            q = random.choice(qPrime)
            break

    # This prints the primes randomly selected
    print(p, ",", q)
    n = p * q
    phi = (p - 1) * (q - 1)

    # In this part, we select randomly a public key 'e' such that 1<e<phi(n) and gcd(e,phi(n))=1
    e = random.randrange(1, phi)
    g = gcd(e, phi)

    # Here we keep generating 'e' until gcd(e,phi(n))=1
    while True:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
        # Here we calculate the private key d
        d = multiplicativeInverse(e, phi)
        if g == 1 and e != d:
            break

    # Public key PU=(e,n)
    PU = (e, n)
    # Private key PR = (d, n)
    PR = (d, n)
    return PU, PR


# This function is to encrypt a message sent to a user
def RSAEncryption(M, PU):
    # This to unpack the PU=(e,n) pair
    e, n = PU
    # Encrypt: C= m^e mod n
    C = [pow(ord(m), e, n) for m in M]
    return C


# This function is to decrypt the ciphertext generated during the encryption
def RSADecryption(C, PR):
    # This to unpack the PR=(d,n) pair
    d, n = PR
    # Decrypt: M= c^d mod n
    M = [chr(pow(c, d, n)) for c in C]
    # This is to cast the decrypted message, M, back
    # to character to be concatenate in a string value for the final output.
    M = (''.join(M))
    return M


# Text codes of RSA Digital Signature
def digitalSignature(msg, PU, PR):
    print("\nRSA Digital Signature Scheme")
    e, n = PU
    d, n = PR
    # Digital signature created by Alice to send the message: S= M^d mod n, M is the message.
    S = [pow(ord(m), d, n) for m in msg]
    print("Digital signature created and sent by Alice to Bob:", S)
    # Computation M1= S^e mod n made by Bob
    M1 = [chr(pow(s, e, n)) for s in S]
    M1 = (''.join(M1))
    print("Message sent by Alice as M=", msg)
    print("Bob's computation as M1=", M1)
    if msg == M1:
        print("Because M=M1, Bob accepts the message sent by Alice.")
    else:
        print("Because M is different from Ma, Bob does not accept the message sent by Alice.")


# Main program to test RSA Algorithm and Digital Signature.
if __name__ == "__main__":
    # Test of RSA encryption/decryption algorithm
    print("RSA Encryption/Decryption Algorithm")
    print("Value of p and q randomly generated for public and private keypair: ", end=" ")
    PU, PR = KeyGen(p, q)
    print("Public Key: ", PU)
    print("Private Key: ", PR)
    msg = input("Enter a message to test this RSA Algo: ")
    print("'", msg, "' is converted to a list of characters:", list(msg))
    print("The list of characters is converted to a list of decimals as per ASCII code:", [ord(c) for c in msg])
    encrypted_msg = RSAEncryption(msg, PU)
    print("Encrypted message: ", end=" ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypted message: ", end=" ")
    print(RSADecryption(encrypted_msg, PR))

    # Test of RSA Digital Signature
    digitalSignature(msg, PU, PR)
