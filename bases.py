#!python
# bases.py
#
# Author: Nyein Chan Aung @ 2019
#
import string
import time

def timer(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        print(func(*args, **kwargs))
        print(f'---->{time.time() - time_start}<----')
    return wrapper

ALPHA = string.ascii_lowercase
ALPHA_HASH = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r'
: 27, 's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35}

# @timer
def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    assert 2 <= base1 <= 36, f'base1 is out of range: {base1}'
    assert 2 <= base2 <= 36, f'base2 is out of range: {base2}'
    converstion = ""
    if base1 == 10:
        while int(digits) >= base2 or int(digits) >= 10:
            digits = int(digits)
            if len(str(digits%base2)) == 2 and base2 >= 11: 
                converstion += f'{ALPHA[int(digits%base2)-10]}'
                digits/=base2
            else: 
                converstion += f'{int(digits%base2)}'
                digits/=base2
    else:
        digits = digits[::-1]
        converstion += str(sum([int(digits[power])*(base1**int(power)) if digits[power].isdecimal() else int(ALPHA_HASH[digits[power].lower()])*(base1**int(power)) for power in range(len(digits))]))
        return convert(converstion, 10, base2)
    if int(digits):
        converstion += f'{int(digits)}'
    return converstion[::-1]


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print(f'{digits} in base {base1} is {result} in base {base2}')
    else:
        print(f'Usage: {sys.argv[0]} digits base1 base2')
        print(f'Converts digits from base1 to base2')


if __name__ == '__main__':
    main()