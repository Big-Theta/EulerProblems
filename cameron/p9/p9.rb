def problem9 ( )
  answer = false
  (1..1000).each do |x|
    (x..1000).each do |y|
      z = 1000 - x - y
      if ((x ** 2) + (y ** 2) == (z ** 2))
        answer = x * y * z
      end
    end
  end
  answer
end
