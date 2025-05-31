import sys


# 解説を見た
def main():
    inputs = [list(map(int, line.split(u' ')))
              if u' ' in line.strip() else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]

    N, K = inputs[0]
    AB = inputs[1:] if isinstance(inputs[1], list) else [inputs[1:]]
    points = []
    for a, b in AB:
        points.append(b)
        points.append(a-b)
    print(sum(sorted(points)[-K:]))


if __name__ == '__main__':
    main()
