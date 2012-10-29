import math as m


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
        self.info()
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
        (mx + b)^2 = (+/-)(100 - 4x^2)

        The Positive version is valid for the top half of the ellipse,
        while the Negative version is valid for the bottom half. It is
        plausible for both the start and end point to be in the same
        half. We need to figure out whether the final point will be in
        the top or bottom half of the ellipse. We can do that by
        creating the line from the current point to either (-5, 0) or
        (5, 0), where the ellipse intersects the X axis. If the first
        point is in the bottom half, and the line's slope creates a
        line that is "beneath" this constructed slope, then we need to
        take the Negative version. A similar test will work if the
        first point is above the X axis. However, it might be better
        to just solve both the positive and the negative version, and
        at the end, we should be able to isolate the correct
        solutions. See below for a discussion on that.

        Positive version:
        m^2x^2 + 2mbx + b^2 = 100 - 4x^2
        (m^2 + 4)x^2 + 2mbx + b^2 - 100 = 0
        A = m^2 + 4, B = 2mb, C = b^2 - 100

        Negative version:
        m^2x^2 + 2mbx + b^2 = 4x^2 - 100
        (m^2 - 4)x^2 + 2mbx + b^2 + 100 = 0
        A = m^2 - 4, B = 2mb, C = b^2 + 100

        Quadratic formula:
        Ax^2 + Bx + C = 0 --> x = (-B + (+/-)sqrt(B^2 - 4AC)) / 2A

        Positive version:
        x = (-2mb + (+/-)sqrt((2mb)^2 - 4(m^2 + 4)(b^2 - 100))) / 2(m^2 + 4)

        Negative version:
        x = (-2mb + (+/-)sqrt((2mb)^2 - 4(m^2 - 4)(b^2 + 100))) / 2(m^2 - 4)

        Try to capture common portions of these equations. alpha will
        be the part that is different in the two cases.

        With these, one x will be outside of [-5, 5]. The other x will
        be inside, and will be the correct one.

        We can match 4 points using the equation for the ellipse and
        the quadratic formula. The starting point will be one of these
        4 points.  With the other three points, I suspect that two of
        them will have x values that are outside of the range of [-5,
        5]. If this is true, then it will be trivial to identify which
        point is the true ending point.

        """
        print "> derive_next_end()"
        print 'new_beam'
        new_beam.info()

        candidates = intersect_all(new_beam.get_slope(),
                                   new_beam.get_y_intercept())
        new_end = None
        for candidate in candidates:
            print "  ::candidate:", candidate
            if not candidate:
                pass
            elif (nearly_equal(candidate[0], new_beam.end[0], 2) and
                  nearly_equal(candidate[1], new_beam.end[1], 2)):
                print "found start...", candidate
                print "start...", new_beam.end
                pass
            elif (abs(candidate[0]) > 5):
                print "outside x...", candidate
                pass
            elif (abs(candidate[1]) > 10):
                print "outside y...", candidate
                pass
            else:
                if new_end:
                    print "=============="
                    for x in candidates:
                        print '?', x
                    print "New end: {0}".format(new_end)
                    print "Candidate: {0}".format(candidate)
                    assert False
                new_end = candidate
                print " ...set candidate:", candidate
        new_beam.end = new_end


def _intersect_y(m_, x, b):
    return m_ * x + b


def intersect_pp(m_, b):
    num = (-2 * m_ * b +
           (m.sqrt((2 * m_ * b) ** 2 -
            4 * (m_ ** 2) * (b ** 2 - 100))))
    denom = 2 * (m_ ** 2 + 4)
    x = num / denom
    y = _intersect_y(m_, x, b)
    print "pp", x, y
    return (x, y)


def intersect_pn(m_, b):
    num = (-2 * m_ * b -
           (m.sqrt((2 * m_ * b) ** 2 -
                   4 * (m_ ** 2) * (b ** 2 - 100))))
    denom = 2 * (m_ ** 2 + 4)
    x = num / denom
    y = _intersect_y(m_, x, b)
    print "pn", x, y
    return (x, y)


def intersect_np(m_, b):
    num = (-2 * m_ * b +
           (m.sqrt((2 * m_ * b) ** 2 -
                    4 * (m_ ** 2 - 4) * (b ** 2 + 100))))
    denom = 2 * (m_ ** 2 - 4)
    x = num / denom
    y = _intersect_y(m_, x, b)
    print "np", x, y
    return (x, y)


def intersect_nn(m_, b):
    num = (-2 * m_ * b -
           (m.sqrt((2 * m_ * b) ** 2 -
                    4 * (m_ ** 2 - 4) * (b ** 2 + 100))))
    denom = 2 * (m_ ** 2 - 4)
    x = num / denom
    y = _intersect_y(m_, x, b)
    print "nn", x, y
    return (x, y)


def intersect_all(m_, b):
    retval = []
    point = None
    for func in [intersect_pp, intersect_pn,
                 intersect_np, intersect_nn]:
        try:
            point = func(m_, b)
            print 'point', point
            print '???', 4 * (point[0] ** 2) + point[1] ** 2
            if not nearly_equal(4 * (point[0] ** 2) + point[1] ** 2,
                                100, 2):
                pass
            retval.append(None)
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
    start = Beam((1.4, -9.6))
    p = (0, 10.1)
    start.set_end(p)
    start.set_slope((start.end[1] - start.start[1]) /
                    (start.end[0] - start.start[0]))
    print '&&&&&&&&&&&&&&&&&&'
    exit()
    start = Beam((0, 10.1))
    p = (1.4, -9.6)
    start.set_end((1.4, -9.6))
    start.set_slope((start.end[1] - start.start[1]) /
                    (start.end[0] - start.start[0]))

    for c in intersect_all(start.get_slope(), start.get_y_intercept()):
        print c

    print "************"
    start.info(False)
    print '**********'
    prev = start

    for _ in range(10):
        next_beam = prev.get_next_beam()
        prev = next_beam
        next_beam.info()

