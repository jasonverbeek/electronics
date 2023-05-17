"""(InputVoltage - OutputVoltage) / Amps
Conjecture:
    ExcessVoltage = InputVoltage - OutputVoltage
    OhmsRequired = ExcessVoltage / Amps(needed for component(s))"""
iV = float(input("Input Voltage: "))
oV = float(input("Required/Output Voltage: "))
A = float(input("Amps(1000mA) required: "))
R1 = (iV - oV) / A
print("Resistor needed(Ohms):", R1)
