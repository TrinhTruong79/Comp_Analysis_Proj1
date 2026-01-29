class Bus:
    def __init__(self, name: str):
        self.name = name
        self.v = None

    def set_bus_v(self, bus_v: float):
        self.v = float(bus_v)