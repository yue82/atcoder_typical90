import sys


# 公式解説を見た
# 領域加減=2次元いもす法
# 後で横に塗り拡げられるようマーカー的に置く感じ？
def main():
    inputs = [list(map(int, line.split(u' ')))
              if u' ' in line.strip() else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]
    N = inputs[0]
    P = inputs[1:]

    msize = 1000

    m = [[0] * (msize+2) for i in range(msize+2)]

    for lx, ly, rx, ry in P:
        lx, ly, rx, ry = lx+1, ly+1, rx+1, ry+1 # 0行0列を空けたい
        m[lx][ly] += 1
        m[lx][ry] -= 1
        m[rx][ly] -= 1
        m[rx][ry] += 1

    for x in range(1, msize+1):
        for y in range(1, msize+1):
            m[x][y] += m[x][y-1]
    for y in range(1, msize+1):
        for x in range(1, msize+1):
            m[x][y] += m[x-1][y]

    r = [0] * (N+1)
    for x in range(1, msize+1):
        for y in range(1, msize+1):
            r[m[x][y]] += 1
    for rr in r[1:]:
        print(rr)

if __name__ == '__main__':
    main()
