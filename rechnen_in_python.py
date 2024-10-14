#
# Addition
#
# Das komma ist zum trennen von Zahlen/Werten.
# Wenn man Flieskommazahlen bzw. Brüche schreiben möchte verwendet man einen Punkt.

x_Komma = 10+11,5
print(x_Komma)                  # Output: (21, 5)

x_Punkt = 10+11.5
print(x_Punkt)                  # Output: 21.5

x_Addition_1 = 365+4005
print(x_Addition_1)             # Output: 4370

x_Addition_2 = 365.365+4005
print(x_Addition_2)             # Output: 4370.365

x_Addition_3 = 365.365+(4005+4005.600)
print(x_Addition_3)             # Output: 8375.965

#
# Substraktion
#

x_Substraktion_1 = 365-355
print(x_Substraktion_1)         # Output: 10

x_Substraktion_2 = 365-4005
print(x_Substraktion_2)         # Output: -3640

x_Substraktion_3 = 365-(-4005-563)
print(x_Substraktion_3)         # Output: 4933

#
# Multiplikation
#

x_Multiplikation_1 = 45*134
print(x_Multiplikation_1)       # Output: 6030

x_Multiplikation_2 = 45-33*236+33
print(x_Multiplikation_2)       # Output: -7710

x_Multiplikation_3 = 45*(-46)+77
print(x_Multiplikation_3)       # Output: -1993

#
# Division
#

x_Division_1 = 55/125
print(x_Division_1)             # Output: 0.44

x_Division_2 = 55/17+987
print(x_Division_2)             # Output: 990.2352941176471

x_Division_3 = (-567)/123+76
print(x_Division_3)             # Output: 71.39024390243902

#
# Ganzzahl Division (GDivision)
#

x_GDivision_1 = 555//34
print(x_GDivision_1)            # Output: 16

x_GDivision_2 = 678+901//110
print(x_GDivision_2)            # Output: 686

x_GDivision_3 = 456//5
print(x_GDivision_3)            # Output: 91

#
# Modulo
#

x_Modulo_1 = 75%7
print(x_Modulo_1)               # Output: 5

x_Modulo_2 = 4567%123
print(x_Modulo_2)               # Output: 16

x_Modulo_3 = 67890%3
print(x_Modulo_3)               # Output: 0

#
# Potenzierung
#

x_Potenzierung_1 = 2**8
print(x_Potenzierung_1)         # Output: 256

x_Potenzierung_2 = 5**9
print(x_Potenzierung_2)         # Output: 1953125

x_Potenzierung_3 = 2**2**8
print(x_Potenzierung_3)         # Output: 115792089237316195423570985008687907853269984665640564039457584007913129639936

#
# Rechnen mit Texten - Addition
#

x_Text_Addition_1 = "Hier steht"+" ihr Text"
print(x_Text_Addition_1)        # Output: Hier steht ihr Text

x_Text_Addition_2 = "abcdefg"+"12345678"
print(x_Text_Addition_2)        # Output: abcdefg12345678

#
# Rechnen mit Texten - Multiplikation
#

x_Text_Multiplikation_1 = "abcd"*5
print(x_Text_Multiplikation_1)  # Output: abcdabcdabcdabcdabcd

x_Text_Multiplikation_2 = 3*"12345"
print(x_Text_Multiplikation_2)  # Output: 123451234512345

x_Text_Multiplikation_3 = "Text"*7
print(x_Text_Multiplikation_3)  # Output: TextTextTextTextTextTextText