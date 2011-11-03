#Cameron Evans

#find smallest number that is evenly divisible by all number from 1 to 20
def problem5 ( )
  lcm_1_to_n(20)
end


#find least common multiple of all numbers (1..num)
def lcm_1_to_n (num)
  answer = 1
  answer_factors = Hash.new(0) #key is prime factor, val is number of occurences
  (0..num).each do |x|
    f = 2 #start with first possible prime factor
    x_factors = Hash.new(0)

    #find prime factors for x
    while (x >= f)
      while (x % f == 0)
        x_factors[f] += 1
        x /= f
      end
      f += 1
    end

    #the answer must have as many occurrences of each prime factor as each
    #individual number (1..num).
    x_factors.each do |factor, occurrences|
      if (occurrences > answer_factors[factor])
        answer_factors[factor] = occurrences
      end
    end
  end

  #answer_factors has correct factors. Multiply them for the answer
  answer_factors.each do |factor, occurrences|
    occurrences.times do
      answer *= factor
    end
  end
  answer
end
