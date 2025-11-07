from math import ceil, sqrt


def get_thickness(n, n_p, n_a, p_3=False):
    if n == 1:
        return n
    else:
        return ((get_thickness(n - 1, n_p, n_a, p_3) * n_p) % n_a) + (n_a if p_3 else 0)


def find_thickness_cycle(n_p, n_a, p_3=False):
    t_i = []
    s = 1 if p_3 else 0
    i = 1
    while True:
        t_i.append(get_thickness(i, n_p, n_a, p_3))
        m = len(t_i) // 2 + s
        if t_i[s:m] and t_i[s:m] == t_i[m:]:
            t_i = t_i[s:m]
            break
        i += 1
    return t_i


def solve_part_one(n_b):

    w = ceil(2 * sqrt(n_b) - 1)
    n_a = (w**2 + 2 * w + 1) // 4 - n_b

    print(w * n_a)


def solve_part_two(n_p):

    # acolytes
    n_a = 1111
    # block supply
    n_b = 20240000

    t_i = find_thickness_cycle(n_p, n_a)

    # layer
    l = 1
    # total blocks
    n_t = 0
    while True:
        # width
        w = 2 * l - 1
        # blocks for current layer
        n_l = w * t_i[(l-1) % len(t_i)]
        # total blocks
        n_t += n_l

        if (n_t > n_b):
            # extra blocks
            n_e = n_t - n_b
            print(w * n_e)
            break

        l += 1


def solve_part_three(n_p):

    # acolytes
    n_a = 10
    # block supply
    n_b = 202400000

    t_i = find_thickness_cycle(n_p, n_a, True)

    n_t = 1
    heights = [1]
    l = 2
    while True:
        # width
        w = 2 * l - 1
        # thickness for current layer
        n_l = t_i[(l-2) % len(t_i)]
        # total blocks
        n_t += w * n_l
        # neights
        heights.insert(0, 0)
        heights.append(0)
        for i in range(len(heights)):
            heights[i] += n_l

        # removed blocks
        n_r = 0
        for h in heights[1:-1]:
            n_r += ((n_p * len(heights)) * h % n_a)

        # additional blocks
        if (n_t - n_r > n_b):
            n_e = n_t - n_r - n_b
            print(n_e)
            break

        l += 1


if __name__ == '__main__':

    data = []
    for i in range(1, 4):
        with open('08_p%d.txt' % i) as file:
            data.append(int(file.read()))

    solve_part_one(data[0])
    solve_part_two(data[1])
    solve_part_three(data[2])
