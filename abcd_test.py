def p0(ans, hypo):
    return True


def p1(ans, hypo):
    if ans == 'A':
        return hypo[4] == 'C'
    if ans == 'B':
        return hypo[4] == 'D'
    if ans == 'C':
        return hypo[4] == 'A'
    if ans == 'D':
        return hypo[4] == 'B'
    return None


def p2(ans, hypo):
    if ans == 'A':
        return hypo[2] != hypo[5] and hypo[2] != hypo[1] and hypo[2] != hypo[3]
    if ans == 'B':
        return hypo[5] != hypo[2] and hypo[5] != hypo[1] and hypo[5] != hypo[3]
    if ans == 'C':
        return hypo[1] != hypo[2] and hypo[1] != hypo[5] and hypo[1] != hypo[3]
    if ans == 'D':
        return hypo[3] != hypo[2] and hypo[3] != hypo[5] and hypo[3] != hypo[1]
    return None


def p3(ans, hypo):
    if ans == 'A':
        return hypo[0] == hypo[4]
    if ans == 'B':
        return hypo[1] == hypo[6]
    if ans == 'C':
        return hypo[0] == hypo[8]
    if ans == 'D':
        return hypo[5] == hypo[9]
    return None


def p4(ans, hypo):
    if ans == 'A':
        return hypo[4] == hypo[7]
    if ans == 'B':
        return hypo[4] == hypo[1]
    if ans == 'C':
        return hypo[4] == hypo[8]
    if ans == 'D':
        return hypo[4] == hypo[6]
    return None


def p5(ans, hypo):
    if ans == 'A':
        return hypo[7] == hypo[1] and hypo[7] == hypo[3]
    if ans == 'B':
        return hypo[7] == hypo[0] and hypo[7] == hypo[5]
    if ans == 'C':
        return hypo[7] == hypo[2] and hypo[7] == hypo[9]
    if ans == 'D':
        return hypo[7] == hypo[4] and hypo[7] == hypo[8]
    return None


def p6(ans, hypo):
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
    if ans == 'A':
        return nc == min_opt
    if ans == 'B':
        return nb == min_opt
    if ans == 'C':
        return na == min_opt
    if ans == 'D':
        return nd == min_opt
    return None


def p7(ans, hypo):
    x = ord(hypo[0])
    if ans == 'A':
        return abs(x - ord(hypo[6])) != 1
    if ans == 'B':
        return abs(x - ord(hypo[4])) != 1
    if ans == 'C':
        return abs(x - ord(hypo[1])) != 1
    if ans == 'D':
        return abs(x - ord(hypo[9])) != 1
    return None


def p8(ans, hypo):
    a = hypo[0] == hypo[5]
    if ans == 'A':
        return a != hypo[5] == hypo[4]
    if ans == 'B':
        return a != hypo[9] == hypo[4]
    if ans == 'C':
        return a != hypo[1] == hypo[4]
    if ans == 'D':
        return a != hypo[8] == hypo[4]
    return None


def p9(ans, hypo):
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
    if ans == 'A':
        return delta == 3
    if ans == 'B':
        return delta == 2
    if ans == 'C':
        return delta == 4
    if ans == 'D':
        return delta == 1
    return None


def test_hypo(problem_list, hypo):
    index = 0
    for p in problem_list:
        if not p.__call__(hypo[index], hypo):
            return False
        index += 1
    return True


def hypo_generator(size):
    num = 1
    for x in range(size):
        num *= 4
    hypo = [None] * size
    for i in xrange(num):
        for j in range(size):
            hypo[j] = ['A', 'B', 'C', 'D'][(i >> (j << 1)) & 3]
        yield hypo


def main():
    problem_list = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9]
    for hypo in hypo_generator(len(problem_list)):
        if test_hypo(problem_list, hypo):
            print 'Answer:', hypo


if __name__ == '__main__':
    main()
