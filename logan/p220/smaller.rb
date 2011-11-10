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
    attr_accessor :target
    def initialize(x=0, y=0)
        @x, @y = x, y
        #@center = Loc.new 0, 0
        #@end = Loc.new 0, 1
        @dir = $UP # Addressing an off by one initialization in center!
        @center = Point.new 0, 0
        @steps = 0
        first!
    end

    def rot! direction=0
        @dir = (@dir - 1) % 4 if direction == 1
        @dir = (@dir + 1) % 4 if direction == 0
    end

    def first!
        case @dir
        when $RIGHT
            @x = @center.x + 1
        when $UP
            @y = @center.y + 1
        when $LEFT
            @x = @center.x - 1
        when $DOWN
            @y = @center.y - 1
        end
        @steps = 1
        rot!
    end

    def center!
        @steps = 0
        @center = Point.new @x, @y
    end

    def double
        if @steps == 0
            first!
        else
            @steps *= 2
            #rot!
            p_x, p_y = @x - @center.x, @y - @center.y
            n_x, n_y = p_x + p_y, -1 * p_x + p_y
            @x, @y = n_x + @center.x, n_y + @center.y
        end
    end

    def seek
        while @steps < @target do
            if @steps > @target - @steps then
                double # @steps is doubled
                @target = @steps - @target
                center! # @steps is now 0
            else
                double
            end
        end
    end

    def to_s
        "x: #{@x} y: #{@y}"
    end
end

magic = Loc.new
magic.target = 10 ** 12
magic.seek
puts magic
