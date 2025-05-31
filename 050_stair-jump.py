import sys
import math


# TLE して解説見た
def main():
    inputs = map(int, sys.stdin.read().strip().split(u' '))
    N, L = inputs

    modnum = 10**9 + 7

    ## TLE
    # P = N // L
    # c = 0
    # for numl in range(P+1):
    #     num1 = N - numl * L
    #     allnum = numl + num1
    #     a = math.factorial(allnum)//(math.factorial(num1)*math.factorial(numl))
    #     c += a % modnum
    # print(c % modnum)

    dp = [0 for n in range(N+1)]
    dp[0] = 1
    for n in range(1, N+1):
        if n < L:
            dp[n] = dp[n-1]
        else:
            dp[n] = (dp[n-1] + dp[n-L]) % modnum
    print(dp[N])


if __name__ == '__main__':
    main()
