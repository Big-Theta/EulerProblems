#Cameron Evans


#finds the largest prime factor of 600851475143
def problem3 ( )
  n = 600851475143
  i = 1
  while (i < n)
    if n % i == 0
      n /= i
      i -= 2
    end
    i += 2
  end
  n
end

