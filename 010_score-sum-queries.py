import sys

def main():
    inputs = [list(map(int, line.split(u' ')))
              if u' ' in line.strip() else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]
    N = inputs[0]
    CP = inputs[1:N+1]
    Q = inputs[N+1]
    LR = inputs[N+2:]

    sums1 = [0 for n in range(N+1)]
    sums2 = [0 for n in range(N+1)]

    sum1 = 0
    sum2 = 0
    for n in range(1, N+1):
        if CP[n-1][0] == 1:
            sum1 += CP[n-1][1]
            sums1[n] = sum1
            if n > 0:
                sums2[n] = sums2[n-1]
        else:
            sum2 += CP[n-1][1]
            sums2[n] = sum2
            if n > 0:
                sums1[n] = sums1[n-1]
    for l, r in LR:
        print('{} {}'.format(sums1[r]-sums1[l-1], sums2[r]-sums2[l-1]))

if __name__ == '__main__':
    main()
