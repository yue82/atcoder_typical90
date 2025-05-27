import sys

def main():
    inputs = list(map(int, sys.stdin.read().strip().split(' ')))
    A = inputs[0]
    B = inputs[1]
    C = inputs[2]

    if A < C**B:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
