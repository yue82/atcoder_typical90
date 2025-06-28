import sys
import math


def main():
    inputs = [int(s) for s in sys.stdin.read().strip().split(u' ')]
    N = inputs[0]

    divs = []
    n = N
    for i in range(2, math.ceil(N**0.5)+1):
        while n % i == 0:
            divs.append(i)
            n //= i
        if n == 1:
            break
    if n != 1:
        divs.append(n)

    divnum = len(divs)
    if divnum == 0:
        print(0)
        return
    i = 0
    b = 1
    while b < divnum:
        i += 1
        b += b
    print(i)

if __name__ == '__main__':
    main()
