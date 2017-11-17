#!/usr/bin/env python

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    a = a % m # allows this to work with negative numbers
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def letter_to_number(c):
    return ord(c.lower()) - ord('a')

def number_to_letter(n):
    return chr(n % 26 + ord('a'))

def affine_encrypt(a, b, plaintext):
    def encrypt_letter(c):
        n = letter_to_number(c)
        return number_to_letter((a * n + b) % 26)
    return "".join([encrypt_letter(c) for c in plaintext])

def affine_decrypt(a, b, ciphertext):
    a_inv = modinv(a, 26)
    def decrypt_letter(c):
        n = letter_to_number(c)
        return number_to_letter((a_inv * (n - b)) % 26)
    return "".join([decrypt_letter(c) for c in ciphertext]).upper()

def print_ciphertext(ciphertext):
    print "\n==========="
    print "Ciphertext:"
    print "===========\n"
    print ciphertext

def print_plaintext(a, b, plaintext):
    header = "Plaintext (as decrypted by ({}, {})):".format(a, b)
    print "\n", "=" * len(header), "\n", header, "\n", "=" * len(header)
    print "\n", plaintext, "\n"

if __name__ == "__main__":
    ciphertext = "falszztysyjzyjkywjrztyjztyynaryjkyswarztyegyyj"
    print_ciphertext(ciphertext)
    plaintext = affine_decrypt(7, 22, ciphertext)
    print_plaintext(7, 22, plaintext)
    print "Q1.11.2 Answer: This was said by the Queen\n"

"""
Deciphered Plaintext:

FIRSTTHESENTENCEANDTHENTHEEVIDENCESAIDTHEQUEEN

"""
