def factorial(val)
    if val == 0 then
        return 1
    else
        return val * factorial(val - 1)
    end
end

c = 0
factorial(100).to_s.each_char {|v| c += v.to_i}
uuts c
