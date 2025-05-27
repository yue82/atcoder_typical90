import sys


def main():
    inputs = [list(map(int, line.split(u' ')))
              if u' ' in line.strip() else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]
    N = inputs[0]
    A = inputs[1] if isinstance(inputs[1], list) else [inputs[1]]
    B = inputs[2] if isinstance(inputs[2], list) else [inputs[2]]

    s = 0
    for a, b in zip(sorted(A), sorted(B)):
        s += abs(a-b)
    print(s)

if __name__ == '__main__':
    main()
