import numpy
import itertools
import operator

class BingoCard():
    def __init__(self, data):
        self.card = numpy.matrix(data, dtype=int).reshape(5,5)

    def __contains__(self, draws):
        for line in itertools.chain(self.card[:], self.card.transpose()[:]):
            if len(numpy.intersect1d(numpy.asarray(line).flatten(),draws)) == 5:
                return True
        return False

    def score(self, draws):
        flat_card = numpy.asarray(self.card).flatten()
        return sum(numpy.setdiff1d(flat_card, draws)) * draws[-1]

    def __str__(self):
        return str(self.card)

def convert(entry):
    match len(entry.splitlines()):
        case 1:
            return list(map(int, entry.split(",")))
        case _:
            return BingoCard(entry)

def solve(draft, bingo_cards):
    for i,_ in enumerate(draft):
        for card in bingo_cards:
            if draft[:i] in card:
                return card.score(draft[:i])

def solve2(draft, bingo_cards):
    card_win_pos = []
    for i,_ in enumerate(draft):
        for card in bingo_cards:
            if draft[:i] in card and card not in [e for _,e in card_win_pos]:
                card_win_pos.append((draft[:i], card))
    card_win_pos.sort(key=lambda e: len(e[0]))
    print(len(draft), len(bingo_cards), len(card_win_pos))
    draft, last_card = card_win_pos[-1]
    return last_card.score(draft)

with open("d4/input", "r") as f:
    data = list(map(convert, f.read().split("\n\n")))
    print(solve(data[0], data[1:]))
    print(solve2(data[0], data[1:]))
