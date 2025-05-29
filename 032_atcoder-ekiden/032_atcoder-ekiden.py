import sys
import itertools
sys.setrecursionlimit(1000000)


# 頭動かない日だったので最初から解説を見た
def main():
    inputs = [list(map(int, line.split(u' ')))
              if u' ' in line.strip() else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]
    N = inputs[0]
    A = inputs[1:N+1] if N > 1 else [[inputs[1]]]
    M = inputs[N+1]
    if M == 0:
        XY = []
    elif M == 1:
        XY = [inputs[N+2]]
    else:
        XY = inputs[N+2:]

    xydic = {}
    for x, y in XY:
        if x in xydic:
            xydic[x].add(y)
        else:
            xydic[x] = {y}
        if y in xydic:
            xydic[y].add(x)
        else:
            xydic[y] = {x}

    mintime = 1000*N + 1
    for nlist in itertools.permutations(list(range(1, N+1)), N):
        time = 0
        prevn = -1
        for i, n in enumerate(nlist):
            if prevn in xydic and n in xydic[prevn]:
                time = 1000*N + 1
                break
            time += A[n-1][i]
            prevn = n
        if time < mintime:
            mintime = time

    if mintime == 1000*N + 1:
        print(-1)
    else:
        print(mintime)


if __name__ == '__main__':
    main()
