# Aufgabe 2
#
# 2.1
#

def Aufgabe_2_1():
    aktuelles_geld = 0
    monatliches_ersparnis = 20
    monate = 0
    zinssatz = 0.10
    ziel = 1000
    while aktuelles_geld < ziel:
        aktuelles_geld += monatliches_ersparnis
        aktuelles_geld += aktuelles_geld * zinssatz
        monate += 1
    else:
        print("Es werden " + str(monate) + " Monate benötigt um " + str(aktuelles_geld) + "€ zu sparen.")

# Output: Es werden 18 Monate benötigt um 1003.1818089682909€ zu sparen.

#
# 2.2
#

def Aufgabe_2_2():
    benoetigtes_geld = 2000
    zinssatz = 0.05
    monate = 12

    print(benoetigtes_geld * (zinssatz * (1 + zinssatz) ** monate / ((1 + zinssatz) ** monate - 1)))

# Output: 225.65082004163068

#
# 2.3
#

def Aufgabe_2_3():
    global gerade_zahlen, zahlen_3_5
    gerade_zahlen = []
    zahlen_3_5 = []
    for zahl in range(0,101):
        if (zahl%2 == 0):
            gerade_zahlen.append(zahl)
        if (zahl%3 == 0 and zahl%5 == 0):
            zahlen_3_5.append(zahl)

    def Alle_Zahlen():
        print("Alle ganze zahlen von 0 bis 100: \n" + str(list(range(0, 101))))
    def Alle_Geraden_Zahlen():
        print("Alle geraden zahlen von 0 bis 100: \n"+str(gerade_zahlen))
    def Zahlen_3_5():
        print("Alle zahlen von 0 bis 100 die durch 3 und 5 teilbar sind: \n"+str(zahlen_3_5))

    def toBinary():
        number = input("Deine gewünschte zahl: (5 | 10.5) ")
        try:
            float_number = float(number)
            integer_part = int(float_number)
            fractional_part = float_number - integer_part

            binary_integer_part = bin(integer_part)[2:]

            binary_fractional_part = []
            while fractional_part:
                fractional_part *= 2
                bit = int(fractional_part)
                if bit == 1:
                    fractional_part -= bit
                    binary_fractional_part.append('1')
                else:
                    binary_fractional_part.append('0')
                if len(binary_fractional_part) > 10:
                    break

            binary_representation = binary_integer_part
            if binary_fractional_part:
                binary_representation += '.' + ''.join(binary_fractional_part)

            print(number + " in Binär ist " + binary_representation)
        except ValueError:
            print("Bitte geben Sie eine gültige Zahl ein.")

    menu_2_3 = input("Was möchen sie?"
                     "\n    1) Alle Ganzen Zahlen von 0 bis 100"
                     "\n    2) Alle Geraden Zahlen von 0 bis 100"
                     "\n    3) Alle Zahlen die durch 3 und 5 teilbar sind, von 0 bis 100"
                     "\n    4) Eine Zahl in Binär konvertieren\n")

    match menu_2_3:
        case "1":
            Alle_Zahlen()
        case "2":
            Alle_Geraden_Zahlen()
        case "3":
            Zahlen_3_5()
        case "4":
            toBinary()



aufgabe = input("Welche Aufgabe möchten Sie sehen? (2.1 | 2.2 | 2.3) ")
match aufgabe:
    case "2.1":
        Aufgabe_2_1()
    case "2.2":
        Aufgabe_2_2()
    case "2.3":
        Aufgabe_2_3()