
def get_radius(N):
    """
    x^2 + y^2 = z^2  # Pythagorus
    2 * z = N * sqrt(2)  # N * sqrt(2) is diameter
    z = (N * sqrt(2)) / 2

    """
    #return m.sqrt(2 * ((N / 2.0) ** 2))
    return (N * m.sqrt(2.0)) / 2.0


def is_inside(N, x, y):
    h_dist = x - N / 2.0
    v_dist = y - N / 2.0
    cond = h_dist ** 2 + v_dist ** 2
    other = (N ** 2.0) / 2.0

    if cond < other:
        return -1
    elif cond > other:
        return 1
    else:
        return 0


def f(N):
    count = 0
    cond = None
    x = int(m.floor((N + 1) // 2 + get_radius(N)))
    y = (N - 1) // 2

    while x > N // 2:
        cond = is_inside(N, x, y)
        if cond == 0:
            count += 1
            x -= 1
            y += 1
        elif cond == -1:
            y += 1
        else:
            x -= 1

    final = count * 4

    #final = count * 8 - 4
    return final




def h(N):
    c_1 = c_3 = 0
    for divisor in gen_odd_divisors(N):
        if divisor % 4 == 1:
            c_1 += 1
        else:
            c_3 += 1
    print 'c_1', c_1
    print 'c_3', c_3
    return 4 * (c_1 - c_3)


