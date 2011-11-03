accumulator = 0
(1..999).each do |num|
    if num % 3 == 0 or num % 5 == 0 then
        accumulator += num
    end
end
puts accumulator

acc = 0
current = 0
[3, 2, 1, 3, 1, 2, 3].cycle do |val|
    current += val
    acc += current

    break if current >= 999
end
puts acc
