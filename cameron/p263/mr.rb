require 'time'


#################
class Integer
    def prime? k=5
        return true if self == 2
        return false if self < 2
        #return false if self & 1 == 0
        return false if self % 2 == 0

        return false if self > 3 && self % 6 != 1 && self % 6 != 5     # added

        d = self - 1
        d >>= 1 while d & 1 == 0

        k.times do
            a = rand(self - 2) + 1
            t = d
            y = ModMath.pow(a, t, self)                  # implemented below

            while t != self - 1 && y != 1 && y != self - 1
                y = (y * y) % self
                t <<= 1
            end

            return false if y != self - 1 && t & 1 == 0
        end
        return true
    end
end

module ModMath
    def ModMath.pow(base, power, mod)
        result = 1

        while power > 0
            result = (result * base) % mod if power & 1 == 1
            base = (base * base) % mod
            power >>= 1
        end

        result
    end
end

def foo
    start = Time.new
    i = 0
    while Time.new - start < 5 do
        i.prime?
        i += 1
    end
    puts "Got this far: " + i.to_s
end
