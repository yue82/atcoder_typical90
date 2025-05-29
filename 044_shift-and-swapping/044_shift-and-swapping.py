import sys


# 1回 TLE してからシフトの解説を見た
def main():
    inputs = [list(map(int, line.split(u' ')))
              if u' ' in line.strip() else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]
    N, Q = inputs[0]
    A = inputs[1]
    TXY = inputs[2:] if Q > 1 else [inputs[2]]

    shift = 0
    for t, x, y in TXY:
        x, y = x-1, y-1
        if t == 1:
            fx, fy = fix(x, shift, N), fix(y, shift, N)
            tmp = A[fx]
            A[fx] = A[fy]
            A[fy] = tmp
        elif t == 2:
            shift += 1
            if shift == N:
                shift = 0
        else:
            print(A[fix(x, shift, N)])


def fix(x, shift, N):
    p = x - shift
    if p < 0:
        return p + N
    elif p > N:
        return p - N
    return p


if __name__ == '__main__':
    main()
