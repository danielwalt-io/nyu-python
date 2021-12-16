from __future__ import annotations


class CycleC(object):
    def __init__(self, nodes: int):
        self.nodes = nodes

    @property
    def face_edges(self):
        return self.nodes

    @property
    def is_bipartite(self):
        return self.nodes % 2 == 0

    def unique_edge_by_vert(self, n_shared_vert: int = 0) -> int:
        if n_shared_vert == self.nodes:
            raise Exception("Same Cycle")
        return self.face_edges - n_shared_vert//2
