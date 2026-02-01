from Circuit import Circuit


class Solution:
    def __init__(self, circuit: Circuit):
        self.circuit = circuit

    def do_power_flow(self):
        r_total = 0

        for r in self.circuit.resistors.values():
            r_total += r.r

        for l in self.circuit.loads.values():
            l.calc_g()
            r_total += l.r

        v = self.circuit.vsource.v

        self.circuit.buses["a"].set_bus_v(v)
        i = v/r_total

        self.circuit.i = i

        load = next(iter(self.circuit.loads.values()))
        vb = i*load.r

        self.circuit.buses["b"].set_bus_v(vb)















