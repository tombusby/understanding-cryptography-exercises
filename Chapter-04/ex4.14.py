#!/usr/bin/env python

# This is backwards compared with the book because it is easier to
# do this than reverse the input bits
matrix = [
    0b11110001,
    0b11100011,
    0b11000111,
    0b10001111,
    0b00011111,
    0b00111110,
    0b01111100,
    0b11111000,
]


def affine_mapping(byte):
    output = []
    for row in matrix:
        new_row = bin(row & byte).lstrip("-0b")
        output.insert(0, str(new_row.count('1') % 2))
    return int("".join(output), 2) ^ 0b01100011


if __name__ == "__main__":
    print "S(26):", hex(affine_mapping(0xA8)).lstrip("-0x").zfill(2).upper()
    print "S(F3):", hex(affine_mapping(0x34)).lstrip("-0x").zfill(2).upper()
    print "S(01):", hex(affine_mapping(0x01)).lstrip("-0x").zfill(2).upper()
