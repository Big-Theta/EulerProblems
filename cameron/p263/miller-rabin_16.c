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

typedef unsigned short u16;
typedef unsigned long  u32;

#define COMPOSITE 0
#define PRIME     1


u16 modular_exponent_16(u16 base, u16 power, u16 modulus) {
    u32 result = 1;
    int i;
    for (i=15; i>=0; i--) {
        result = (result*result) % modulus;
        if (power & (1 << i)) {
            result = (result*base) % modulus;
        }
    }
    return (u16)result; /* Will not truncate since modulus is a u16 */
}


int miller_rabin_pass_16(u16 a, u16 n) {
    u16 a_to_power, s, d, i;
    s = 0;
    d = n - 1;
    while ((d % 2) == 0) {
        d /= 2;
        s++;
    }

    a_to_power = modular_exponent_16(a, d, n);
    if (a_to_power == 1) return PRIME;
    for(i=0; i < s-1; i++) {
        if (a_to_power == n-1) return PRIME;
        a_to_power = modular_exponent_16(a_to_power, 2, n);
    }
    if (a_to_power == n-1) return PRIME;
    return COMPOSITE;
}


int miller_rabin_16(u16 n) {
    if (n <= 1) return COMPOSITE;
    if (n == 2) return PRIME;
    if (miller_rabin_pass_16( 2, n) == PRIME &&
        (n <= 7  || miller_rabin_pass_16( 7, n) == PRIME) &&
        (n <= 61 || miller_rabin_pass_16(61, n) == PRIME))
        return PRIME;
    else
        return COMPOSITE;
}


int main(int argc, char* argv[]) {
    u16 n = (u16)atoi(argv[1]);
    puts(miller_rabin_16(n) == PRIME ? "PRIME" : "COMPOSITE");
    return 0;
}

