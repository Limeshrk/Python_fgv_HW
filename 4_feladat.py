import math

radius = input("Kérem a kör sugarát: ")

def convert_to_number(radius):
    converted_text = int(radius)
    return converted_text

r = convert_to_number(radius)

def kor_kerulete(r):
    kerulet = 2*r*math.pi
    print(f'A kör kerülete: {kerulet}')
    return kerulet

def kor_terulete(r):
    terulet = r*r*math.pi
    print(f'A kör területe: {terulet}')
    return terulet

kor_kerulete(r)
kor_terulete(r)

