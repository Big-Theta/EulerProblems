# Copyright (c) 2011 the authors listed at the following URL, and/or
# the authors of referenced articles or incorporated external code:
# http://en.literateprograms.org/Miller-Rabin_primality_test_(Ruby)?action=history&offset=20090326153929
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
# Retrieved from: http://en.literateprograms.org/Miller-Rabin_primality_test_(Ruby)?oldid=16299


def modPow(x, r, m)
    y = r
    z = x
    v = 1
    while y > 0
        u = y % 2
        t = y / 2
        if u == 1
            v = (v * z) % m
        end
        z = z * z % m
        y = t
    end
    return v
end


def miller_rabin_pass(a, n)
    d = n - 1
    s = 0
    while d % 2 == 0 do
        d >>= 1
        s += 1
    end


    a_to_power = modPow(a, d, n)
    if a_to_power == 1
        return true
    end
    for i in 0...s do
        if a_to_power == n - 1
            return true
        end
        a_to_power = (a_to_power * a_to_power) % n
    end
    return (a_to_power == n - 1)
end


def miller_rabin(n)
    k = 20
    for i in 0...k do
        a = 0
        while a == 0
             a = rand(n)
        end
        if (!miller_rabin_pass(a, n))
            return false
        end
    end
    return true
end


if ARGV[0] == "test"
    n = ARGV[1].to_i
    puts (miller_rabin(n) ? "PRIME" : "COMPOSITE")
elsif ARGV[0] == "genprime"
    nbits = ARGV[1].to_i
    while true
        p = rand(2**nbits)
        if (p % 2 == 0)
            next
        elsif (p % 3 == 0)
            next
        elsif (p % 5 == 0)
            next
        elsif (p % 7 == 0)
            next
        end

        if miller_rabin(p)
            puts "#{p}"
            break
        end
    end
end

