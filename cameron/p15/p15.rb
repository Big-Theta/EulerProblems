def problem15 (x, y)
  answer = 0
  answer += paths2(x, y)
  answer
end

def paths (hor, ver)
  answer = 0
  if (hor > 0 and ver > 0)
    answer += paths(hor -1 , ver) + paths(hor, ver - 1)
  elsif (hor > 0)
    answer += paths(hor - 1, ver)
  elsif (ver > 0)
    answer += paths(hor, ver -1)
  else
    answer += 1
  end
  answer
end

def paths2 (hor, ver)
  grid = Hash.new(0)
  (0...hor + 1).each do |x|
    (0...ver + 1).each do |y|
      if (x == 0 or y == 0)
        grid[[x, y]] = 1
      else
        grid[[x, y]] = grid[[x - 1, y]] + grid[[x, y - 1]]
      printf("%i + %i = %i\n", grid[[x - 1, y]], grid[[x, y - 1]], grid[[x, y]])
      end
    end
  end
  grid[[hor, ver]]
end
