import sys
import math

bases = [9**p for p in range(20, 0, -1)]

def main():
    inputs = sys.stdin.read().strip().split(u' ')
    N, K = inputs

    s8 = N
    for k in range(int(K)):
        xs = ''
        s9 = base_9str(int(s8, 8))
        for ss9 in s9:
            if ss9 == '8':
                xs += '5'
            else:
                xs += ss9
        s8 = xs
    print(xs)

def base_9str(n):
    global bases
    s = ''
    while n > 0:
        q = n // 9
        m = n % 9
        s += str(m)
        n = q
    if len(s) == 0:
        return '0'
    return s[::-1]

if __name__ == '__main__':
    main()
