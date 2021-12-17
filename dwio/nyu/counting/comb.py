import math


class BinomialCoef(object):
    def __init__(self, n, r):
        self.n = n
        self.r = r

    @property
    def count(self):
        return math.factorial(self.n) // (
              math.factorial(self.r) * (math.factorial(self.n - self.r)))

    @property
    def short(self):
        return "({}_C_{})".format(self.n, self.r)

    @property
    def formula(self):
        if self.r > self.n - self.r:
            k = self.r
        else:
            k = self.n - self.r
        numer = []
        for _ in range(self.n, k, -1):
            numer.append(str(_))
        denom = []
        for _ in range(1, k + 1):
            denom.append(str(_))

        return "[{:s}] / [{:s}]".format("*".join([_ for _ in numer]),
                                        "*".join([_ for _ in denom]))


class StirlingSecond(object):
    def __init__(self, objects, bins):
        self.obj = objects
        self.bins = bins

    @property
    def short(self):
        return "Stir({},{})".format(self.obj, self.bins)

    @property
    def formula(self):
        if self.obj == 0 and self.bins == 0:
            return "1"
        if self.bins == 0:
            return "0"
        if self.obj < self.bins:
            return "0"

        valz = ["[1 / {}!] * [".format(self.bins), ]
        for i in range(0, self.bins):
            if ((-1) ** i) == 1:
                if i > 0:
                    valz.append(" + ")
            else:
                valz.append(" - ")

            if i > 0:
                valz.append(BinomialCoef(self.bins, i).short)
                valz.append("*")

            valz.append("({})^{} ".format(self.bins - i, self.obj))
        valz.append("]")
        return "".join(valz)

    @property
    def count(self):
        if self.obj == 0 and self.bins == 0:
            return 1
        if self.bins == 0:
            return 0
        if self.obj < self.bins:
            return 0
        total = 0
        for i in range(0, self.bins):
            b = BinomialCoef(self.bins, i).count
            e = (self.bins - i) ** self.obj
            total += ((-1) ** i) * b * e

        return total // math.factorial(self.bins)


class Partition(object):
    def __init__(self, objects, bins=None):
        self.n = objects
        self.k = bins

    @property
    def short(self):
        if self.k:
            return "Partn({},{})".format(self.n, self.k)
        return "[ Σ_{{i=0}}^{{{}}} Partn({},i) ]".format(self.n, self.n)

    @property
    def count(self):
        if self.k:
            return Partition._value(self.n, self.k)
        val = 0
        for i in range(self.n+1):
            print("  i:", i)
            val += Partition._value(self.n, i)
        return val

    @staticmethod
    def _value(n, k):
        if n == k == 0:
            return 1
        if n <= 0:
            return 0
        if k <= 0:
            return 0

        l = Partition._value(n - 1, k - 1)
        r = Partition._value(n - k, k)
        return l + r
