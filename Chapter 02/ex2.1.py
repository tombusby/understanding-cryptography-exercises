#!/usr/bin/env python

def letter_to_number(c):
    return ord(c.lower()) - ord('a')

def number_to_letter(n):
    return chr(n % 26 + ord('a'))

def encrypt_letter(key, plaintext):
    if plaintext == " ": return plaintext
    key = letter_to_number(key)
    plaintext = letter_to_number(plaintext)
    return number_to_letter((plaintext + key) % 26)

def decrypt_letter(key, ciphertext):
    if ciphertext == " ": return ciphertext
    key = letter_to_number(key)
    ciphertext = letter_to_number(ciphertext)
    return number_to_letter((ciphertext - key) % 26)

def encrypt(key, plaintext):
    return "".join(encrypt_letter(k, p) for (k, p) in zip(key, plaintext))

def decrypt(key, ciphertext):
    return "".join(decrypt_letter(k, c) for (k, c) in zip(key, ciphertext))

def print_ciphertext_and_key(key, ciphertext):
    print "\n===="
    print "Key:"
    print "====\n"
    print key
    print "\n==========="
    print "Ciphertext:"
    print "===========\n"
    print ciphertext

def print_plaintext(plaintext):
    print "\n=========="
    print "Plaintext:"
    print "==========\n"
    print plaintext, "\n"

if __name__ == "__main__":
    ciphertext = "bsaspp kkuosp"
    key = "rsidpy dkawoy" # mistake in the key in the book, should end with y not a
    print_ciphertext_and_key(key, ciphertext)
    plaintext = decrypt(key, ciphertext)
    print_plaintext(plaintext)
    print "Q2.1.3: Kaspar Hauser was murdered via a stab wound\n"
