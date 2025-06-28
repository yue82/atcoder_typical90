import sys


def main():
    inputs = [int(s) for s in sys.stdin.read().strip().split(u' ')]
    L, R = inputs

    mod = 10**9 + 7

    digL = len(str(L))
    digR = len(str(R))

    if digL == digR:
        Lm1sum = (L-1)*L//2
        Rsum = R*(R+1)//2
        print(((Rsum-Lm1sum) * digL) % mod)
        return

    Lm1sum = (L-1)*L//2
    digLmax = 10**digL - 1
    digLmaxsum = digLmax*(digLmax+1)//2
    digLsum = ((digLmaxsum-Lm1sum) * digL) % mod

    digRminm1 = 10**(digR-1) - 1
    digRminsum = digRminm1*(digRminm1+1)//2
    Rsum = R*(R+1)//2
    digRsum = ((Rsum-digRminsum) * digR) % mod

    digsums = 0
    if abs(digL-digR) > 1:
        for dig in range(digL+1, digR):
            digminm1 = 10**(dig-1) - 1
            digminsum = digminm1*(digminm1+1)//2

            digmax = 10**dig - 1
            digmaxsum = digmax*(digmax+1)//2
            digsums += ((digmaxsum - digminsum) * dig) % mod

    print((digLsum + digRsum + digsums) % mod)


if __name__ == '__main__':
    main()
