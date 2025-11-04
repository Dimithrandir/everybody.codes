def get_neighbors(matrix, i, j, diagonal=False):

    return [(i + x, j + y)
            for x in range(-1, 2)
            for y in range(-1, 2)
            if (i + x in range(len(matrix))
                and j + y in range(len(matrix[0]))
                and ((x + y) % 2 != 0) if not diagonal else True)]


def solve_part_one(gridmap, diagonal=False):

    digs = [(x, y)
            for x in range(len(gridmap))
            for y in range(len(gridmap[0]))
            if gridmap[x][y] == '#']
    blocks = len(digs)

    while digs:
        next_level = []
        for dig in digs:
            if all([x in digs for x in get_neighbors(gridmap, dig[0], dig[1], diagonal)]):
                blocks += 1
                next_level.append(dig)
        digs = next_level

    print(blocks)


def solve_part_two(gridmap, diagonal=False):

    solve_part_one(gridmap)


def solve_part_three(gridmap, diagonal=True):

    solve_part_one(gridmap, diagonal)


if __name__ == '__main__':

    data = []
    for i in range(1, 4):
        with open('03_p%d.txt' % i) as file:
            data.append(file.read().splitlines())

    solve_part_one(data[0])
    solve_part_two(data[1])
    solve_part_three(data[2])
