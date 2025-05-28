import sys


def main():
    inputs = [line.split(u' ') if u' ' in line.strip()
              else line.strip()
              for line in sys.stdin.read().strip().split('\n')]
    N = inputs[0]
    S = inputs[1:]

    users = set()
    for i, s in enumerate(S):
        if s not in users:
            users.add(s)
            print(i+1)

if __name__ == '__main__':
    main()
