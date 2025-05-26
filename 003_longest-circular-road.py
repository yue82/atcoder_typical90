import sys
sys.setrecursionlimit(1000000)  # 再起関数の呼び出し回数の上限が1000 のままだと RE になる

# 基本方針から解説を見た
# 木の中の最長パス=直径 を見つけ、1を足す
# 直径は最遠点を2回やると求められるらしい
def main():

    inputs = [list(map(int, line.split(u' '))) if u' ' in line.strip()
              else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]
    N = inputs[0]
    AB = inputs[1:]
    ABdic = [set() for i in range(N+1)]
    for ab in AB:
        ABdic[ab[0]].add(ab[1])
        ABdic[ab[1]].add(ab[0])

    # 適当な点 からの最遠点
    for i in range(1, N+1):
        if ABdic[i] != set():
            _, fp1 = far(i, -1, ABdic)
            break
    # fp1 からの最遠点
    d, fp2 = far(fp1, -1, ABdic)
    print(d+1)


def far(here, frm, ABdic):
    if ABdic[here] == set() or ABdic[here] == {frm}:
        return 0, here

    dmax = 0
    mfp = here
    for nhere in ABdic[here]:
        if nhere == frm:
            continue
        d, fp = far(nhere, here, ABdic)
        if d >= dmax:
            dmax = d + 1
            mfp = fp

    return dmax, mfp


if __name__ == '__main__':
    main()
