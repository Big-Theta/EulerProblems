def gen_primes(max_prime=200000):
    '''Inefficient way to generate primes.'''

    primes = []
    base = 2
    while base <= max_prime:
        for i in range(2, base):
            if base % i == 0:
                break
        else:
            primes.append(base)
            yield base
        base += 1


def max_exp(num, max_val):
    '''Returns a value raised to the largest power that is less than or equal to val'''

    exp = 0

    while num ** exp < max_val:
        exp += 1

    return num ** (exp - 1)


def max_comb(max_val, *nums):
    num2 = nums[-1]
    if len(nums) == 1:
        return max_exp(nums[0], max_val)
    elif len(nums) = 2:
        baseline = max_comb(nums[:-1], max_val) + max_exp(num2, max_val)
        ret = 0

        tmp1 = num1
        tmp2 = num2
        while tmp2 < max_val:
            tmp_acc = tmp1 * tmp2
            if tmp_acc < max_val and tmp_acc > baseline:
                ret = tmp_acc
                tmp1 *= num1
            elif tmp_acc < max_val:
                tmp1 *= num1
            else:
                tmp1 = num1
                tmp2 *= num2

        return ret
    else: # len(nums) > 2


def greedy_refine(maximal):
    refine = list(maximal.keys())
    refine.sort()

    first = refine[0]
    bast = 0

    for val in maximal.keys():
        tmp = max_comb(


def guess(max_val):
    acc = 1

    maximal = {} # add 1 to the sum afterward

    for prime in gen_primes(max_val):
        maximal[max_exp(prime, max_val)] = prime

    refine = list(maximal.keys())
    refine.sort()

    done = False

    

    return sum(maximal.keys()) + 1


if __name__ == '__main__':
    print guess(10)
    #print max_comb(3, 5, 20)
