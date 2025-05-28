import sys
import itertools


def main():
    inputs = [list(map(int, line.split(u' ')))
              if u' ' in line.strip() else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]
    N, P, Q = inputs[0]
    A = inputs[1]
    mods = [a % P for a in A]

    c = 0
    for v in itertools.combinations(A, 5):
        if (v[0]%P * v[1]%P * v[2]%P * v[3]%P * v[4]%P) %P == Q:
            c += 1
    print(c)

if __name__ == '__main__':
    main()
