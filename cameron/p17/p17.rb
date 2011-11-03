def problem17
  answer = 0
  (1..1000).each do |x|
    split = x.divmod(100)
    answer += letters_ones(split[0])
    answer += 3 if split[0] > 0 and split[1] > 0
    answer += letters_tens(split[1]) if split[1] > 0
  end
  answer + 11
end

def letters_ones(x)
  if [1, 2, 6].include?(x)
    3
  elsif [4, 5, 9].include?(x)
    4
  else
    5
  end
end

def letters_tens(x)
  if x > 10 and x < 17
    answer = 7
  elsif x == 10
  answer = 3
  elsif x == 17
    answer = 9
  elsif x == 18 or x == 19
    answer = 8
  else
    split = x.divmod(10)
    if split[0] == 5
      answer = 5
    elsif split[0] == 0
      answer = 0
    else
      answer = 6
    end
    answer += 4 if split[1] > 0
  end
  answer
end

