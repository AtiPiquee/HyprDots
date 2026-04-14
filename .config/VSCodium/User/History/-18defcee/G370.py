#!/bin/python3

import math

from args import parser_args

# constantes

h = 6.62607015e-34
c = 299792458
cc = c * c
phi = (1 + math.sqrt(5)) / 2
Na = 6.00214076e23
pi = math.pi

# Ma = Inconnue introduit dans la fonction qui sera chiffrée

def text_to_ascii(text):
    chars = []

    for char in text:
        r.append(ord(char))

    result = ''.join(chars)

    return result

def f(Ma) -> int:
    MaAbs = math.fabs(Ma)

    result = ((MaAbs * h)/(pi * cc)) * (math.exp(phi) / Na)
    resultAbs = math.fabs(result)

    return int(resultAbs)

def main() -> None:
    text = parser_args()
    Ma = ord(text)
    Ma = f(Ma)

    print(f"text : {text}, Ma : {Ma}")

if __name__ == "__main__":
    main()