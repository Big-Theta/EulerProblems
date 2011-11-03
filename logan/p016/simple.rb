c = 0
a = (2 ** 1000).to_s.each_char {|v| c += v.to_i}
puts c
