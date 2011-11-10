$RIGHT = 0
$UP =    1
$LEFT =  2
$DOWN =  3

class Point
    attr_accessor :x, :y

    def initialize x=0, y=0
        @x, @y = x, y
    end
end

class Loc < Point
    def initialize(x=0, y=0)
        @x, @y = x, y
        #@center = Loc.new 0, 0
        #@end = Loc.new 0, 1
        @orientation = $UP
        @steps = 0
        @total_steps = 0
        center!
        first!
    end

    def rot! direction=1
        @orientation = (@orientation - 1) % 4 if direction == 1
        @orientation = (@orientation + 1) % 4 if direction == 0
    end

    def first!
        case @orientation
        when $RIGHT
            @x = @x + @center.x + 1
        when $UP
            @y = @y + @center.y + 1
        when $LEFT
            @x = @x + @center.x - 1
        when $DOWN
            @y = @y + @center.y - 1
        end
        rot!
        @steps = 1
        @total_steps += 1
    end

    def center! x=0, y=0
        @steps = 0
        @center = Point.new x, y
    end

    def double
        if @steps == 0
            first!
        else
            @total_steps += @steps
            @steps *= 2
            rot!
            @x, @y = @y + @x + @center.x, -1 * @x + @y + @center.y
        end
    end

    def to_s
        puts "x: #{@x} y: #{@y} steps: #{@steps} total_steps: #{@total_steps}"
    end
end

a = Loc.new 0, 0
puts a
puts
3.times do
    a.double
puts a
end

puts '------------'
a.center!(a.x, a.y)

3.times do
    a.double
    puts a
end
