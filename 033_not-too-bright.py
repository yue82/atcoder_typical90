import sys
import math


def main():
    inputs = map(int, sys.stdin.read().strip().split(u' '))
    H, W = inputs

    if H == 1 or W == 1:
        print(H*W)
    else:
        print((math.ceil(H/2)) * (math.ceil(W/2)))

if __name__ == '__main__':
    main()
