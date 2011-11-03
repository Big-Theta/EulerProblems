load 'message.rb'

def find_white_space(start)
  c = Hash.new(0)
  (start...$message.length).step(3) do |i|
    c[$message[i]] += 1
  end
  answer = [0, 0]
  c.each do |val, times|
    if (times > answer[1])
      answer[0] = val
      answer[1] = times
    end
  end
  answer[0]
end

def problem59 ( )
  code = [find_white_space(0) ^ 32,
          find_white_space(1) ^ 32,
          find_white_space(2) ^ 32]
  answer = 0
  (0...$message.length).each do |i|
    c = $message[i] ^ code[i % 3]
    answer += c
  #  printf("%s", c.chr)
  end
  answer
end
