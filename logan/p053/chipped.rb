class Integer
  def factorial
    return 1 if self == 0
    (1..self).inject(:*)
  end
  def choose k
    return self.factorial / (k.factorial * (self - k).factorial)
  end
  def exceed? n
    self > n ? true : false
  end
end


if __FILE__ == $0
  total = 0
  (1..100).each do |x|
    (1..x).each do |y|
      total += 1 if x.choose(y).exceed? 1_000_000
    end
  end
  puts total
end
