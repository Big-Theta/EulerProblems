require 'Qt'

$RIGHT = 0
$UP =    1
$LEFT =  2
$DOWN =  3

$SPACING = 4

def gen_directions val=10
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
    slots "pressed()", "quit()"
    attr_accessor :loc, :dir, :segs

    def initialize
        super
        @dir = $UP

        setWindowTitle "Heighway Dragon"

        #resize 350, 280
        move 300, 150

        @loc = Qt::Point.new((self.size.width / 2), (self.size.height / 2))
        @segs = []


        vbox = Qt::VBoxLayout.new self
        hbox = Qt::HBoxLayout.new



        @button = Qt::PushButton.new "Don't push me TOO hard...", self
        connect @button, SIGNAL('clicked()'), self, SLOT('pressed()')
        @quit_button = Qt::PushButton.new "Don't push me!", self
        connect @quit_button, SIGNAL('clicked()'), self, SLOT('quit()')

        hbox.addWidget @button, 1, Qt::AlignRight
        hbox.addWidget @quit_button

        vbox.addStretch 1
        vbox.addLayout hbox

        self.showFullScreen

        @steps = 0
        @directions = gen_directions(14)
        @n_steps = 1000

        show
    end

    def quit
        exit
    end

    def next_c
        @directions.shift
    end

    def pressed
        @n_steps.times do
            #sleep 0.1
            parse!
        end
        #puts self.pos
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
            #puts @steps.to_s
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
