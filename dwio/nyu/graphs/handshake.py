from __future__ import annotations


def test_graph_from_degrees(*inlist):
    if sum(inlist) % 2 == 0:
        return True
    return False


class CompleteK(object):
    def __init__(self, nodes: int):
        self.nodes = nodes

    @property
    def edge_count(self) -> int:
        return self.nodes * (self.nodes - 1) // 2
