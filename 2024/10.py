n = 8
d = 2


def calculate_power(word):
    return sum([(i + 1) * (ord(x) - ord('A') + 1) for i, x in enumerate(word)])


def solve_part_one(grid):

    word = ''

    for i in range(d, n - d):
        row = set([x for x in grid[i] if x != '.'])
        for j in range(d, n - d):
            column = set([grid[x][j] for x in range(n) if grid[x][j] != '.'])
            word += list(row.intersection(column))[0]

    print(word)


def solve_part_two(grids):

    power = 0

    for i in range(d, len(grids), n + 1):
        for j in range(d, len(grids[i]), n + 1):
            word = ''
            for k in range(i, i + 2 * d):
                row = set([x for x in grids[k].split(' ')[j // (n + 1)] if x != '.'])
                for l in range(j, j + 2 * d):
                    column = set([grids[x][l] for x in range(i - d, i + n - d) if grids[x][l] != '.'])
                    word += list(row.intersection(column))[0]
            power += calculate_power(word)

    print(power)


def solve_part_three(grids):

    # number of solvable blocks
    solvable = 0

    while True:

        power = 0
        new_solvable = 0

        for i in range(d, len(grids), n - 2):
            for j in range(d, len(grids[i]), n - 2):
                word = ''
                possible_symbols = []
                for k in range(i, i + 2 * d):
                    row = [(k, x) for x in range(j - d, j + n - d) if x not in range(j, j + 2 * d)]
                    for l in range(j, j + 2 * d):
                        column = [(x, l) for x in range(i - d, i + n - d) if x not in range(i, i + 2 * d)]
                        intersect = set([grids[x[0]][x[1]] for x in row]).intersection(set([grids[x[0]][x[1]] for x in column]))
                        if len(intersect) == 1 and '?' not in intersect:
                            word += list(intersect)[0]
                        else:
                            word += '.'
                            possible_symbols.append(row + column)

                # try deducing the question marks
                for sym in word:
                    if sym == '.':
                        possible = possible_symbols.pop(0)
                        diff = set([grids[x[0]][x[1]] for x in possible]).difference(set(word))
                        if '?' not in diff:
                            continue
                        diff.remove('?')
                        if len(diff) == 1:
                            missing_sym = list(diff)[0]
                            word = word.replace('.', missing_sym, 1)
                            for p in possible:
                                if grids[p[0]][p[1]] == '?':
                                    q_row = list(grids[p[0]])
                                    q_row[p[1]] = missing_sym
                                    grids[p[0]] = ''.join(q_row)

                if '.' not in word:
                    power += calculate_power(word)
                    new_solvable += 1

        # if no blocks have been solved in the last run, end it
        if solvable == new_solvable:
            print(power)
            break
        else:
            solvable = new_solvable


if __name__ == '__main__':

    data = []
    for i in range(1, 4):
        with open('10_p%d.txt' % i) as file:
            data.append([x for x in file.read().splitlines()])

    solve_part_one(data[0])
    solve_part_two(data[1])
    solve_part_three(data[2])
