import sys

# 基本方針から解説を見た
def main():

    S = int(sys.stdin.read().strip())

    if S % 2 == 1:
        return

    f = '{:0'+str(S)+'b}'
    for i in range(1, 2**(S-1), 2):
        s = f.format(i)
        c = 0
        for ss in s:
            if ss == '0':
                c += 1
            elif ss == '1':
                c -= 1
            if c < 0:
                break
        if c == 0:
            print(s.translate(str.maketrans({'0': '(', '1': ')'})))

if __name__ == '__main__':
    main()
