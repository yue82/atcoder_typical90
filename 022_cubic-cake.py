import sys
import math


def main():
    inputs = list(map(int, sys.stdin.read().strip().split(' ')))
    A = inputs[0]
    B = inputs[1]
    C = inputs[2]

    gcd = math.gcd(A, B, C)

    print(A//gcd + B//gcd + C//gcd - 3)

if __name__ == '__main__':
    main()
