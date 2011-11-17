def problem220(dx, steps)
  cur = dragon(dx)
  remaining_steps = (2**dx) - steps
  while remaining_steps > 0
    dx -= 1
    split = remaining_steps.divmod(2**dx)
    remaining_steps = split[1]
    if split[0] == 1
      pre = dragon(dx)
    else
      pre = problem220(dx, split[1])
      remaining_steps = 0
    end
    cur[0] -= pre[1]
    cur[1] += pre[0]
  end
  cur
end

def dragon_string(dx)
  d0 = "Fa"
  puts d0
  (0...dx).each do |x|
    d0.gsub!("a", "ARBFR")
    d0.gsub!("b", "LFALB")
    d0.gsub!("A", "a")
    d0.gsub!("B", "b")
    puts d0
  end
end

def dragon(dx)
  pos2 = [0, 1]
  (1..dx).each do |x|
    if x % 4 == 0
      pos2[1] -= pos2[0]
      pos2[0] = 0
    elsif x % 4 == 1
      pos2[0] = pos2[1]
    elsif x % 4 == 2
      pos2[0] += pos2[1]
      pos2[1] = 0
    elsif x % 4 == 3
      pos2[1] = -pos2[0]
    end
  end
  pos2
end
