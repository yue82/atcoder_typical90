import sys
import itertools


# TLE したので解説を見て、尺取法にした
def main():
    inputs = [list(map(int, line.split(u' ')))
              if u' ' in line.strip() else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]
    N = inputs[0]
    A = inputs[1] if N > 1 else [inputs[1]]

    s = sum(A)
    if s < 10 or s % 10 != 0:
        print('No')
        return

    ring = lambda x: x if x < N else x - N

    t = s // 10
    l, r = 0, 0
    sa = A[l]
    while l < N:
        while sa < t:
            r += 1
            sa += A[ring(r)]
        if sa == t:
            print('Yes')
            return
        sa -= A[l]
        l += 1
    print('No')

if __name__ == '__main__':
    main()
