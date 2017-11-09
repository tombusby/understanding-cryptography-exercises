#!/usr/bin/env python
import collections, re, operator

def get_ciphertext_letters_by_frequency(ciphertext):
    ciphertext_nopunc = re.sub(r"\W+", "", ciphertext)
    letter_freqs = collections.Counter(ciphertext_nopunc)
    return [i[0] for i in letter_freqs.most_common()]

def reconstruct_key(ciphertext_letters):
    letters_ordered_by_freq = ["E","T","A","O","I","N","S","R","H","D","L",
        "U","C","M","F","Y","W","G","P","B","V","K","X","Q","J","Z"]
    return zip(ciphertext_letters, letters_ordered_by_freq)

def get_manually_tweaked_key():
    return [
        ('r', 'E'),
        ('b', 'T'),
        ('m', 'A'),
        ('k', 'N'),
        ('j', 'O'),
        ('w', 'I'),
        ('i', 'S'),
        ('p', 'H'),
        ('u', 'R'),
        ('d', 'D'),
        ('h', 'L'),
        ('v', 'C'),
        ('x', 'F'),
        ('y', 'M'),
        ('n', 'U'),
        ('s', 'P'),
        ('t', 'Y'),
        ('l', 'B'),
        ('o', 'G'),
        ('q', 'K'),
        ('a', 'X'),
        ('c', 'W'),
        ('e', 'V'),
        ('g', 'Z'),
        ('f', 'Q')
    ]

def decipher(ciphertext, key):
    for x, y in key:
        ciphertext = ciphertext.replace(x, y)
    return ciphertext

def print_deciphered_plaintext(type, key, plaintext):
    header = "{} Statistical Key Reconstruction:".format(type)
    print "=" * len(header), "\n", header, "\n", "=" * len(header)
    print "\n", "Key:", "\n"
    key.sort(key=lambda x: x[1])
    for x, y in key:
        print "{} = {}".format(y, x)
    print plaintext

with open("ex1.1-ciphertext.txt") as f:
    ciphertext = f.read()
    ciphertext_letters = get_ciphertext_letters_by_frequency(ciphertext)
    key = reconstruct_key(ciphertext_letters)
    print_deciphered_plaintext("Naive", key, decipher(ciphertext, key))
    key = get_manually_tweaked_key()
    print_deciphered_plaintext("Manually Tweaked", key, decipher(ciphertext, key))
