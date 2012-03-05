require 'prime'
require 'time'

def gen_primes n, my_max
    (n..my_max).each do |x|
        yield x if x.prime?
    end
end

def longest_for_seed n, max=1_000_000
    memo = []
    val = 0
    gen_primes(n, max) do |x|
        val += x
        memo.push x
        break if val > max
    end

    while 1 do
        return val, memo.length if val.prime?
        val -= memo.pop
    end
end

def longest_for_max my_max=1_000_000
    max_val = 0
    max_len = 0
    gen_primes(2, my_max=my_max) do |p|
        v, l = longest_for_seed(p, my_max=my_max)
        if l > max_len
            max_len = l
            max_val = v
        end
    end
    return max_val, max_len
end

if __FILE__ == $0
    start = Time.now
    val, len = longest_for_max
    puts val
    puts len
    puts Time.now - start
end
