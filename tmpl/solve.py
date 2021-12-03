import dataclasses
import itertools

def txt2offset(line):
    match line.split():
        case ["forward", x]:
            return complex(int(x), 0)
        case ["down", y]:
            return complex(0, int(y))
        case ["up", y]:
            return complex(0, -int(y))

def solve(data): #x,y
    s = sum(data)
    return s.real * s.imag

with open("d2/input", "r") as f:
    data = list(map(txt2offset, f.read().splitlines()))
    print(solve(data))

####

@dataclasses.dataclass
class Position:
    distance: int
    aim: int
    depth: int

@dataclasses.dataclass
class Move:
    distance: int
    aim: int

def add_pos_move(pos, move):
    return Position(pos.distance + move.distance,
                    pos.aim + move.aim,
                    pos.depth + move.distance * pos.aim)


def txt2move(line):
    match line.split():
        case ["forward", x]:
            return Move(int(x), 0)
        case ["down", y]:
            return Move(0, int(y))
        case ["up", y]:
            return Move(0, -int(y))


def solve2(data):
    *_, last_pos = itertools.accumulate(data, func=add_pos_move, initial=Position(0,0,0))
    return last_pos.distance * last_pos.depth

with open("d2/input", "r") as f:
    data = list(map(txt2move, f.read().splitlines()))
    print(solve2(data))
