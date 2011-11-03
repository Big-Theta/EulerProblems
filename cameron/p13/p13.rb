def problem13
  numbers_in = File.new("numbers.txt")
  line = numbers_in.gets()
  total = 0
  while line
    line = line.slice(0, 13).to_i
    total += line
    line = numbers_in.gets()
  end
  total

end
