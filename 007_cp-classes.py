import sys

def main():

    inputs = [list(map(int, line.split(u' '))) if u' ' in line.strip()
              else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]
    N = inputs[0]
    A = inputs[1] if isinstance(inputs[1], list) else [inputs[1]]
    Q = inputs[2]
    B = inputs[3:]

    A.sort()

    for b in B:
        left = 0
        right = N-1
        while True:
            mid = (left + right) // 2
            if mid == left:
                break
            if A[mid] < b:
                left = mid
            else:
                right = mid
        print(min(abs(b-A[left]), abs(b-A[right])))


if __name__ == '__main__':
    main()
