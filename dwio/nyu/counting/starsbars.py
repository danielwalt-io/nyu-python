import math

from dwio.nyu.counting import BinomialCoef
from dwio.nyu.counting import Partition
from dwio.nyu.counting import Stirling

# Heavily guided by:
# https://www.careerbless.com/aptitude/qa/permutations_combinations_imp7.php


class StarsAndBars(object):

    def __init__(self, objects=1, bins=1, distinct_objects=False,
                 distinct_bins=True, allow_zero_bins=False, order_matters=False):
        self.obj = objects
        self.bins = bins
        self.d_obj = distinct_objects
        self.d_bins = distinct_bins
        self.z_bins = allow_zero_bins
        self.ordered = order_matters

    @property
    def formula(self):
        if self.d_bins and not self.d_obj and not self.z_bins:
            return BinomialCoef(self.obj - 1, self.bins - 1).short
        if self.d_bins and not self.d_obj and self.z_bins:
            return BinomialCoef(self.obj + self.bins - 1, self.bins - 1)
        if self.d_bins and self.d_obj and self.z_bins:
            return "({}^{})".format(self.bins, self.obj)
        if self.d_bins and self.d_obj and not self.z_bins:
            return "{}! * {}".format(self.bins,
                                     Stirling(self.obj, self.bins).formula)
        if not self.d_bins and self.d_obj and self.z_bins:
            formulas = []
            for i in range(1, self.bins + 1):
                formulas.append(Stirling(self.obj, i).formula)
            return " + ".join(formulas)

        if not self.d_bins and self.d_obj and not self.z_bins:
            return Stirling(self.obj, self.bins).formula

        if not self.d_bins and not self.d_obj and self.z_bins:
            formulas = []
            for i in range(1, self.bins + 1):
                formulas.append(Partition(self.obj, i).short)
            return " + ".join(formulas)

        if not self.d_bins and not self.d_obj and not self.z_bins:
            return Partition(self.obj, self.bins).short

        raise Exception("UNHANDLED")

    @property
    def count(self):
        if self.d_bins and not self.d_obj and not self.z_bins:
            return BinomialCoef(self.obj - 1, self.bins - 1).count
        if self.d_bins and not self.d_obj and self.z_bins:
            return BinomialCoef(self.obj + self.bins - 1, self.bins - 1).count
        if self.d_bins and self.d_obj and self.z_bins:
            return self.bins**self.obj
        if self.d_bins and self.d_obj and not self.z_bins:
            return math.factorial(self.bins) * \
                   Stirling(self.obj, self.bins).count
        if not self.d_bins and self.d_obj and self.z_bins:
            valz = 0
            for i in range(1, self.bins + 1):
                valz += Stirling(self.obj, i).count
            return valz
        if not self.d_bins and self.d_obj and not self.z_bins:
            return Stirling(self.obj, self.bins).count

        if not self.d_bins and not self.d_obj and self.z_bins:
            valz = 0
            for i in range(1, self.bins + 1):
                valz += Partition(self.obj, i).count
            return valz
        if not self.d_bins and not self.d_obj and not self.z_bins:
            return Partition(self.obj, self.bins).count

        raise Exception("Unhandled")
