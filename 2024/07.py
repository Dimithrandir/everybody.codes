def solve_part_one(plans):
    # number of actions per plan
    a_len = len(plans[list(plans.keys())[0]])

    cur_power = {x: 10 for x in plans.keys()}
    essence = {x: 0 for x in plans.keys()}

    for segment in range(10):
        for device in plans.keys():
            action = plans[device][segment % a_len]
            cur_power[device] += (1 if action == '+' else -1 if action == '-' else 0)
            essence[device] += cur_power[device]

    ranking = sorted([(key, val) for (key, val) in essence.items()], key=lambda l: l[1], reverse=True)
    print(''.join([x[0] for x in ranking]))


def solve_part_two(plans):

    track = '''S-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=--
-                                                                     -
=                                                                     =
+                                                                     +
=                                                                     +
+                                                                     =
=                                                                     =
-                                                                     -
--==++++==+=+++-=+=-=+=-+-=+-=+-=+=-=+=--=+++=++=+++==++==--=+=++==+++-'''.splitlines()
    m = len(track)
    track = (''.join(track[0][1:]) +
             ''.join([track[i][len(track[i])-1] for i in range(m)][1:]) +
             ''.join(list(reversed(track[m-1]))[1:]) +
             ''.join([track[i][0] for i in range(m - 1, -1, -1)][1:]))

    # number of actions per plan
    a_len = len(plans[list(plans.keys())[0]])

    cur_power = {x: 10 for x in plans.keys()}
    essence = {x: 0 for x in plans.keys()}

    i = 0
    for loop in range(10):
        for field in track:
            for device in plans.keys():
                action = plans[device][i % a_len] if field in '=S' else field
                cur_power[device] += (1 if action == '+' else -1 if action == '-' else 0)
                essence[device] += cur_power[device]
            i += 1

    ranking = sorted([(key, val) for (key, val) in essence.items()], key=lambda l: l[1], reverse=True)
    print(''.join([x[0] for x in ranking]))


def solve_part_three(plans):

    def get_all_plans(actions):
        if not actions:
            return ['']
        result = set()
        for i in range(len(actions)):
            cur = actions[i]
            rest = actions[:i] + actions[i+1:]
            for p in get_all_plans(rest):
                result.add(cur + p)
        return result

    track = '''S+= +=-== +=++=     =+=+=--=    =-= ++=     +=-  =+=++=-+==+ =++=-=-=--
- + +   + =   =     =      =   == = - -     - =  =         =-=        -
= + + +-- =-= ==-==-= --++ +  == == = +     - =  =    ==++=    =++=-=++
+ + + =     +         =  + + == == ++ =     = =  ==   =   = =++=       
= = + + +== +==     =++ == =+=  =  +  +==-=++ =   =++ --= + =          
+ ==- = + =   = =+= =   =       ++--          +     =   = = =--= ==++==
=     ==- ==+-- = = = ++= +=--      ==+ ==--= +--+=-= ==- ==   =+=    =
-               = = = =   +  +  ==+ = = +   =        ++    =          -
-               = + + =   +  -  = + = = +   =        +     =          -
--==++++==+=+++-= =-= =-+-=  =+-= =-= =--   +=++=+++==     -=+=++==+++-'''.splitlines()

    track_pos = []
    track_vals = ''
    (i, j) = (0, 1)

    while track[i][j] != 'S':

        neighbors = [(x, y)
                     for x in range(max(0, i-1), min(len(track), i+2))
                     for y in range(max(0, j-1), min(len(track[i]), j+2))
                     if (x + y) % 2 == (0 if (i + j) % 2 == 1 else 1)
                     and track[x][y] != ' ' and (x, y) not in track_pos]

        if len(neighbors) > 1:
            for (i, neigh) in enumerate(neighbors):
                if track[neigh[0]][neigh[1]] == 'S':
                    neighbors.pop(i)
                    break

        track_vals += track[i][j]
        track_pos.append((i, j))
        (i, j) = neighbors[0]

    track = track_vals + 'S'

    # find input knight score
    cur_power = 10
    a_score = 0
    i = 0
    for loop in range(2024):
        for field in track:
            action = plans['A'][i % len(plans['A'])] if field in '=S' else field
            cur_power += (1 if action == '+' else -1 if action == '-' else 0)
            a_score += cur_power
            i += 1

    result = 0
    for plan in get_all_plans(5 * '+' + 3 * '-' + 3 * '='):
        i = 0
        cur_power = 10
        wap = 0
        for loop in range(2024):
            for field in track:
                action = plan[i % len(plan)] if field in '=S' else field
                cur_power += (1 if action == '+' else -1 if action == '-' else 0)
                wap += cur_power
                i += 1

        if wap > a_score:
            result += 1

    print(result)


if __name__ == '__main__':

    data = []
    for i in range(1, 4):
        with open('07_p%d.txt' % i) as file:
            data.append({x.split(':')[0]: x.split(':')[1].split(',')
                         for x in file.read().splitlines()})

    solve_part_one(data[0])
    solve_part_two(data[1])
    solve_part_three(data[2])
