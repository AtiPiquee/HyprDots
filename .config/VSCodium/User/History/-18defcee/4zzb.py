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
        chars.append(str(ord(char)))

    result = ''.join(chars)

    return result

def f(Ma: int) -> str:
    MaAbs = math.fabs(Ma)

    result = ((MaAbs * h)/(pi * cc)) * (math.exp(phi) / Na)
    #resultAbs = math.fabs(result)
    print(result)
    return str(result)

def main() -> None:
    text = parser_args()
    MaOrd = text_to_ascii(text)
    print(MaOrd)
    Ma = f(MaOrd)

    Ma = Ma.replace(".", "")
    Ma = Ma.replace("e", "")
    Ma = Ma.replace("-", "")

    print(f"text : {text}, Ma : {Ma}")

if __name__ == "__main__":
    main()