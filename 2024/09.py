def solve_part_one(sparkballs, stamps=[1, 3, 5, 10]):

    sparkballs.sort()
    m = [[10**10 if x == 0 else 0 for y in range(sparkballs[-1] + 1)]
         for x in range(len(stamps) + 1)]

    for i in range(1, len(stamps) + 1):
        for j in range(1, sparkballs[-1] + 1):
            if stamps[i-1] == j:
                m[i][j] = 1
            elif stamps[i-1] > j:
                m[i][j] = m[i-1][j]
            else:
                m[i][j] = min(m[i-1][j], m[i][j-stamps[i-1]] + 1)

    print(sum([m[-1][x] for x in sparkballs]))


def solve_part_two(sparkballs):

    solve_part_one(sparkballs, [1, 3, 5, 10, 15, 16, 20, 24, 25, 30])


def solve_part_three(sparkballs):

    stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]

    maxball = max(sparkballs)

    m = [[10**10 if x == 0 else 0 for y in range(maxball + 101)]
         for x in range(len(stamps) + 1)]

    for i in range(1, len(stamps) + 1):
        for j in range(1, maxball + 101):
            if stamps[i-1] == j:
                m[i][j] = 1
            elif stamps[i-1] > j:
                m[i][j] = m[i-1][j]
            else:
                m[i][j] = min(m[i-1][j], m[i][j-stamps[i-1]] + 1)

    mins = []

    for ball in sparkballs:

        b1 = ball // 2
        b2 = (ball // 2) + (1 if ball % 2 else 0)
        b_mins = 2 * [10**10]

        while b2 - b1 <= 100:

            b_mins[0] = min(b_mins[0], m[-1][b1])
            b_mins[1] = min(b_mins[1], m[-1][b2])

            b2 += 1
            b1 -= 1

        mins.extend(b_mins)

    print(sum(mins))


if __name__ == '__main__':

    data = []
    for i in range(1, 4):
        with open('09_p%d.txt' % i) as file:
            data.append([int(x) for x in file.read().splitlines()])

    solve_part_one(data[0])
    solve_part_two(data[1])
    solve_part_three(data[2])
