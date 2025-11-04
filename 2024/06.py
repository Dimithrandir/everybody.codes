def solve_part_one(nails):

    lowest = min(nails)
    print(sum([x - lowest for x in nails]))


def solve_part_two(nails):

    solve_part_one(nails)


def solve_part_three(nails):

    min_strikes = nails[0] * 10
    for nail in nails:
        min_strikes = min(min_strikes, sum([abs(x - nail) for x in nails]))

    print(min_strikes)


if __name__ == '__main__':

    data = []
    for i in range(1, 4):
        with open('04_p%d.txt' % i) as file:
            data.append([int(x) for x in file.read().splitlines()])

    solve_part_one(data[0])
    solve_part_two(data[1])
    solve_part_three(data[2])
