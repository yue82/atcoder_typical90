import sys
from collections import deque


def main():
    inputs = [list(map(int, line.split(u' ')))
              if u' ' in line.strip() else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]
    Q = inputs[0]
    X = inputs[1:]

    d = deque()

    for t, x in X:
        if t == 1:
            d.appendleft(x)
        elif t == 2:
            d.append(x)
        else:
            print(d[x-1])


if __name__ == '__main__':
    main()
