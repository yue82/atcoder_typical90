import sys
sys.setrecursionlimit(1000000)


# N/2頂点を取り出す がわからず解説を見た
# N/2個の点を、隣り合わないよう出す
# 木は必ず二部グラフ(交互塗り分け可能)(閉路での塗り矛盾が起きない)
# 二色の数を揃えられるかはわからないので、多い方からN/2個出す

childs = {}
red = []
green = []

def main():
    inputs = [list(map(int, line.split(u' ')))
              if u' ' in line.strip() else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]
    N = inputs[0]
    AB = inputs[1:]

    global childs
    for a, b in AB:
        if a not in childs:
            childs[a] = {b}
        else:
            childs[a].add(b)
        if b not in childs:
            childs[b] = {a}
        else:
            childs[b].add(a)

    # print(childs)
    dfs(AB[0][0], 'red', -1)

    global red
    global green
    # print(red, green)
    if len(red) >= len(green):
        print(' '.join(map(str, red[:N//2])))
    else:
        print(' '.join(map(str, green[:N//2])))


def dfs(me, color, parent):
    global childs
    global red
    global green
    # print(me, color)
    if color == 'red':
        red.append(me)
        childcolor = 'green'
    else:
        green.append(me)
        childcolor = 'red'
    if me not in childs or childs[me] is None:
        return
    for child in childs[me]:
        if child == parent:
            continue
        dfs(child, childcolor, me)

if __name__ == '__main__':
    main()
