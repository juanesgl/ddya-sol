from sys import stdin as sd


def check_parity(p: list[int]):

    w = sum(p)
    if w % 2 == 1:
        return False
    return fr(0, w // 2, {}, p)


def fr(i: int, w: int, memo: dict[int, int], p: list[int]):

    if w == 0:
        return True
    if w < 0:
        return False
    if i == len(p):
        return False

    if (i, w) in memo:
        return memo[(i, w)]

    res = fr(i + 1, w - p[i], memo, p) or fr(i + 1, w, memo, p)
    memo[(i, w)] = res
    return res


def main(sd):

    tc = int(sd.readline().strip())
    for _ in range(tc):
        line = sd.readline().split()

        p = list(map(int, line))

        if check_parity(p):
            print("YES")
        else:
            print("NO")


main(sd)
