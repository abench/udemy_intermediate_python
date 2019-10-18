# TASK:
#
# Create a generator that generates a tuple of two random numbers and returns them
#
# Create another generator that calls the first generator and returns each of the generated elements one at a time! (Hint: You may need two yield statements here.)
#
# Use this second generator in main code.
import random

def rr():

    yield random.random(), random.random()


def r():
    ra,rb = next(rr())
    yield ra
    yield rb


if __name__ == "__main__":
    print("Attempt 1: ", next(r()))
    print("Attempt 2: ", next(r()))
    print("Attempt 3: ", next(r()))