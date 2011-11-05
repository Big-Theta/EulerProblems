require 'Qt'

$RIGHT = 0
$UP =    1
$LEFT =  2
$DOWN =  3

$SPACING = 10

def gen_directions val
    directions = "Fa"
    ret = []

    (1..val).each do
        directions.gsub! 'a', 'A'
        directions.gsub! 'b', 'B'
        directions.gsub! 'A', 'aRbFR'
        directions.gsub! 'B', 'LFaLb'
    end

    directions.each_char {|c| ret.push c}
    ret
end

class QtApp < Qt::Widget
    slots "pressed()"
    attr_accessor :loc, :dir, :segs

    def initialize
        super
        @dir = $UP

        setWindowTitle "Heighway Dragon"

        resize 350, 280
        move 300, 150

        @loc = center
        @segs = []

        @button = Qt::PushButton.new 'Push me', self
        connect @button, SIGNAL('clicked()'), self, SLOT('pressed()')

        @steps = 0
        @directions = gen_directions(10)
        puts @directions

        show
    end

    def next_c
        @directions.shift
    end

    def center
        Qt::Point.new((self.size.width / 2), (self.size.height / 2))
    end

    def pressed
        parse!
        update
    end

    def parse!
        val = next_c
        case val
        when 'a'
            parse!
        when 'b'
            parse!
        when 'F'
            @steps += 1
            puts @steps.to_s
            forward!
        when 'L'
            left!
            parse!
        when 'R'
            right!
            parse!
        else
            parse!
        end
    end

    def paintEvent event
        pen = Qt::Painter.new self
        drawStep pen
        pen.end
    end

    def drawStep pen
        pen.setPen Qt::Color.new 150, 150, 150
        @segs.each {|seg| pen.drawLine seg}
    end

    def right!
        @dir = (@dir + 1) % 4
    end

    def left!
        @dir = (@dir + 3) % 4
    end

    def forward!
        new_x = nil
        new_y = nil

        case @dir
        when 0
            new_x = @loc.x + $SPACING
            new_y = @loc.y
        when 1
            new_x = @loc.x
            new_y = @loc.y - $SPACING
        when 2
            new_x = @loc.x - $SPACING
            new_y = @loc.y
        when 3
            new_x = @loc.x
            new_y = @loc.y + $SPACING
        end

        new = Qt::Line.new(Qt::Point.new(@loc), Qt::Point.new(new_x, new_y))
        segs.push new
        @loc = Qt::Point.new new_x, new_y
    end
end

app = Qt::Application.new ARGV
QtApp.new
app.exec
