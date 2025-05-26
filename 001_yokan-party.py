import sys
import math

# 基本方針から解説を見た
# スコアいくつなら達成可能か二分探索する
# 最小値を最大化する問題では二分探索が有効なことが多いそう
def main():

    inputs = [list(map(int, line.split(u' '))) if u' ' in line.strip()
              else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]

    N, L = inputs[0]
    K = inputs[1]
    A = inputs[2]

    mi, ma = -1, L+1
    while ma - mi > 1:
        m = (mi + ma) // 2
        if cancut(m, L, K, A):
            mi = m
        else:
            ma = m
    print(mi)

def cancut(target, L, K, A):
    l = L
    k = K
    c = 0
    pa = 0
    for a in A:
        c += a - pa               # a は左端からのサイズ
        pa = a
        if target <= c:            # 目標より大きく切れる
            if l - c <= 0:        # 切ったらなくなる
                return False
            k -= 1                # 切る
            l = l - c
            c = 0                 # 切ったらリセット
        if k == 0:                # 切り終わり
            return target <= l    # 最後のピースチェック
    return False

if __name__ == '__main__':
    main()
