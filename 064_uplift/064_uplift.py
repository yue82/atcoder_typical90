import sys


def main():
    inputs = [list(map(int, line.split(u' ')))
              if u' ' in line.strip() else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]

    N, Q = inputs[0]
    A = inputs[1]
    LRV = inputs[2:] if Q > 1 else [inputs[2]]

    edsum = 0
    ed = [0]*(N-1)
    for n in range(N-1):
        ed[n] = A[n+1] - A[n]
    edsum = sum([abs(edd) for edd in ed])

    for L, R, V in LRV:
        L, R = L-1, R-1
        if L > 0:
            edsum -= abs(ed[L-1])
            ed[L-1] += V
            edsum += abs(ed[L-1])
        if R < N-1:
            edsum -= abs(ed[R])
            ed[R] -= V
            edsum += abs(ed[R])
        print(edsum)

if __name__ == '__main__':
    main()
