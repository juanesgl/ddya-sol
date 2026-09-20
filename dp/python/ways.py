from sys import stdin as sd

coins = [50, 25, 10, 5, 1]
memo = {}


def fr(i, goal, memo, coins):

    if i == len(coins):
        return 0

    if goal == 0:
        return 1

    if goal < 0:
        return 0

    if (i, goal) in memo:
        return memo[(i, goal)]

    res = fr(i, goal - coins[i], memo, coins) + fr(i + 1, goal, memo, coins)

    memo[(i, goal)] = res

    return res


def main(sd):

    for line in sd:
        n = int(line.strip())
        ways = fr(0, n, memo, coins)
        if ways == 1:
            print(f"There is only 1 way to produce {n} cents change.")
        else:
            print(f"There are {ways} ways to produce {n} cents change.")


main(sd)
