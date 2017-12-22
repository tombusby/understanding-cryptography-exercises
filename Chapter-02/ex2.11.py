#!/usr/bin/env python
import string, re

def bit_encoding_map():
    return zip(string.ascii_lowercase + string.digits, range(0, 32))

def bitencode(text):
    def encode_char(c):
        map = dict(bit_encoding_map())
        return bin(map[c.lower()]).lstrip("-0b").zfill(5)
    return "".join([encode_char(c) for c in text])

def bitdecode(text):
    def decode_block(bits):
        map = dict([(b, a) for a, b in bit_encoding_map()])
        return map[int(bits, 2)].upper()
    return "".join([decode_block(bits) for bits in re.findall(".{1,5}", text)])

# This was discovered by performing Gaussian Elimination on the discovered keystream
# There is a generalised algo for solving Guassian Elimination that could have produced
# this function in an automated way
def lfsr(init_vector):
    registers = list(bin(init_vector).lstrip("-0b").zfill(6)[-6:])
    while True:
        registers.insert(0, "1" if registers[-1] != registers[-2] else "0")
        yield registers.pop()

def xor_bitstream(a, b):
    return "".join(["1" if a != b else "0" for a, b in zip(a, b)])

def apply_keystream(lfsr_init_vector, text):
    return bitdecode(xor_bitstream(lfsr(lfsr_init_vector), bitencode(text)))

def print_ciphertext_and_chosen_plaintext(ciphertext, chosen_plaintext):
    print "\n==========="
    print "Ciphertext:"
    print "===========\n"
    print ciphertext
    print "\n================="
    print "Chosen Plaintext:"
    print "=================\n"
    print chosen_plaintext

def print_keystream(keystream):
    print "\n==================="
    print "Revealed keystream:"
    print "===================\n"
    print keystream

def print_decrypted_message(plaintext):
    print "\n==================="
    print "Revealed plaintext:"
    print "===================\n"
    print plaintext, "\n"

if __name__ == "__main__":
    ciphertext = "j5a0edj2b"
    chosen_plaintext = "WPI"
    lfsr_init_vector = 63
    keystream = xor_bitstream(bitencode(ciphertext), bitencode(chosen_plaintext))
    plaintext = apply_keystream(lfsr_init_vector, ciphertext)
    print_ciphertext_and_chosen_plaintext(ciphertext, chosen_plaintext)
    print_keystream(keystream)
    print_decrypted_message(plaintext)
