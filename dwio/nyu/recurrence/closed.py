from __future__ import annotations
import numpy as np

class Recurrence(object):
    def __init__(self, starting_values, multipliers):
        if len(multipliers) != len(starting_values):
            raise Exception("Bad Starting Values")
        self.starting = starting_values
        self.coefs = multipliers
        self.dim = len(starting_values)

    def e_vals(self):
        a = []
        print("MM:\na = {",end="")
        for _ in range(0, self.dim):
            if _ == 0:
                a.append(self.coefs)
                continue
            row = []
            for __ in range(self.dim):
                if _ - 1 == __:
                    row.append(1)
                else:
                    row.append(0)
            a.append(row)

        print(",".join(["{{{}}}".format(",".join([str(val) for val in rows])) for rows in a]), end="")
        print("}\nev = Eigenvalues[a]")
        print("RSolve[{", end="")
        bases = []
        for i in range(self.dim):
            bases.append("f[{}] == {}".format(i, self.starting[i]))
        rec = []
        for i in range(self.dim):
            rec.append("f[n-{}]*({})".format(i+1, self.coefs[i]))

        print(",".join(bases) + ", f[n] ==", " + ".join(rec),"}, f[n], n]")

        mat_a = np.mat(a, dtype=np.int64)

        e_val = np.linalg.eigvals(mat_a)


        return e_val


