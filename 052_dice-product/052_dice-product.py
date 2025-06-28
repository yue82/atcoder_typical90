import sys


def main():
    inputs = [list(map(int, line.split(u' ')))
              if u' ' in line.strip() else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]

    N = inputs[0]
    A = inputs[1:] if N > 1 else [inputs[1]]

    mod = 10**9 + 7

    sumai = 1
    for i, ai in enumerate(A):
        sumai = sum([mulmod(aij, sumai, mod) for aij in ai])
        sumai = sumai % mod
    print(sumai)

def mulmod(a, b, mod):
    if a >= mod:
        a -= mod
    if b >= mod:
        b -= mod
    a *= b
    if a >= mod:
        a -= mod
    return a

if __name__ == '__main__':
    main()
