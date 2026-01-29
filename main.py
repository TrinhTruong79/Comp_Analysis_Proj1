from Bus import Bus
from Circuit import Circuit
from Solution import Solution


def main():
    # 1. Define the circuit
    circuit = Circuit("Simple DC Circuit")

    # a. Add buses A and B
    circuit.add_bus(Bus("A"))
    circuit.add_bus(Bus("B"))

    # b. Voltage source Va connected at bus A with 100 V
    circuit.add_vsource_element("Va", "A", 100.0)

    # c. Resistor Rab connected between buses A and B with 5 Ohms
    circuit.add_resistor_element("Rab", "A", "B", 5.0)

    # d. Load Lb connected to bus B
    #    Power = 2000 W, nominal voltage = 100 V
    circuit.add_load_element("Lb", "B", 2000.0, 100.0)

    # 2. Create solution object and simulate the circuit
    solution = Solution(circuit)
    solution.do_power_flow()

    # 3. Display results
    circuit.print_nodal_voltage()
    circuit.print_circuit_current()


if __name__ == "__main__":
    main()