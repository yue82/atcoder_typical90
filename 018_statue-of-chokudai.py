import sys
import math


def main():
    inputs = [list(map(int, line.split(u' ')))
              if u' ' in line.strip() else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]

    T = inputs[0]
    L, X, Y = inputs[1]
    Q = inputs[2]
    E = inputs[3:]

    for e in E:
        high = get_z(e, L, T)
        y = get_y(e, L, T)
        dist = math.sqrt(X**2 + (y - Y)**2)
        print(math.degrees(math.atan2(high, dist)))

def get_y(t, L, T):
    deg = t / T * 360   # 真下から
    return -math.sin(math.radians(deg)) * L/2

def get_z(t, L, T):
    deg = t / T * 360   # 真下から
    return (math.sin(math.radians(deg - 90)) + 1) * L/2


if __name__ == '__main__':
    main()
