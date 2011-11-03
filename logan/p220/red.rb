require 'Qt'

$RIGHT = 0
$UP =    1
$LEFT =  2
$DOWN =  3

def right dir
    (dir + 1) % 4
end

def left dir
    (dir + 3) % 4
end

class QtApp < Qt::Widget
    slots "pressed()"

    def initialize
        super
        @dir = $UP

        setWindowTitle "Heighway Dragon"

        resize 350, 280
        move 300, 150

        @button = Qt::PushButton.new 'Push me', self
        connect @button, SIGNAL('clicked()'), self, SLOT('pressed()')

        show
    end

    def center
        Qt::Point.new((self.size.width / 2), (self.size.height / 2))
    end

    def pressed
        puts center.x
        puts center.y
    end

    def paintEvent event

        pen = Qt::Painter.new self

        drawPatterns pen
        pen.end
    end

    def drawPatterns pen
        pen.setPen Qt::Color.new 150, 150, 150

        pen.drawLine(Qt::Point.new(0, 0),
                     Qt::Point.new(350, 280))
    end
end

app = Qt::Application.new ARGV
QtApp.new
app.exec
