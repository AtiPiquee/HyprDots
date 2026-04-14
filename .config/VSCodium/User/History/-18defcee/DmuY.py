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

def ascii_to_text(ascii_suite: int) -> str:
    text = []

    ascstr = str(ascii_suite)

    for asc in ascstr:
        text.append(chr(int(asc)))

    for t in text:
        t = t.replace("\\", "")
        t = t.replace("x", "")

    print(text)
    result = ''.join(text)

    return result

def f(Ma: int) -> str:
    MaAbs = math.fabs(Ma)

    result = ((MaAbs * h)/(pi * cc)) * (math.exp(phi) / Na)
    
    return str(result)

def main() -> None:
    text = parser_args()
    MaOrd = text_to_ascii(text)
    Ma = f(int(MaOrd))

    Ma = Ma.replace(".", "")
    Ma = Ma.replace("e", "")
    Ma = Ma.replace("-", "")

    Ma = ascii_to_text(int(Ma))

    print(f"text : {text}, Ma : {Ma}")

if __name__ == "__main__":
    main()