def problem260(max)
  (0..max).each do |x|
    (x..max).each do |y|
      (y..max).each do |z|
        puts "#{x}, #{y}, #{z}"
      end
    end
  end
end
