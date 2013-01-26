def spot_is_in_list(candidate, list_):
    for check in list_:
        if candidate == check:
            return check
    return False


class Spot(object):
    def __init__(self, X, Y, cost=None, steps=None, prev_spot=None):
        self.X = X
        self.Y = Y
        self.cost = cost
        self.steps = steps
        self.prev_spot = prev_spot

    def __str__(self):
        return "X: {self.X} Y: {self.Y} cost: {self.cost} steps: {self.steps}".format(
                                                                            self=self)

    @property
    def X(self):
        try:
            return self._X
        except NameError:
            return None

    @X.setter
    def X(self, rval):
        self._X = int(rval)

    @property
    def Y(self):
        try:
            return self._Y
        except NameError:
            return None

    @Y.setter
    def Y(self, rval):
        self._Y = int(rval)

    @property
    def cost(self):
        try:
            return self._cost
        except AttributeError:
            return None

    @cost.setter
    def cost(self, rval):
        try:
            self._cost = int(rval)
        except TypeError:
            pass

    @property
    def steps(self):
        try:
            return self._steps
        except AttributeError:
            return None

    @steps.setter
    def steps(self, rval):
        try:
            self._steps = int(rval)
        except TypeError:
            pass

    @property
    def prev_spot(self):
        try:
            return self._prev_spot
        except AttributeError:
            return None

    @prev_spot.setter
    def prev_spot(self, prev):
        try:
            self._prev_spot = prev
        except TypeError:
            pass

    def __eq__(self, other):
        if isinstance(other, Spot):
            '''
            if self.X == other.X and self.Y == other.Y:
                return True
            else:
                return False
            '''
            return self.X == other.X and self.Y == other.Y
        else:
            raise NotImplementedError("other is of type " + str(type(other)))

