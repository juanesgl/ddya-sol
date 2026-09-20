from sys import stdin as sd

memo = {}


def fr(i, goal, memo, coins, suffix_sum):

    if i == len(coins):
        return 0

    goal = min(goal, suffix_sum[i])

    if goal == suffix_sum[i]:
        return goal

    if goal == 0:
        return 0

    if (i, goal) in memo:
        return memo[(i, goal)]

    optionA = 0
    if coins[i] <= goal:
        optionA = coins[i] + fr(i + 1, goal - coins[i], memo, coins, suffix_sum)

    optionB = fr(i + 1, goal, memo, coins, suffix_sum)
    final_fr = max(optionA, optionB)

    memo[(i, goal)] = final_fr

    return final_fr


def main(sd):
    tc = int(sd.readline().strip())

    for _ in range(tc):
        m = int(sd.readline().strip())

        if m == 0:
            sd.readline()
            print(0)
            continue

        coins = []

        while len(coins) < m:
            line = sd.readline().split()
            coins.extend(map(int, line))

        coins.sort(reverse=True)

        suffix_sum = [0] * m
        suffix_sum[-1] = coins[-1]

        for k in range(m - 2, -1, -1):
            suffix_sum[k] = suffix_sum[k + 1] + coins[k]

        memo = {}

        objective = sum(coins)

        G = fr(0, objective // 2, memo, coins, suffix_sum)

        print(objective - 2 * G)


main(sd)
