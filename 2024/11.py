def solve_part_one(rules, days=4, start='A'):

    pop = start

    for i in range(days):
        new_gen = ''
        for p in pop:
            new_gen += ''.join(rules[p])
        pop = new_gen

    print(len(pop))


def solve_part_two(rules, days=10, start='Z'):

    solve_part_one(rules, days, start)


def solve_part_three(rules):

    def find_pop(term, day):
        if day == 1:
            return len(rules[term])
        elif pops[term][day-1] != 0:
            return pops[term][day-1]
        else:
            size = 0
            for n_term in rules[term]:
                size += find_pop(n_term, day - 1)
            pops[term][day-1] += size
            return size

    days = 20
    pops = {x: days * [0] for x in rules.keys()}

    for kind in rules.keys():
        pops[kind][days-1] = find_pop(kind, days)

    last_day_pops = [pops[x][days-1] for x in rules.keys()]
    print(max(last_day_pops) - min(last_day_pops))


if __name__ == '__main__':

    data = []
    for i in range(1, 4):
        with open('11_p%d.txt' % i) as file:
            data.append({x.split(':')[0]: x.split(':')[1].split(',')
                         for x in file.read().splitlines()})

    solve_part_one(data[0])
    solve_part_two(data[1])
    solve_part_three(data[2])
