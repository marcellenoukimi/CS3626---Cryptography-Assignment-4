# CS3626---Cryptography-Assignment-4
**Problems:**

The aim of this assignment is to implement the RSA algorithm. Specifically, the
implementation should include the following functions:

**1. KeyGen(p,q) → PU = (e,n), PR = (d,n) – 40 points**

The key generation function takes as input two prime numbers and outputs a public/private
key pair. Let’s assume that the prime numbers are smaller than 100(10).

**2. RSA(M,PU) → C, or RSA(C,PR) → M – 20 points**

The encryption function (note that RSA uses the same function for both encryption and
decryption) takes as input a plaintext and a public key then outputs a ciphertext. Also, it takes
as input a ciphertext and a private key then outputs a plaintext.

Hint: To find a multiplicative inverse, you may use a brute-force strategy.

Note: For all other requirements and specifications not defined here, please refer to them in
the textbook.

**3. Combining with Assignment 1 – 20 points**

Improve your implementation for 1 by using your Text Converter, so it can handle a string
from a user and output a string.

Hint: you can execute the RSA function once for each letter, i.e., the plaintext “hello” needs
five executions. For example, the input “hello” will be encrypted as follows:

(a) “hello” is converted to a list of characters: [‘h’,’e’,’l’,’l’,’o’]

(b) the list of characters is converted to a list of decimals as per ASCII code: [104, 101, 108,
108, 111]

(c) each decimal in the list is encrypted by the “RSA” function implemented for 2.

**4. make some text codes of “Encryption” and “Digital Signature” to demonstrate the
validity of the implementation – 10 points**
