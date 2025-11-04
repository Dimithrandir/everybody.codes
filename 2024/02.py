def solve_part_one(words, text):

    print(sum([text.count(x) for x in words]))


def solve_part_two(words, text):

    symbols = set()
    for i in range(len(text)):
        for word in words:
            rev_word = ''.join(list(reversed(list(word))))
            if text[i:].startswith(word) or text[i:].startswith(rev_word):
                for j in range(i, i+len(word)):
                    symbols.add(j)

    print(len(symbols))


def solve_part_three(words, text):

    text = text.splitlines()
    scales = set()
    for word in words:
        rev_word = ''.join(list(reversed(list(word))))
        for i in range(len(text)):
            row_base = text[i]
            row_ext = row_base + row_base[:len(word)-1]
            for j in range(len(row_ext)):
                if row_ext[j:].startswith(word) or row_ext[j:].startswith(rev_word):
                    for k in range(j, j + len(word)):
                        scales.add((i, k % len(row_base)))
        for j in range(len(text[0])):
            column = ''.join([text[x][j] for x in range(len(text))])
            for i in range(len(column)):
                if column[i:].startswith(word) or column[i:].startswith(rev_word):
                    for k in range(i, i + len(word)):
                        scales.add((k, j))

    print(len(scales))


if __name__ == '__main__':

    words = []
    text = []
    for i in range(1, 4):
        with open('02_p%d.txt' % i) as file:
            data = file.read().split('\n\n')
            words.append(data[0][6:].split(','))
            text.append(data[1])

    solve_part_one(words[0], text[0])
    solve_part_two(words[1], text[1])
    solve_part_three(words[2], text[2])
