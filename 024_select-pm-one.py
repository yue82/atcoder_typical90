import sys


def main():
    inputs = [list(map(int, line.split(u' ')))
              if u' ' in line.strip() else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]
    N, K = inputs[0]
    A = inputs[1] if isinstance(inputs[1], list) else [inputs[1]]
    B = inputs[2] if isinstance(inputs[2], list) else [inputs[2]]

    diffs = 0
    for a, b in zip(A, B):
        diffs += abs(a-b)

    if diffs <= K and (K - diffs) % 2 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
