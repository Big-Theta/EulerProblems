def my_prime?(val)
    return false if val == 1
    return true if val == 2
    return false if val % 2 == 0

    (3..(Math.sqrt(val).ceil)).step(2) do |x|
        return false if val % x == 0
    end

    return true
end

class Fixnum
    def prime?
        return my_prime?(self)
    end
end

class Bignum
    def prime?
        return my_prime?(self)
    end
end

(0..11).each do |i|
  puts i if i.prime?
end

