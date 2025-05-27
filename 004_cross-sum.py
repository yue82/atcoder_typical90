import sys

def main():

    inputs = [list(map(int, line.split(u' '))) if u' ' in line.strip()
              else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]
    H, W = inputs[0]
    A = inputs[1:]

    rowsum = [0 for h in range(H)]
    colsum = [0 for w in range(W)]
    for h in range(H):
        rowsum[h] = sum(A[h])
    for w in range(W):
        for h in range(H):
            colsum[w] += A[h][w]

    for h in range(H):
        print(' '.join([str(rowsum[h]+colsum[w]-A[h][w]) for w in range(W)]))


if __name__ == '__main__':
    main()
