#!/usr/bin/env python
import time

class LFSR(object):

    def __init__(self, reg_len, feedback, feedforward):
        self.registers = [0] * reg_len
        self.feedback = feedback
        self.feedforward = feedforward

    def initialise_registers(self, init_vector):
        self.registers = [int(a) for a in list(bin(init_vector).lstrip("-0b").zfill(len(self.registers)))]

    def get_output_bit(self):
        return (self.registers[-1] + self._get_feedforward_output() + self._get_and_output()) % 2

    def iterate(self, input_bit):
        self.registers.pop()
        self.registers.insert(0, (input_bit + self._get_feedback_output()) % 2)

    def _get_and_output(self):
        return self.registers[-3] * self.registers[-2]

    def _get_feedback_output(self):
        return self.registers[self.feedback]

    def _get_feedforward_output(self):
        return self.registers[self.feedforward]

class Trivium(object):

    def _fix_offset_for_init_vector(self, init_vector):
        # TODO: Fix this so that it initialises the leftmost 70 bits as per spec
        return init_vector

    def __init__(self, init_vector, key):
        self.a = LFSR(93, 68, 65)
        self.b = LFSR(84, 77, 68)
        self.c = LFSR(111, 86, 65)
        self.a.initialise_registers(init_vector)
        self.b.initialise_registers(key)
        self.c.initialise_registers(7)

    def show_internal_state(self):
        print "A:\n", self.a.registers, "\nOutput bit:", self.a.get_output_bit(), "\n"
        print "B:\n", self.b.registers, "\nOutput bit:", self.b.get_output_bit(), "\n"
        print "C:\n", self.c.registers, "\nOutput bit:", self.c.get_output_bit(), "\n"

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
    keystream_generator = Trivium(0, 0)
    while True:
        keystream_generator.show_internal_state()
        print keystream_generator.get_output_bit()
        keystream_generator.iterate()
        time.sleep(0.1)
