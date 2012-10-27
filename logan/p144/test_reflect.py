import unittest
import math as m
from reflection import *

class TestReflect(unittest.TestCase):
    def test_intersect(self):
        '''
        uut = Beam((0, 10.1))
        uut.set_end((1.4, -9.6))
        uut.info()
        print intersect_all(uut.get_slope(), uut.get_y_intercept())
        uut.info()
        self.fail()
        '''

    def test_reflect(self):
        self.assertAlmostEquals(1, reflect(1, 1), 5)
        self.assertAlmostEquals(m.sqrt(3),
                                reflect(1 / m.sqrt(3), 1),
                                5)

        self.assertAlmostEquals(m.sqrt(3),
                                reflect(m.sqrt(3), m.sqrt(3)),
                                5)
        self.assertAlmostEquals(m.tan(m.radians(15)),
                                reflect(1, 1 / m.sqrt(3)),
                                5)
        self.assertAlmostEquals(-m.tan(m.radians(15)),
                                reflect(-1, -1 / m.sqrt(3)),
                                5)
        self.assertAlmostEquals(-m.tan(m.radians(75)),
                                reflect(-1, -m.sqrt(3)),
                                5)
        for angle in range(360):
            for i in range(360):
                reflect_angle = angle + i
                expected = m.tan(2 * (reflect_angle - angle) + angle)
                reflected =reflect(m.tan(angle),
                                   m.tan(reflect_angle))
                self.assertAlmostEquals(
                        expected,
                        reflected,
                        5,
                        "\nangle: {0}, reflect_angle: {1}, "
                        "expected: {2} reflected: {3} "
                        "expected_angle {4}"
                        "".format(angle, reflect_angle, expected,
                                 reflected,
                                 2 * (reflect_angle - angle) + angle))


if __name__ == '__main__':
    unittest.main()

