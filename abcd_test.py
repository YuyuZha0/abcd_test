from itertools import product
from typing import Literal, Tuple

ChoiceType = Literal['A', 'B', 'C', 'D']


def p0(choice: ChoiceType, hypo: Tuple[ChoiceType]):
    return True


def p1(choice: ChoiceType, hypo: Tuple[ChoiceType]):
    if choice == 'A':
        return hypo[4] == 'C'
    if choice == 'B':
        return hypo[4] == 'D'
    if choice == 'C':
        return hypo[4] == 'A'
    if choice == 'D':
        return hypo[4] == 'B'
    return None


def p2(choice: ChoiceType, hypo: Tuple[ChoiceType]):
    if choice == 'A':
        return hypo[2] != hypo[5] and hypo[2] != hypo[1] and hypo[2] != hypo[3]
    if choice == 'B':
        return hypo[5] != hypo[2] and hypo[5] != hypo[1] and hypo[5] != hypo[3]
    if choice == 'C':
        return hypo[1] != hypo[2] and hypo[1] != hypo[5] and hypo[1] != hypo[3]
    if choice == 'D':
        return hypo[3] != hypo[2] and hypo[3] != hypo[5] and hypo[3] != hypo[1]
    return None


def p3(choice: ChoiceType, hypo: Tuple[ChoiceType]):
    if choice == 'A':
        return hypo[0] == hypo[4]
    if choice == 'B':
        return hypo[1] == hypo[6]
    if choice == 'C':
        return hypo[0] == hypo[8]
    if choice == 'D':
        return hypo[5] == hypo[9]
    return None


def p4(choice: ChoiceType, hypo: Tuple[ChoiceType]):
    if choice == 'A':
        return hypo[4] == hypo[7]
    if choice == 'B':
        return hypo[4] == hypo[1]
    if choice == 'C':
        return hypo[4] == hypo[8]
    if choice == 'D':
        return hypo[4] == hypo[6]
    return None


def p5(choice: ChoiceType, hypo: Tuple[ChoiceType]):
    if choice == 'A':
        return hypo[7] == hypo[1] and hypo[7] == hypo[3]
    if choice == 'B':
        return hypo[7] == hypo[0] and hypo[7] == hypo[5]
    if choice == 'C':
        return hypo[7] == hypo[2] and hypo[7] == hypo[9]
    if choice == 'D':
        return hypo[7] == hypo[4] and hypo[7] == hypo[8]
    return None


def p6(choice: ChoiceType, hypo: Tuple[ChoiceType]):
    na, nb, nc, nd = 0, 0, 0, 0
    for x in hypo:
        if x == 'A':
            na += 1
        if x == 'B':
            nb += 1
        if x == 'C':
            nc += 1
        if x == 'D':
            nd += 1
    min_opt = min(na, nb, nc, nd)
    if choice == 'A':
        return nc == min_opt
    if choice == 'B':
        return nb == min_opt
    if choice == 'C':
        return na == min_opt
    if choice == 'D':
        return nd == min_opt
    return None


def p7(choice: ChoiceType, hypo: Tuple[ChoiceType]):
    x = ord(hypo[0])
    if choice == 'A':
        return abs(x - ord(hypo[6])) != 1
    if choice == 'B':
        return abs(x - ord(hypo[4])) != 1
    if choice == 'C':
        return abs(x - ord(hypo[1])) != 1
    if choice == 'D':
        return abs(x - ord(hypo[9])) != 1
    return None


def p8(choice: ChoiceType, hypo: Tuple[ChoiceType]):
    a = hypo[0] == hypo[5]
    if choice == 'A':
        return a != hypo[5] == hypo[4]
    if choice == 'B':
        return a != hypo[9] == hypo[4]
    if choice == 'C':
        return a != hypo[1] == hypo[4]
    if choice == 'D':
        return a != hypo[8] == hypo[4]
    return None


def p9(choice: ChoiceType, hypo: Tuple[ChoiceType]):
    na, nb, nc, nd = 0, 0, 0, 0
    for x in hypo:
        if x == 'A':
            na += 1
        if x == 'B':
            nb += 1
        if x == 'C':
            nc += 1
        if x == 'D':
            nd += 1
    delta = max(na, nb, nc, nd) - min(na, nb, nc, nd)
    if choice == 'A':
        return delta == 3
    if choice == 'B':
        return delta == 2
    if choice == 'C':
        return delta == 4
    if choice == 'D':
        return delta == 1
    return None


def test_hypo(problem_list, hypo) -> bool:
    for i, p in enumerate(problem_list):
        if not p(hypo[i], hypo):
            return False
    return True


def main():
    problem_list = (p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)
    for hypo in product('ABCD', repeat=len(problem_list)):
        if test_hypo(problem_list, hypo):
            print('Answers:', hypo)


if __name__ == '__main__':
    main()
