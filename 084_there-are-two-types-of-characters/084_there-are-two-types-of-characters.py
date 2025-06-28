import sys


def main():
    inputs = [line.split(u' ') if u' ' in line.strip()
              else line.strip()
              for line in sys.stdin.read().strip().split('\n')]
    N = int(inputs[0])
    S = inputs[1]

    allrange = N * (N-1) // 2

    l = 0
    r = 1
    nowsim = S[l]
    sim1range = 0
    while r < N:
        c = 1
        while r < N and S[l] == S[r]:
            c += 1
            r += 1
        sim1range += c * (c-1) // 2
        l = r
        r = l + 1

    print(allrange - sim1range)


if __name__ == '__main__':
    main()
