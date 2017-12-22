#!/usr/bin/env python

one_bit = 7 # off by one so that bit 28 doesn't become bit 0 - is corrected via a +1 when used.

def find_one_bit_location_after_PC1(bit_position):
    map = dict(zip([
            14, 17, 11, 24, 1, 5, 3, 28,
            15, 6, 21, 10, 23, 19, 12, 4,
            26, 8, 16, 7, 27, 20, 13, 2
        ], range(1, 29)))
    return map[bit_position] if bit_position in map else None

for i in range(1,17):
    if i in [1, 2, 9, 16]:
        rotate = 1
    else:
        rotate = 2
    one_bit = (one_bit - rotate) % 28
    subkey_bit = find_one_bit_location_after_PC1(one_bit + 1)
    print "Round {}: 1-bit is occupying position {}\n\tAfter PC-2 this is subkey bit {}\n\twhich afects S-box {}\n".format(
        str(i).zfill(2),
        one_bit + 1,
        subkey_bit if subkey_bit else "N/A",
        ((subkey_bit - 1) / 6) + 1 if subkey_bit else "N/A"
    )
