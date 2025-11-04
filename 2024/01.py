def get_potions(foe):
    return (ord(foe) - 65) * 2 - 1 if ord(foe) in range(66, 69) else 0


def get_extra_potions(foe):
    l = len(foe)
    x = foe.count('x')
    result = l * (l - 1) - x * (x + l)
    return result if result > 0 else 0


def solve_part_one(creatures):

    print(sum([get_potions(x) for x in creatures]))


def solve_part_two(creatures):

    potions = 0
    while creatures:
        pair = creatures[:2]
        potions += sum([get_potions(x) for x in pair]) + get_extra_potions(pair)
        creatures = creatures[2:]

    print(potions)


def solve_part_three(creatures):

    potions = 0
    while creatures:
        triple = creatures[:3]
        potions += sum([get_potions(x) for x in triple]) + get_extra_potions(triple)
        creatures = creatures[3:]

    print(potions)


if __name__ == '__main__':

    data = []
    for i in range(1, 4):
        with open('01_p%d.txt' % i) as file:
            data.append(file.read())

    solve_part_one(data[0])
    solve_part_two(data[1])
    solve_part_three(data[2])
