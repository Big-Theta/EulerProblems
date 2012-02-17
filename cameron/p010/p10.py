#/usr/bin/python

def problem10():
    prime_list = [2]
    total = 0
    num = 3

    for x in range(2000000):
        if is_prime(x, prime_list):
            total += x
    print total

def is_prime(num, prime_list):
    for prime in prime_list:
        if num % prime == 0:
            return False
    prime_list.append(num)
    print prime_list
    return True
problem10()
