

def eGCD(val_2, val_1, show_work=False):
    _format = "{rem:12,d} = {b:12,d} * {q:<12,d} + {r:<12,d} | {x:12,d} " \
              "{y:12,d} <<< {prev:>30s}"
    _header = "{:>12s} = {:>12s} * {:12s} + {:12s} | {:>12s} {:>12s} <<< {:>30s}"

    def fmt(rem, b, q, r, x, y, xp=None, yp=None):
        if b == 1 and r == 0:
            prev = ""
        else:
            prev = "{:,d} - ({:,d})({:,d})".format(xp, yp, q)

        return _format.format(
            rem=rem,
            b=b,
            q=q,
            r=r,
            x=x,
            y=y,
            prev=prev
        )

    if val_2 < val_1:
        val_2, val_1 = val_1, val_2

    work = []

    def inner(a, b):
        if a % b == 0:
            q = a // b
            if show_work:
                work.append(fmt(a, b, q, 0, 0, 1, 0, 1))
            return b, 0, 1

        else:
            q = a // b
            r = a % b
            _d, _x, _y = inner(b, r)
            __d = _d
            __x = _y
            __y = _x - _y * q
            if show_work:
                work.append(fmt(a, b, q, r, __x, __y, _x, _y))
            return __d, __x, __y

    gcd, e, d = inner(val_2, val_1)

    if show_work:
        print("{:,d} and {:,d}\n".format(val_2, val_1))
        print(_header.format("A", "B", "q", "r", "x'", "y'", "x'' - y'' * q"))
        print("-"*180)
        for _ in reversed(work):
            print(_)
        print("="*180)
        _of = "{:,d} = {:,d}*({:,d})  +  {:,d}*({:,d})\n"
        print(_of.format(gcd, val_2, e, val_1, d))

        if gcd == 1:
            print("{:,d} * {:,d} = 1 mod {:,d}".format(val_2, e % val_1, val_1))
            print("{:,d} * {:,d} = 1 mod {:,d}".format(val_1, d % val_2, val_2))

    return gcd, e, d

