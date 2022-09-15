# Switch
An algorithm to change base of any given number (N) to any specified base (B). It supports integers only for now and *upto base 85*.

<p>N<sub>B1</sub> => X<sub>B2</sub></p>

If there are non-numeric symbols involved, it also returns a dictionary to map the symbols. For example, the following symbols are used in Hexadecimal:

| Hex | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| Decimal | 10 | 11 | 12 | 13 | 14 | 15 |

```python
from switch import Switch

example = Switch()

example.toBinary(97)
example.toHexadecimal(97)
example.switch(97, 14)

# Resposes
- 1100001 # Binary
- ['61', {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}] # Hexadecimal
- ['6D', {'A': 10, 'B': 11, 'C': 12, 'D': 13}] # Base 14
```