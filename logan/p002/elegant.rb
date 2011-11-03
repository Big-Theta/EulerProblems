def next_fib(max)
    a, b = 1, 1
    while a < max
        yield a
        a, b = b, a + b
    end
end

acc = 0
next_fib(4_000_000) {|x| acc += x if x % 2 == 0}

puts acc
