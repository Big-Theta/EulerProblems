def permutations(seq):
    if len(seq):
        yield seq
    else:
        perms = permutations(seq[:-1])
        for perm in perms:
            for i in range(len(seq) + 1):
                yield perm[:i] + [seq[-1]] + perm[i:]


if __name__ == '__main__':
    permutations([1,2,3])
