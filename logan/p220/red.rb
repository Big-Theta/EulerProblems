require 'Qt'

$RIGHT = 0
$UP =    1
$LEFT =  2
$DOWN =  3

$SPACING = 10

def right dir
    (dir + 1) % 4
end

def left dir
    (dir + 3) % 4
end

def forward point, dir
    new_x = nil
    new_y = nil

    case dir
    when 0
        new_x = point.x + $SPACING
        new_y = point.y
    when 1
        new_x = point.x
        new_y = point.y - $SPACING
    when 2
        new_x = point.x - $SPACING
        new_y = point.y
    when 3
        new_x = point.x
        new_y = point.y + $SPACING
    end

    Qt::Point.new(new_x, new_y)
end

class QtApp < Qt::Widget
    slots "pressed()"

    def initialize
        super
        @dir = $UP

        setWindowTitle "Heighway Dragon"

        resize 350, 280
        move 300, 150

        @loc = center

        @button = Qt::PushButton.new 'Push me', self
        connect @button, SIGNAL('clicked()'), self, SLOT('pressed()')

        show
    end

    def center
        Qt::Point.new((self.size.width / 2), (self.size.height / 2))
    end

    def execute choice
        case choice
        when :F
            @loc = forward @loc, @dir
        when :L
            @dir = left @dir
        when :R
            @dir = right @dir
        end

        @loc
    end

    def pressed
        update
    end

    def paintEvent event
        pen = Qt::Painter.new self

        drawStep pen
        pen.end
    end

    def drawStep pen
        pen.setPen Qt::Color.new 150, 150, 150

        pen.drawLine(@loc, (execute :F))
    end
end

app = Qt::Application.new ARGV
QtApp.new
app.exec
