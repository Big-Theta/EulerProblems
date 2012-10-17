import math as m

class Beam(object):
    def __init__(self, x, y):
        self.start_x, self.start_y = x, y
        self.end_x = self.end_y = self.slope = self.angle = None

    def info(self):
        print "Starting point:", self.start_x, self.start_y
        print "Ending point:  ", self.end_x, self.end_y
        print "Slope:         ", self.slope

    def set_end(self, x, y):
        self.end_x, self.end_y = x, y

    def set_slope(self, slope):
        self.slope = slope
        self.angle = m.atan(self.slope)

    def get_next_beam(self):
        new_beam = Beam(self.end_x, self.end_y)
        self._derive_next_slope(new_beam)
        self._derive_next_end(new_beam)
        return new_beam

    def _derive_next_slope(self, new_beam):
        """
        This has NOT been checked.

        """
        tan_slope = -4 * self.end_x / self.end_y  # Given
        tan_angle = m.atan(tan_slope)
        difference = tan_angle - cur_angle
        new_angle = cur_angle + 2 * difference
        new_slope = m.tan(new_angle)

        '''
        cur_angle = self.angle
        cur_slope = self.slope
        for k, v in locals().items():
            print k, v
        '''
        new_beam.set_slope(new_slope)

    def _derive_next_end(self, new_beam):
        """
        Equation of ellipse:
        4x^2 + y^2 = 100
        y = sqrt(100 - 4x^2); x = sqrt(100 - y^2)

        Equation of line: (m, x_0, y_0 are known, need to find b)
        y = mx + b

        Set the two versions of y equal:
        mx + b = sqrt(100 - 4x^2)
        (mx + b)^2 = (+/-)(100 - 4x^2)

        The Positive version is valid for the top half of the ellipse, while the
        Negative version is valid for the bottom half. It is plausible for both the
        start and end point to be in the same half. We need to figure out whether the
        final point will be in the top or bottom half of the ellipse. We can do that
        by creating the line from the current point to either (-5, 0) or (5, 0), where
        the ellipse intersects the X axis. If the first point is in the bottom
        half, and the line's slope creates a line that is "beneath" this
        constructed slope, then we need to take the Negative version. A similar test
        will work if the first point is above the X axis. However, it might be better
        to just solve both the positive and the negative version, and at the end,
        we should be able to isolate the correct solutions. See below for a discussion
        on that.

        Positive version:                   | Negative version:
        m^2x^2 + 2mbx + b^2 = 100 - 4x^2    | m^2x^2 + 2mbx + b^2 = 4x^2 - 100
        (m^2 + 4)x^2 + 2mbx + b^2 - 100 = 0 | (m^2 - 4)x^2 + 2mbx + b^2 + 100 = 0
        A = m^2 + 4, B = 2mb, C = b^2 - 100 | A = m^2 - 4, B = 2mb, C = b^2 + 100

        Quadratic formula:
        Ax^2 + Bx + C = 0 --> x = -B + (+/-)sqrt(B^2 - 4AC) / 2A

        Positive version:
        x = -2mb + (+/-)sqrt((2mb)^2 - 4(m^2 + 4)(b^2 - 100)) / 2(m^2 + 4)

        Negative version:
        x = -2mb + (+/-)sqrt((2mb)^2 - 4(m^2 - 4)(b^2 + 100)) / 2(m^2 - 4)

        With these, one x will be outside of [-5, 5]. The other x will be
        inside, and will be the correct one.

        We can match 4 points using the equation for the ellipse and the quadratic
        formula. The starting point will be one of these 4 points. With the other
        three points, I suspect that two of them will have x values that are outside
        of the range of [-5, 5]. If this is true, then it will be trivial to identify
        which point is the true ending point.

        """


if __name__ == '__main__':
    #start = Beam(0, 10.1)
    #start.set_end(1.4, -9.6)
    start = Beam(0.0, 5.0)
    start.set_end(-5.0, 0.1)
    start.set_slope((start.end_y - start.start_y) /
                    (start.end_x - start.start_x))
    start.info()
    start.get_next_beam()

