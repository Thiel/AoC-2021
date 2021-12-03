import itertools

def solve(input):
    return sum([after > before for (before, after) in itertools.pairwise(input)])

def solve2(input):
    return sum([sum(after) > sum(before)
                for (before, after) in itertools.pairwise(zip(input, input[1:], input[2:]))])

with open("d1/input", "r") as f:
    data = list(map(int, f.read().splitlines()))
    print(solve(data))
    print(solve2(data))
