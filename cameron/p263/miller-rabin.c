/* Copyright (c) 2011 the authors listed at the following URL, and/or
the authors of referenced articles or incorporated external code:
http://en.literateprograms.org/Miller-Rabin_primality_test_(C)?action=history&offset=20060620214840

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Retrieved from: http://en.literateprograms.org/Miller-Rabin_primality_test_(C)?oldid=6349
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "integer.h"

#define COMPOSITE 0
#define PRIME     1


integer modular_exponent(integer base, integer power, integer modulus) {
    int i, bit;
    integer result = create_integer(modulus.num_components + 1);
    integer temp   = create_integer(modulus.num_components*2 + 1);
    set_zero_integer(result);
    result.c[0] = 1;

    for(i=power.num_components - 1; i>=0; i--) {
        for(bit=COMPONENT_BITS-1; bit>=0; bit--) {
            multiply_integer(result, result, temp);
            mod_integer(temp, modulus, result);
            if ((power.c[i] & (1 << bit)) != 0) {
                multiply_integer(result, base, temp);
                mod_integer(temp, modulus, result);
            }
        }
    }

    free_integer(temp);
    return result;
}


int miller_rabin_pass(integer a, integer n) {
    int i, s, result;
    integer a_to_power, d, one, n_minus_one;
    integer temp = create_integer(n.num_components*2 + 1);

    one = create_integer(1);
    set_zero_integer(one);
    one.c[0] = 1;
    n_minus_one = create_integer(n.num_components);
    subtract_integer(n, one, n_minus_one);

    s = 0;
    d = create_integer(n_minus_one.num_components);
    copy_integer(n_minus_one, d);
    while ((d.c[0] % 2) == 0) {
        shift_right_one_integer(d);
        s++;
    }

    a_to_power = modular_exponent(a, d, n);
    if (compare_integers(a_to_power, one) == 0)  { result=PRIME; goto exit; }
    for(i=0; i < s-1; i++) {
        if (compare_integers(a_to_power, n_minus_one) == 0) { result=PRIME; goto exit; }
        multiply_integer(a_to_power, a_to_power, temp);
        mod_integer(temp, n, a_to_power);
    }
    if (compare_integers(a_to_power, n_minus_one) == 0) { result=PRIME; goto exit; }
    result = COMPOSITE;

exit:
    free_integer(temp);
    free_integer(a_to_power);
    free_integer(one);
    free_integer(n_minus_one);
    return result;
}


void random_integer(integer max, integer result) {
    int i, most_sig = max.num_components - 1;
    while (max.c[most_sig] == 0) most_sig--;
    for (i=0; i<most_sig; i++) {
        result.c[i] = rand() % (MAX_COMPONENT + 1);
    }
    result.c[most_sig] = rand() % max.c[most_sig];
}


int miller_rabin(integer n) {
    integer a = create_integer(n.num_components);
    int repeat;
    for(repeat=0; repeat<20; repeat++) {
        do {
            random_integer(n, a);
        } while (is_zero_integer(a));
        if (miller_rabin_pass(a, n) == COMPOSITE) {
            return COMPOSITE;
        }
    }
    return PRIME;
}

/*
int main(int argc, char* argv[]) {
    srand(time(NULL));
    if (strcmp(argv[1], "test") == 0) {
        integer n = string_to_integer(argv[2]);
        puts(miller_rabin(n) == PRIME ? "PRIME" : "COMPOSITE");
    } else if (strcmp(argv[1], "genprime") == 0) {
        integer max = create_integer(atoi(argv[2])/COMPONENT_BITS);
        integer p   = create_integer(max.num_components);
        set_zero_integer(max);
        max.c[max.num_components-1] = MAX_COMPONENT;
        do {
            random_integer(max, p);
            if ((p.c[0] % 2) == 0) continue;
	    if (mod_small_integer(p, 3) == 0) continue;
	    if (mod_small_integer(p, 5) == 0) continue;
	    if (mod_small_integer(p, 7) == 0) continue;

        } while (miller_rabin(p) == COMPOSITE);
        puts(integer_to_string(p));
    }
    return 0;
}

*/
