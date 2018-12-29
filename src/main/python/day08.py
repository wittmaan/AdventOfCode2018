
# --- Day 8: Memory Maneuver ---


def parse(it):
    child_nodes = next(it)
    metadata_entries = next(it)
    # print("Got {} child nodes and {} metadata entries".format(child_nodes, metadata_entries))

    children = []
    for i in range(child_nodes):
        sub_children = parse(it)
        children.append(sub_children)

    metadata = []
    for i in range(metadata_entries):
        metadata.append(next(it))

    return metadata, children


def sum_metadata(x):
    metadata, children = x
    result = sum(metadata)
    for child in children:
        result += sum_metadata(child)
    return result


def value(x):
    metadata, children = x
    if not children:
        return sum(metadata)
    else:
        result = 0
        for index in metadata:
            # ensure index in the range of children
            if 1 <= index <= len(children):
                result += value(children[index-1])
        return result


if __name__ == '__main__':
    sample_input1 = list(map(int, "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split(" ")))
    assert sum_metadata(parse(iter(sample_input1))) == 138
    assert value(parse(iter(sample_input1))) == 66

    parsed = parse(iter(map(int, open('../resources/day08input.txt').read().strip().split())))

    # part 1
    print(sum_metadata(parsed))

    # part 2
    print(value(parsed))
