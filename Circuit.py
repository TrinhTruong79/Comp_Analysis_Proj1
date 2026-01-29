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
        self.i = 0.0           # float

    def add_bus(self, bus: Bus):
        self.buses[bus.name] = bus

    def add_resistor_element(self, name: str, bus1: str, bus2: str, r: float):
        resistor = Resistor(name, bus1, bus2, r)
        resistor.calc_g()
        self.resistors[name] = resistor

    def add_load_element(self, name: str, bus1: str, p: float, v: float):
        load = Load(name, bus1, p, v)
        load.calc_g()
        self.loads[name] = load

    def add_vsource_element(self, name: str, bus1: str, v: float):
        self.vsource = Vsource(name, bus1, v)

        # bus connected to vsource gets voltage updated immediately
        if bus1 in self.buses:
            self.buses[bus1].set_bus_v(v)

    def set_i(self, i: float):
        self.i = float(i)

    def print_nodal_voltage(self):
        for bus_name, bus in self.buses.items():
            print(f"Bus {bus_name}: V = {bus.v:.6f} V")

    def print_circuit_current(self):
        print(f"Circuit current I = {self.i:.6f} A")


if __name__ == "__main__":
    c = Circuit("Test Circuit")

    c.add_bus(Bus("A"))
    c.add_bus(Bus("B"))

    c.add_vsource_element("V1", "A", 10.0)
    c.add_resistor_element("R1", "A", "B", 100.0)
    c.add_load_element("Load1", "B", 100.0, 10.0)

    c.print_nodal_voltage()

    c.set_i(0.05)
    c.print_circuit_current()