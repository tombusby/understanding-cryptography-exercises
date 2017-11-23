#!/usr/bin/env python
import time

class LFSR(object):

    def __init__(self, reg_len, feedback, feedforward):
        self.registers = [0] * reg_len
        self.feedback = feedback
        self.feedforward = feedforward

    def initialise_registers(self, init_vector):
        self.registers = [0] * (len(self.registers) - len(init_vector)) + init_vector

    def get_output_bit(self):
        return (self.registers[-1] + self._get_feedforward_output() + self._get_and_output()) % 2

    def iterate(self, input_bit):
        self.registers.pop()
        self.registers.insert(0, (input_bit + self._get_feedback_output()) % 2)

    def show_internal_state(self):
        print self.registers
        print "Output bit:", self.get_output_bit(), "\nFeedBack bit:", self._get_feedback_output(), "\n"

    def _get_and_output(self):
        return self.registers[-3] * self.registers[-2]

    def _get_feedback_output(self):
        return self.registers[self.feedback]

    def _get_feedforward_output(self):
        return self.registers[self.feedforward]

class Trivium(object):

    def __init__(self, init_vector, key):
        self.a = LFSR(93, 68, 65)
        self.b = LFSR(84, 77, 68)
        self.c = LFSR(111, 86, 65)
        self.a.initialise_registers(init_vector + [0] * 13)
        self.b.initialise_registers(key + [0] * 4)
        self.c.initialise_registers([1, 1, 1])

    def show_internal_state(self):
        print "A:"
        self.a.show_internal_state()
        print "B:"
        self.b.show_internal_state()
        print "C:"
        self.c.show_internal_state()

    def get_output_bit(self):
        return (self.a.get_output_bit() + self.b.get_output_bit() + self.c.get_output_bit()) % 2

    def iterate(self):
        a_output = self.a.get_output_bit()
        b_output = self.b.get_output_bit()
        c_output = self.c.get_output_bit()
        self.a.iterate(c_output)
        self.b.iterate(a_output)
        self.c.iterate(b_output)

if __name__ == "__main__":
    keystream_generator = Trivium([], [])
    bits = []
    for i in range(0,70):
        bits.append(keystream_generator.get_output_bit())
        keystream_generator.iterate()
    print bits
    print len(bits)
