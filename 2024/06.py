# dfs with stack
def find_all_paths(tree, node, path, all_paths):
    path.append(node)
    if node == '@':
        all_paths.append(path.copy())
    elif node in tree.keys():
        for neighbor in tree[node]:
            if neighbor not in ['ANT', 'BUG']:
                find_all_paths(tree, neighbor, path, all_paths)
    path.pop()


def solve_part_one(tree, initials=False):
    # get all paths from root to fruit
    all_paths = []
    find_all_paths(tree, 'RR', [], all_paths)
    # group paths by length
    lengths = {}
    for path in all_paths:
        str_path = ''.join([x[0] for x in path] if initials else path)
        if len(path) not in lengths.keys():
            lengths[len(path)] = [str_path]
        else:
            lengths[len(path)].append(str_path)
    # print the shortest path with unique length
    print(lengths[min(lengths.keys(), key=lambda l: len(lengths[l]))][0])


def solve_part_two(tree, initials=True):

    solve_part_one(tree, initials)


def solve_part_three(tree, initials=True):

    solve_part_one(tree, initials)


if __name__ == '__main__':

    data = []
    for i in range(1, 4):
        with open('06_p%d.txt' % i) as file:
            data.append({x.split(':')[0]: x.split(':')[1].split(',')
                         for x in file.read().splitlines()})

    solve_part_one(data[0])
    solve_part_two(data[1])
    solve_part_three(data[2])
