def palindrome?(val)
    if val == val.to_s.reverse.to_i then
        return true
    else
        return false
    end
end

def gen()
    (100..999).each do |a|
        (100..999).each do |b|
            yield a * b
        end
    end
end

def execute()
    max = 0
    gen() do |i|
        if palindrome? i and i > max then
            max = i
        end
    end

    return max
end

start = Time.new
puts execute()
puts Time.new - start
