# electronics

A repository with developer understandable formulas for electronics

## Calculating the required resistance in Ohms for a component

In order to do this method the `Vin`, `V`(required voltage)
and `A`(required Amps) need to be known.

$$\ohm=\frac{\left(Vin-V\right)}{A}$$

## Voltage Divider

Voltage dividers using only 2 resistors
(still need to figure out >2)

Knowing the following variables:

- Input voltage
- Needed output voltage
- Resistor 1 in $`\ohm`$

We can calculate for _Resistor 2 in_ $`\ohm`$:

$$R2\ohm=\frac{\left(V \times R1\ohm\right)}{\left(Vin - V\right)}$$

Knowing the following variables:

- Input voltage
- Needed output voltage
- Resistor 2 in $`\ohm`$

We can calculate for _Resistor 1 in_ $`\ohm`$:

$$R1\ohm=\frac{Vin \times R2\ohm}{V}-R2\ohm$$

Knowing the following variables:

- Input voltage
- Resistor 1 in $`\ohm`$
- Resistor 2 in $`\ohm`$

We can calculate for _Output voltage_:

$$V=\frac{\left(Vin \times R2\ohm\right)}{\left(R1\ohm-R2\ohm\right)}$$
