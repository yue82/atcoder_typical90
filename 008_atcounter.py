import sys

# 基本方針から解説を見た
# ナップザック問題的な状態DP
# 今見ている文字が atcoder の何文字目まで進んだ状態か
def main():

    inputs = [line.split(u' ') if u' ' in line.strip()
              else line.strip()
              for line in sys.stdin.read().strip().split('\n')]
    N = int(inputs[0])
    S = inputs[1]

    key = 'atcoder'

    dp = [[0]*(len(key)+1) for s in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j, k in enumerate(key+' '):
            dp[i+1][j] = addmod(dp[i+1][j], dp[i][j], 1_000_000_007)
            if S[i] == k:
                dp[i+1][j+1] = addmod(dp[i+1][j+1], dp[i][j], 1_000_000_007)
    print(dp[N][len(key)])

def addmod(a, b, mod):
    a += b
    if a >= mod:
        a -= mod
    return a

if __name__ == '__main__':
    main()
