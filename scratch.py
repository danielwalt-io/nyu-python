import math

from dwio.nyu.algos import eGCD
from dwio.nyu.algos import CRD
from dwio.nyu.counting import StarsAndBars
from dwio.nyu.counting import BinomialCoef
from dwio.nyu.counting import Partition
from dwio.nyu.counting import Stirling
from dwio.nyu.recurrence import Recurrence

from dwio.nyu.graphs import test_graph_from_degrees
from dwio.nyu.graphs import CompleteK
from dwio.nyu.graphs import CycleC


if __name__ == "__main__":

    x = Recurrence((0, 10, 100), (0, 75, -250))
    x.e_vals()



"""
for n in range(1, 8):
    print("Case:", n)
    tot = 0
    for i in range(math.ceil(n/3), n+1):
        if n / i > 3:
            continue
        val = Partition(n, i)
        print(" ", val.short, "=", val.count)


        tot += val.count

    print("======== total ways:", tot)

"""