
from dwio.nyu.algos import eGCD


def CRT(*eqns, show_work=False):

    def inner(t1, t2, show_work=False):
        a1 = t1[0]
        a2 = t2[0]
        n1 = t1[1]
        n2 = t2[1]
        if n1 < n2:
            n1, n2 = n2, n1
            a1, a2 = a2, a1

        gcd, m1, m2 = eGCD(n1, n2)
        if gcd != 1:
            raise Exception("gcd is not 1 (valz {} and {}) (it is {})".format(
                n1, n2, gcd
            ))
        n1n2 = n1 * n2
        x = (a1 * m2 * n2 + a2 *m1 * n1) % n1n2
        if show_work:
            print("\niter; Solving:")
            print("  x={:d} mod {:d} and\n  x={:d} mod {:d}\n==========".format(
                a1, n1, a2, n2
            ))
            print("-> eGCD: {:d}, e:{:d}, d:{:d}".format(gcd, m1, m2))
            print("-> so ... x={:d}*({:d})*({:d}) + "
                  "{:d}*({:d})*({:d}) == {:d}".format(
                a1, m2, n2, a2, m1, n1, x
            ))
            print("   because")
            print("   {:,d} * {:,d} = 1 mod {:,d}".format(n1, m1 % n2, n2))
            print("       (inv of {:,d} in mod {:,d} is {:d})".format(n1, n2,
                                                                    m1 % n2))
            print("   {:,d} * {:,d} = 1 mod {:,d}".format(n2, m2 % n1, n1))
            print("       (inv of {:,d} in mod {:,d} is {:d})".format(n2, n1,
                                                                    m2 % n1))
        return dict(x=x, mod=n1n2)

    all_eq = list(eqns)
    to_check = []
    l1 = all_eq.pop(0)
    to_check.append(l1)
    sub = None
    while len(all_eq) > 0:
        l2 = all_eq.pop(0)
        to_check.append(l2)
        sub = inner(l1, l2, show_work)
        l1 = (sub["x"], sub["mod"])

    if show_work:
        print("\nFINALIZING... check them")
        for _ in to_check:
            print("  ", sub["x"], "mod", _[1], "=",
                  sub["x"] % _[1], ", want", _[0])
    return sub
