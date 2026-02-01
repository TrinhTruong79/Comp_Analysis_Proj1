from Bus import Bus
from Resistor import Resistor
from Load import Load
from Vsource import Vsource


class Circuit:
    def __init__(self, name: str):
        self.name = name
        self.buses = {}        # Dict[str, Bus]
        self.resistors = {}    # Dict[str, Resistor]
        self.loads = {}        # Dict[str, Load]
        self.vsource = None    # Vsource
        self.i = None          # i

    def add_bus(self, bus: str):
        self.buses[bus] = Bus(bus)

    def add_resistor_element(self, name: str, bus1: str, bus2: str, r: float):
        resistor = Resistor(name, bus1, bus2, r)
        self.resistors[name] = resistor

    def add_load_element(self, name: str, bus1: str, p: float, v: float):
        load = Load(name, bus1, p, v)
        self.loads[name] = load

    def add_vsource_element(self, name: str, bus1: str, v: float):
        self.vsource = Vsource(name, bus1, v)


    def set_i(self, i: float):
        self.i = float(i)

    def print_nodal_voltage(self):
        for name, bus in self.buses.items():
            print(f"Bus {name}: V = {bus.v} V")

    def print_circuit_current(self):
        print(f"Circuit current I = {self.i} A")


if __name__ ==  "__main__":
    c = Circuit('Test Circuit')

    c.add_bus("A")
    c.add_bus("B")

    c.add_resistor_element("R1", "A", "B", 10.0)

    c.add_load_element("L1", "B", 2000.0, 100.0)

    c.add_vsource_element("V1", "A", 100.0)

    c.print_nodal_voltage()
    c.print_circuit_current()
