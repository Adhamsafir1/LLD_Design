from berth import Berth

class Cabin:
    def __init__(self, cabin_id):
        self.cabin_id = cabin_id
        self.berths = []
        self._create_berths()

    def _create_berths(self):
        types = ['LB', 'MB', 'UB'] * 2 + ['SUB'] + ['SLB'] * 2
        for i, btype in enumerate(types):
            self.berths.append(Berth(i + 1, btype))

    def get_available_berths(self, btype=None):
        return [b for b in self.berths if b.is_available() and (btype is None or b.type == btype)]
