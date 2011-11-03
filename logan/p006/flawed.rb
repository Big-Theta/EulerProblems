a = (1..100).reduce {|c, x| c += x ** 2}
b = (1..100).reduce {|c, x| c += x} ** 2

puts b - a

puts (((1..100).reduce {|c, x| c += x} ** 2) - ((1..100).reduce {|c, x| c += x ** 2}))
