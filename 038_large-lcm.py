import sys
import math


def main():
    inputs = map(int, sys.stdin.read().strip().split(u' '))
    A, B = inputs

    lcm = math.lcm(A, B)

    if lcm > 10**18:
        print('Large')
    else:
        print(lcm)


if __name__ == '__main__':
    main()
