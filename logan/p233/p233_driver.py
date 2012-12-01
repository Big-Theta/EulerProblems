from p233_cy import *

if __name__ == '__main__':
    start = time.time()
    print "Initializing primes ..."
    start_init_primes = time.time()
    init_primes()
    print "\t\t\t\tdone --", time.time() - start_init_primes, "seconds"

    print "construct_safe_multiples() ..."
    start_construct = time.time()
    construct_safe_multiples()
    print "\t\t\t\tdone --", time.time() - start_construct, "seconds"

    sol = acc_solutions()
    print "Solution:", sol
    print "Time taken:", time.time() - start, "seconds"

