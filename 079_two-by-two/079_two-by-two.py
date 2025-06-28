import sys


# 解説見た
def main():
    inputs = [list(map(int, line.split(u' ')))
              if u' ' in line.strip() else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]

    H, W = inputs[0]
    A = inputs[1:H+1]
    B = inputs[H+1:]

    c = 0
    for h in range(H-1):
        for w in range(W-1):
            if A[h][w] != B[h][w]:
                d = B[h][w] - A[h][w]
                A[h][w] += d
                A[h+1][w] += d
                A[h][w+1] += d
                A[h+1][w+1] += d
                c += abs(d)
        if A[h][W-1] != B[h][W-1]:
            print('No')
            return
    if A[H-1] != B[H-1]:
        print('No')
        return
    print('Yes')
    print(c)

if __name__ == '__main__':
    main()
