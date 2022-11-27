import random
from random import choice

f={
    "Laurinska":    "CH3-(CH2)10-COOH",
    "Miristinska": "CH3-(CH2)12-COOH",
    "Palmitinska":  "CH3-(CH2)14-COOH",
    "Stearinska":   "CH3-(CH2)16-COOH",
    
    "Oleinska":     "CH3-(CH2)7=CH(CH2)7-COOH",
    "Palmitoleinska":   "CH3-(CH2)4=CH-(CH2)7-COOH",
    "Linolna":  "CH3-(CH2)4-CH=CH-CH2-CH=CH-(CH2)7-COOH",
    "Linolenska":   "CH3-CH2-CH=CH-CH2-CH=CH-CH2-CH=CH(CH2)7-COOH"
}
key,value=choice(list(f.items()))
print(value)

z=input("Koja je ovo? ")
if z==key:
    print("Tačno")
else:
    print("Nije tačno")
    print("Tačan odgovor je ", key)