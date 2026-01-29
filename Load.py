class Load:
    def __init__(self, name: str, bus1: str, p: float, v: float):
        self.name = name
        self.bus1 = bus1
        self.p = float(p)
        self.v = float(v)

        self.r = None
        self.g = None

    def calc_g(self):
        if self.p == 0:
            self.r = float("inf")
            self.g = 0.0
        else:
            self.r = (self.v ** 2) / self.p
            self.g = 1.0 / self.r

        return self.g