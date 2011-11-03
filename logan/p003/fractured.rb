require 'prime'

max = 2
val = 600_851_475_143

class Bignum
    def divisor?(val)
        return self % val == 0
    end
end

(3..(Math.sqrt(val).ceil)).step(2) do |x|
    (max = x if x.prime?) if val.divisor?(x)
end

puts max
