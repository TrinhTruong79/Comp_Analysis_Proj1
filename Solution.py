from Circuit import Circuit


class Solution:
    def __init__(self, circuit: Circuit):
        self.circuit = circuit

    def do_power_flow(self):
        # 1) Voltage source must exist
        if self.circuit.vsource is None:
            raise ValueError("No voltage source in circuit")

        Vs = float(self.circuit.vsource.v)

        # 2) Get the (only) series resistor Rab
        if len(self.circuit.resistors) != 1:
            raise ValueError("This solver expects exactly 1 series resistor (Rab).")

        series_r = next(iter(self.circuit.resistors.values()))
        Rab = float(series_r.r)

        # 3) Get the (only) load Lb (constant impedance)
        if len(self.circuit.loads) != 1:
            raise ValueError("This solver expects exactly 1 load (Lb).")

        load = next(iter(self.circuit.loads.values()))

        # Ensure load conductance/resistance is computed (from p and v)
        load.calc_g()
        Rload = float(load.r)

        # 4) Series circuit: R_total = Rab + Rload
        Rtotal = Rab + Rload
        if Rtotal == 0:
            raise ValueError("Total resistance is zero")

        I = Vs / Rtotal
        self.circuit.set_i(I)

        # 5) Bus voltages:
        # Bus A already set to Vs when vsource was added (Circuit.add_vsource_element)
        # Bus B is the node after Rab, so VB = VA - I*Rab
        VA = self.circuit.buses[self.circuit.vsource.bus1].v
        VB = VA - I * Rab

        # Update bus B voltage (the bus on the other side of Rab)
        # In this simple circuit, Rab connects A <-> B, so pick the bus that is not A.
        if series_r.bus1 == self.circuit.vsource.bus1:
            bus_b_name = series_r.bus2
        else:
            bus_b_name = series_r.bus1

        self.circuit.buses[bus_b_name].set_bus_v(VB)