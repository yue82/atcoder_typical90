import sys


# 解説見た
# 繰り返し二乗法
def main():
    inputs = [int(s) for s in sys.stdin.read().strip().split(u' ')]
    N, K = inputs

    mod = 10**9 + 7

    if (N == 2 and K == 1) or (N > 2 and K <= 2):
        print(0)
        return

    if N == 1:
        print(K % mod)
        return
    elif N == 2:
        if K < 2:
            print(0)
        else:
            print((K * (K-1)) % mod)
        return

    # K * (K-1) * (K-2)**(N-2)
    a = K-2
    p = N-2
    binp = bin(p)[2:]
    beforepow = 0
    ans = (K * (K-1)) % mod
    for bit, bp in enumerate(binp[::-1]):
        if bit == 0:
            bipow = a % mod
        else:
            bipow = (beforepow * beforepow) % mod
        beforepow = bipow
        if bp == '1':
            ans *= bipow
            ans %= mod
    print(ans)

if __name__ == '__main__':
    main()
