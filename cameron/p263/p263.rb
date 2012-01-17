#Cameron Evans


load "mr.rb"

def problem263 ( )
  primes = [3]
  testnum = 5
  found = 0
  total = 0
  prime_triplets = 0
  while found < 4
    #puts "testing #{testnum}"
    if testnum.prime?
      if primes[-1] != testnum - 6
        primes = [testnum]
      else
        primes.push(testnum)
      end
      if primes.length >= 4# and test_practicality(testnum - 9)
        prime_triplets += 1
        #found += 1
        #total += testnum - 9
        if prime_triplets % 20 == 0
          puts "found #{found}, paradise = #{testnum - 9}, total = #{total}"
        end
      end
    end
    testnum += 2
  end
  total
end

def test_miller_rabin()
  x = 5
  while x > 0
    y = x.prime?
    if x % 1000001 == 0
      puts "x: #{x}, prime?: #{y}"
    end
    x += 2
  end
end

def test_sexiness (a)
  count = 1
  current = a[-1]
  (2..4).each do |i|
    if a[-i] 
      count += 1
      current = a[-i]
    end
  end
  if count >= 4
    #puts "sexy prime #{a[-1] - 9}"
    true
  else
    false
  end
end

def test_practicality (num)
  #puts "testing #{num}"
  (num - 8..num + 8).step(4) do |x|
    div_sum = 0
    (1..x).each do |d|
      if (x % d == 0)
        if d > (div_sum + 1)
          print "false b/c #{div_sum} + 1 < #{d} testing #{x} part of #{num} \n"
          return false
        end
        div_sum += d
      end
    end
  end
  true
end
