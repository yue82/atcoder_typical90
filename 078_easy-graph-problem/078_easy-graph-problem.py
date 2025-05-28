import sys


def main():
    inputs = [list(map(int, line.split(u' ')))
              if u' ' in line.strip() else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]
    N, M = inputs[0]
    AB = inputs[1:]

    nes = [0 for i in range(N)]
    for a, b in AB:
        s, l = min(a, b)-1, max(a, b)-1
        nes[l] += 1

    c = 0
    for l in range(N):
        if nes[l] == 1:
            c += 1

    print(c)


if __name__ == '__main__':
    main()
