import math as m
import numpy as np
import pylab
from matplotlib.patches import Ellipse
import matplotlib.lines as mlines


class Beam(object):
    def __init__(self, point):
        """
        Initializes the instance attributes that will eventually be set.
        start and end are assumed to be 2-tuples representing x, y
        coordinates.  Slope is the rise over the run for the current
        line

        or equivalently, the
        (start[1] - end[1]) / (start[0] - end[0])
        """
        self.start = point
        self.end = None
        self.slope = None
        self.angle = None

    def info(self, extra=True):
        print "==== info ===="
        print "Starting point:", self.start
        print "Ending point:  ", self.end
        if extra:
            print "Slope:         ", self.get_slope()
            print "Angle:         ", self.angle
        print "=============="

    def set_end(self, new_point):
        self.end = new_point

    def set_slope(self, slope):
        """Sets the slope and derives the angle for this beam."""
        self.slope = slope
        self.angle = m.atan(self.slope)

    def get_slope(self):
        if not self.slope:
            assert (self.start and self.end)
            self.set_slope((self.end[1] - self.start[1]) /
                           (self.end[0] - self.start[0]))
        return self.slope

    def done(self):
        if ((-0.01 < self.end[0] and self.end[0] < 0.01) and
            (nearly_equal(10, self.end[1], 1))):
            return True
        return False

    def get_y_intercept(self):
        """
        y = mx + b
        b = y - mx

        """
        return self.start[1] - self.get_slope() * self.start[0]

    def get_next_beam(self):
        """Derives the next beam using the information from the
        current beam.

        """
        new_beam = Beam(self.end)
        self._derive_next_slope(new_beam)
        self._derive_next_end(new_beam)
        assert new_beam.end
        return new_beam

    def _derive_next_slope(self, new_beam):
        """
        FIXME: This code does NOT work.

        The tangent slope is given: -4x/y.

        """
        tan_slope = -4 * self.end[0] / self.end[1]  # Given
        new_beam.set_slope(reflect(self.get_slope(), tan_slope))

    def _derive_next_end(self, new_beam):
        """
        Equation of ellipse:
        4x^2 + y^2 = 100
        y = (+/-)sqrt(100 - 4x^2); x = sqrt(100 - y^2)

        Equation of line: (m, x_0, y_0 are known, need to find b)
        y = mx + b

        Set the two versions of y equal:
        mx + b = sqrt(100 - 4x^2)
        (mx + b)^2 = 100 - 4x^2
        m^2x^2 + 2mbx + b^2 = 100 - 4x^2
        (m^2 + 4)x^2 + 2mbx + b^2 - 100 = 0
        A = m^2 + 4, B = 2mb, C = b^2 - 100

        Quadratic formula:
        Ax^2 + Bx + C = 0 --> x = (-B + (+/-)sqrt(B^2 - 4AC)) / 2A

        x = (-2mb + (+/-)sqrt((2mb)^2 - 4(m^2 + 4)(b^2 - 100))) / 2(m^2 + 4)

        Try to capture common portions of these equations. alpha will
        be the part that is different in the two cases.

        """
        candidates = intersect_all(new_beam.get_slope(),
                                   new_beam.get_y_intercept())
        new_end = None
        for candidate in candidates:
            if not candidate:
                pass
            elif (nearly_equal(candidate[0], new_beam.start[0], 2) and
                  nearly_equal(candidate[1], new_beam.start[1], 2)):
                pass
            elif (abs(candidate[0]) > 5):
                pass
            elif (abs(candidate[1]) > 10):
                pass
            else:
                if new_end:
                    assert False
                new_end = candidate
        new_beam.end = new_end


def _intersect_y(m_, x, b):
    return m_ * x + b


def intersect_p(m_, b):
    num = (-2 * m_ * b +
           (m.sqrt((2 * m_ * b) ** 2 -
            4 * (m_ ** 2 + 4) * (b ** 2 - 100))))
    denom = 2 * (m_ ** 2 + 4)
    x = num / denom
    y = _intersect_y(m_, x, b)
    return (x, y)


def intersect_n(m_, b):
    num = (-2 * m_ * b -
           (m.sqrt((2 * m_ * b) ** 2 -
                   4 * (m_ ** 2 + 4) * (b ** 2 - 100))))
    denom = 2 * (m_ ** 2 + 4)
    x = num / denom
    y = _intersect_y(m_, x, b)
    return (x, y)


def intersect_all(m_, b):
    retval = []
    point = None
    for func in [intersect_p, intersect_n]:
        try:
            point = func(m_, b)
            if not nearly_equal(4 * (point[0] ** 2) + point[1] ** 2,
                                100, 2):
                pass
            retval.append(point)
        except ValueError:
            retval.append(None)
    return retval


def clean_angle(angle):
    mod_2pi = m.radians(m.degrees(angle))
    while 0 > mod_2pi or mod_2pi > (2 * m.pi):
        if mod_2pi < 0:
            mod_2pi += 2 * m.pi
        if mod_2pi >= (2 * m.pi):
            mod_2pi -= 2 * m.pi
    return mod_2pi


def reflect(slope, reflection_slope):
    """
    We can derive the angle of this tangent using the atan function.
    The angle for the new will be calculated by taking twice the
    difference in the angles and adding this quantity to the angle of
    the beam. The idea here is that once the first beam bounces, we
    could look at the original path and then the new path.  The
    tangent line will be halfway between these two paths.  Note: there
    are two possible differences in angles...  a big difference and a
    small difference. The angle for the new beam should be the same
    regardless of our choice (big or small difference).

    Perhaps this observation can be used to check the results?

    """
    reflection_angle = m.atan(reflection_slope)
    angle = m.atan(slope)

    difference = angle - reflection_angle
    new_angle = clean_angle(reflection_angle - difference)
    new_slope = m.tan(new_angle)

    other_difference = m.pi - (angle - reflection_angle)
    other_angle = clean_angle(angle + 2 * other_difference)
    other_slope = m.tan(other_angle)
    assert (nearly_equal(other_slope, new_slope, 5))

    return new_slope


def nearly_equal(a, b, n=3):
    threshhold = .1 ** n
    if (a - threshhold < b and a + threshhold > b):
        return True
    else:
        return False


if __name__ == '__main__':
    start = Beam((0, 10.1))
    start.set_end((1.4, -9.6))
    start.set_slope((start.end[1] - start.start[1]) /
                    (start.end[0] - start.start[0]))
    prev = start

    count = 1
    x_points = []
    y_points = []
    p = None
    while not prev.done():
        print count, prev.end
        p = prev.end
        x_points.append(p[0])
        y_points.append(p[1])
        next_beam = prev.get_next_beam()
        prev = next_beam
        count += 1
    print "Out at", count, prev.end

    ells = [Ellipse(xy=(0, 0), width=10, height=20)]

    fig = pylab.figure()
    ax = fig.add_subplot(111, aspect='equal')
    for e in ells:
        ax.add_artist(e)
        e.set_clip_box(ax.bbox)
        e.set_alpha(pylab.rand())
        e.set_facecolor(pylab.rand(3))

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)


    # add a line
    x,y = np.array([x_points, y_points])
    line = mlines.Line2D(x, y)

    ax.add_line(line)

    pylab.show()

