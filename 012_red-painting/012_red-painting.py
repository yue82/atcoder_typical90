import sys

sqmap = []
roots = {}

# 途中で方針を調べた
# Union find tree
def main():
    inputs = [list(map(int, line.split(u' ')))
              if u' ' in line.strip() else int(line.strip())
              for line in sys.stdin.read().strip().split('\n')]
    H, W = inputs[0]
    Q = inputs[1]
    Qs = inputs[2:]

    global sqmap
    sqmap = [[False] * W for h in range(H)]

    for q in Qs:
        if q[0] == 1:
            t, r, c = q
            r, c = r-1, c-1
            sqmap[r][c] = True
            add_tree(r, c, H, W)
        else:
            t, ra, ca, rb, cb = q
            ra, ca, rb, cb = ra-1, ca-1, rb-1, cb-1
            if sqmap[ra][ca] and sqmap[rb][cb] and get_root(ra, ca) == get_root(rb, cb):
                print('Yes')
            else:
                print('No')

def add_tree(r, c, H, W):
    global sqmap
    global roots
    nes = []
    if r-1 >= 0 and sqmap[r-1][c]:
        nes.append((r-1, c))
    if r+1 < H and sqmap[r+1][c]:
        nes.append((r+1, c))
    if c-1 >= 0 and sqmap[r][c-1]:
        nes.append((r, c-1))
    if c+1 < W and sqmap[r][c+1]:
        nes.append((r, c+1))

    if len(nes) == 0:           # 孤立点
        roots[(r, c)] = (r, c)
    else:
        groot = get_root(*nes[0])
        roots[(r, c)] = groot
        if len(nes) > 1:
            for ne in nes[1:]:
                roots[get_root(*ne)] = groot


def get_root(r, c):
    global roots
    root = roots[(r, c)]
    if root == (r, c):
        return (r, c)
    return get_root(*root)


if __name__ == '__main__':
    main()
