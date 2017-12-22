#!/usr/bin/env python
import collections, re

def get_ciphertext_letters_by_frequency(ciphertext):
    ciphertext_nopunc = re.sub(r"\W+", "", ciphertext)
    letter_freqs = collections.Counter(ciphertext_nopunc)
    return [i[0] for i in letter_freqs.most_common()]

def reconstruct_key(ciphertext_letters):
    letters_ordered_by_freq = ["E","T","A","O","I","N","S","R","H","D","L",
        "U","C","M","F","Y","W","G","P","B","V","K","X","Q","J","Z"]
    return zip(ciphertext_letters, letters_ordered_by_freq)

def get_manually_tweaked_key():
    # The statistical analysis produced a plaintext that was still garbled
    # but certain words stood out. I swapped these mismatches manually until
    # the true plaintext revealed itself. This was very easy given the
    # headstart provided by the statistical analysis
    return [
        ('r', 'E'), ('b', 'T'), ('m', 'A'),
        ('k', 'N'), ('j', 'O'), ('w', 'I'),
        ('i', 'S'), ('p', 'H'), ('u', 'R'),
        ('d', 'D'), ('h', 'L'), ('v', 'C'),
        ('x', 'F'), ('y', 'M'), ('n', 'U'),
        ('s', 'P'), ('t', 'Y'), ('l', 'B'),
        ('o', 'G'), ('q', 'K'), ('a', 'X'),
        ('c', 'W'), ('e', 'V'), ('g', 'Z'),
        ('f', 'Q')
    ]

def decipher(ciphertext, key):
    for x, y in key:
        ciphertext = ciphertext.replace(x, y)
    return ciphertext

def print_ciphertext(ciphertext):
    print "\n==========="
    print "Ciphertext:"
    print "==========="
    print ciphertext

def print_deciphered_plaintext(type, key, plaintext):
    header = "{} Statistical Key Reconstruction:".format(type)
    print "=" * len(header), "\n", header, "\n", "=" * len(header)
    print "\n", "Key:", "\n"
    key.sort(key=lambda x: x[1])
    i = 0
    for x, y in key:
        print "{} = {},".format(y, x),
        i += 1
        if not i % 5: print
    print "\n", plaintext

with open("ex1.1-ciphertext.txt") as f:
    ciphertext = f.read()
    print_ciphertext(ciphertext)
    ciphertext_letters = get_ciphertext_letters_by_frequency(ciphertext)
    key = reconstruct_key(ciphertext_letters)
    print_deciphered_plaintext("Naive", key, decipher(ciphertext, key))
    key = get_manually_tweaked_key()
    print_deciphered_plaintext("Manually Tweaked", key, decipher(ciphertext, key))
    print "Q1.1.3 Answer: This was said by Shoshin Nagamine", "\n"


"""
Recovered Plaintext:

BECAUSE THE PRACTICE OF THE BASIC MOVEMENTS OF KATA IS
THE FOCUS AND MASTERY OF SELF IS THE ESSENCE OF
MATSUBAYASHI RYU KARATE DO I SHALL TRY TO ELUCIDATE THE
MOVEMENTS OF THE KATA ACCORDING TO MY INTERPRETATION
BASED ON FORTY YEARS OF STUDY

IT IS NOT AN EASY TASK TO EXPLAIN EACH MOVEMENT AND ITS
SIGNIFICANCE AND SOME MUST REMAIN UNEXPLAINED TO GIVE A
COMPLETE EXPLANATION ONE WOULD HAVE TO BE QUALIFIED AND
INSPIRED TO SUCH AN EXTENT THAT HE COULD REACH THE STATE
OF ENLIGHTENED MIND CAPABLE OF RECOGNIZING SOUNDLESS
SOUND AND SHAPELESS SHAPE I DO NOT DEEM MYSELF THE FINAL
AUTHORITY BUT MY EXPERIENCE WITH KATA HAS LEFT NO DOUBT
THAT THE FOLLOWING IS THE PROPER APPLICATION AND
INTERPRETATION I OFFER MY THEORIES IN THE HOPE THAT THE
ESSENCE OF OKINAWAN KARATE WILL REMAIN INTACT

"""
