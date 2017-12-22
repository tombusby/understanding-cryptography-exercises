#!/usr/bin/env python
import string, collections, re

def generate_key(rot):
    return zip(string.ascii_lowercase, string.ascii_uppercase[rot:] + string.ascii_uppercase[:rot])

def get_ciphertext_letters_by_frequency(ciphertext):
    ciphertext_nopunc = re.sub(r"\W+", "", ciphertext)
    letter_freqs = collections.Counter(ciphertext_nopunc)
    return [i[0] for i in letter_freqs.most_common()]

def decipher(ciphertext, rot):
    key = generate_key(rot)
    for x, y in key:
        ciphertext = ciphertext.replace(x, y)
    return ciphertext

# The keyspace is small enough (knowing that it's a shift cipher) for brute force
def brute_force(ciphertext):
    print "\n=================="
    print "Brute Force Attack"
    print "==================\n"
    for rot in range(1, 26):
        arrow = "<========== CORRECT" if rot == 11 else ""
        print "{rot:02d}: ".format(rot=rot), decipher(ciphertext, rot), arrow

# Here follows a statistical attempt to find the key
def statistical_attack(ciphertext):
    print "\n=================="
    print "Statistical Attack"
    print "==================\n"
    most_common_letter = get_ciphertext_letters_by_frequency(ciphertext)[0]
    rot = (ord('e') - ord(most_common_letter)) % 26
    print decipher(ciphertext, rot), "\n"

if __name__ == "__main__":
    ciphertext = "xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpitghlxiwiwtxgqadds."
    brute_force(ciphertext)
    statistical_attack(ciphertext)
    print "Q1.2.2 Answer: This was said by Tecumseh\n"

"""
Recovered Plaintext:

IFWEALLUNITEWEWILLCAUSETHERIVERSTOSTAINTHEGREATWATERSWITHTHEIRBLOOD.

"""
