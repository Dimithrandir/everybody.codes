def dance_round(rnd, columns):

    cur_i = rnd % len(columns)
    next_i = (rnd + 1) % len(columns)
    clapper = columns[cur_i].pop(0)
    a = len(columns[next_i]) / 2
    p = len(columns[next_i]) * 2
    insert_i = int(4 * a / p * abs(((((clapper - 1 - a - p / 4) % p) + p) % p) - p / 2))
    columns[next_i].insert(insert_i, clapper)


def get_number(columns):
    return ''.join([str(x[0]) for x in columns])


def solve_part_one(columns, rounds):

    for i in range(rounds):
        dance_round(i, columns)

    print(get_number(columns))


def solve_part_two(columns):

    nmbs = {}
    rnd = 0

    while True:
        dance_round(rnd, columns)

        new_num = get_number(columns)
        nmbs[new_num] = 1 if new_num not in nmbs.keys() else nmbs[new_num] + 1

        rnd += 1

        if nmbs[new_num] == 2024:
            print(rnd * int(new_num))
            return


def solve_part_three(columns):

    rnd = 0
    max_num = 0
    col_states = set()

    while True:
        dance_round(rnd, columns)

        max_num = max(max_num, int(get_number(columns)))

        cur_state = ''.join([''.join([str(y) for y in x]) for x in columns])

        if cur_state in col_states:
            print(max_num)
            return

        col_states.add(cur_state)
        rnd += 1


if __name__ == '__main__':

    data = []
    for i in range(1, 4):
        with open('05_p%d.txt' % i) as file:
            rows = [[int(y) for y in x.split()] for x in file.read().splitlines()]
            columns = [[rows[y][x] for y in range(len(rows))] for x in range(len(rows[0]))]
            data.append(columns)

    solve_part_one(data[0], 10)
    solve_part_two(data[1])
    solve_part_three(data[2])
