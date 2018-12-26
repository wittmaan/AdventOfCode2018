
# --- Day 20: A Regular Map ---

from collections import defaultdict

DIRECTION = {'E': (0, 1), 'W': (0, -1), 'N': (-1, 0), 'S': (1, 0)}


def parse(x):
    pos = (0, 0)
    result = defaultdict(list)
    stack = []

    for i, c in enumerate(x[1:-1]):
        if c in "ENSW":
            oldpos = pos
            dx, dy = DIRECTION[c]
            x, y = pos
            pos = (x + dx, y + dy)
            result[oldpos].append(pos)
        elif c == '(':
            stack.append(pos)
        elif c == ')':
            pos = stack.pop()
        elif c == '|':
            pos = stack[-1]
    return result


def count_visits(x):
    stack = [(0, 0)]
    seen = {(0, 0): 0}
    while len(stack) != 0:
        pos = stack.pop()
        for adjacent_pos in x[pos]:
            if adjacent_pos not in seen:
                seen[adjacent_pos] = seen[pos] + 1
                stack.append(adjacent_pos)
    # print("we have seen this positions {}".format(seen))
    return seen


def get_max_path(x):
    return max([v for v in x.values()])


def count_above(x):
    return len([v for v in x.values() if v >= 1000])


if __name__ == '__main__':
    sample_input1 = "^WNE$"
    assert get_max_path(count_visits(parse(sample_input1))) == 3

    sample_input2 = "^ENWWW(NEEE|SSE(EE|N))$"
    assert get_max_path(count_visits(parse(sample_input2))) == 10

    sample_input3 = "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"
    assert get_max_path(count_visits(parse(sample_input3))) == 18

    sample_input4 = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"
    assert get_max_path(count_visits(parse(sample_input4))) == 23

    sample_input5 = "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"
    assert get_max_path(count_visits(parse(sample_input5))) == 31

    # part 1
    data = open('../resources/day20input.txt').read().strip()
    print(get_max_path(count_visits(parse(data))))

    # part 2
    print(count_above(count_visits(parse(data))))
