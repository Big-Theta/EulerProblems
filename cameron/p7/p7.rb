#Cameron Evans

#Return the 10,001st prime number
def problem7 ( )
  a = []
  testnum = 1
  while (a.length < 10001)
    testnum += 1
    a.push(testnum)
    i = 0
    while (i < a.length)
      if (testnum % a[i] == 0 && a[i] != testnum)
        a.pop
        i = a.length
      end
      i += 1
    end
  end
  testnum
end
