#Cameron Evans
#cameron_evans87@hotmail.com

#return the sum of all positive numbers below 1000 that are multiples of 3 or 5
def problem1 ( )
  i = 0
  0.upto(999) do |x|
    if (x % 3 == 0 || x % 5 == 0)
      i += x
    end
  end
  i
end
