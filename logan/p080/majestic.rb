class Fixnum
  def sqrt_irrational?
    return true if Math.sqrt(self) != Math.sqrt(self).to_i
    false
  end

  def sqrt100
    if self.sqrt_irrational?
      val = '0.0'
      while val.length < 102
        val_next = val.succ
        puts val_next + " : " + (val_next.to_f ** 2.0).to_s + " : " + self.to_s
        if val_next.to_f ** 2 > self
          val += '0'
        else
          val = val_next
        end
      end
      val
    end
  end
end

if __FILE__ == $0
  puts 2.sqrt100
end
