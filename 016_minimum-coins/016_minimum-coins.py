import sys

# 解説の想定解法を見た
# 3重ループを2重に緩和する
def main():
    inputs = [list(map(int, line.split(u' ')))
              if u' ' in line.strip() else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]
    N = inputs[0]
    A, B, C = inputs[1]

    # 合計 9999 枚以下の硬貨でちょうど N 円を支払うことができる
    cmin = 10000
    for x in range(10000):
        ax = A*x
        if ax > N:
            break
        for y in range(10000):
            axby = ax + B*y
            if axby > N:
                break
            # xA+yB+zC=N ---> z = (N-xA+yB)/C
            if (N - axby) % C == 0:
                c = x + y + ((N - axby) // C)
                if c < cmin:
                    cmin = c
    print(cmin)

if __name__ == '__main__':
    main()
