

class Euler(object):
    def __init__(self, *edge_degrees):
        self.deg = edge_degrees

    @property
    def is_circuit(self):
        # If any odd degree edge, false
        for _ in self.deg:
            if _ % 2 == 1:
                return False
        return True

    @property
    def is_path(self):
        # If >2 nodes of odd degree, false
        odd_cnt = 0
        for _ in self.deg:
            if _ % 2 == 1:
                odd_cnt += 1
            if odd_cnt > 2:
                return False
        return True