import sys


# 解説見た
def main():
    inputs = [list(map(int, line.split(u' ')))
              if u' ' in line.strip() else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]
    N = inputs[0]
    A = inputs[1] if isinstance(inputs[1], list) else [inputs[1]]
    B = inputs[2] if isinstance(inputs[2], list) else [inputs[2]]
    C = inputs[3] if isinstance(inputs[3], list) else [inputs[3]]

    modcA = [0 for i in range(46)]
    modcB = [0 for i in range(46)]
    modcC = [0 for i in range(46)]
    for n in range(N):
        modcA[A[n]%46] += 1
        modcB[B[n]%46] += 1
        modcC[C[n]%46] += 1

    c = 0
    for i, ai in enumerate(modcA):
        if ai == 0:
            continue
        for j, bj in enumerate(modcB):
            if bj == 0:
                continue
            for k, ck in enumerate(modcC):
                if ck == 0:
                    continue
                ijk = i + j + k
                if ijk % 46 == 0:
                    c += ai * bj * ck
    print(c)


if __name__ == '__main__':
    main()
