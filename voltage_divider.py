# InputVoltage, Resistor1, Resistor2 are known
print("1) calculate oV using iV+R1+R2")
# InputVoltage, OutputVoltage, Resistor1 are known
print("2) calculate R2 using iV+oV+R1")
# InputVoltage, OutputVoltage, Resistor2 are known
print("3) calculate R1 using iV+oV+R2")

mode = input("Choose mode: ")


def calc_oV():
    """Calculate OutputVoltage
    (InputVoltage * Resistor2) / (Resistor1 - Resistor2)"""
    iV = float(input("Input Voltage: "))
    R1 = float(input("Resistor 1 (Ohm): "))
    R2 = float(input("Resistor 2 (Ohm): "))
    oV = (iV * R2) / (R1 + R2)
    print("Output voltage between resistors:", oV)


def calc_R2():
    """Calculate Resistor 2
    (OutputVoltage * Resistor1) / (InputVoltage - OutputVoltage)"""
    iV = float(input("Input Voltage: "))
    R1 = float(input("Resistor 1 (Ohm): "))
    oV = float(input("Output Voltage: "))
    R2 = (oV * R1) / (iV - oV)
    print("Resistor 2 should be", R2, "Ohm")


def calc_R1():
    """Calculate Resistor 1
    (InputVoltage * Resistor2 / OutputVoltage) - Resistor2"""
    iV = float(input("Input Voltage: "))
    R2 = float(input("Resistor 2 (Ohm): "))
    oV = float(input("Output Voltage: "))
    R1 = (iV * R2 / oV) - R2
    print("Resistor 1 should be", R1, "Ohm")


def invalid_mode():
    """Invalid mode has been selected, error will be thrown"""
    print("Invalid mode")
    exit(1)


# run mode or give an error if input is invalid
{
    "1": calc_oV,
    "2": calc_R2,
    "3": calc_R1,
}.get(mode, invalid_mode)()
