import os
import random
import numpy
from externalFunctions import *

def aufgabentyp8():
    randInt = random.randint(0,1)
    randQuant = round(random.random(), 2)

    if randInt == 0:
        values = [random.randint(0,50) for i in range(0, 9)]
    else:
        values = [random.randint(0,50) for i in range(0, 10)]

    while True:    
        os.system("cls")
        print_start()
        print("")
        print(mJust("Aufgaben-Typ 8"))
        print("")
        print(mJust("Bestimmen sie das " + str(int(randQuant*100)) + "er Quantil:"))
        print("")
        print(mJust(", ".join(map(str, values))))
        print("")
        print_end()
        out = input("> ")

        if out.upper() == "E":
            exit()
        elif out == "":
            break

    quantil = round(numpy.quantile(values, randQuant),2)

    if (quantil % 1) == 0:
        quantil = int(quantil)

    while True:    
        os.system("cls")
        print_start()
        print("")
        print(mJust("Aufgaben-Typ 8"))
        print("")
        print(mJust("Bestimmen sie das " + str(int(randQuant*100)) + "er Quantil:"))
        print("")
        print(mJust(", ".join(map(str, values))))
        print("")
        print("")
        print(mJust("Lösung:"))
        print("")
        print(mJust(str(quantil)))
        print("")
        print_end()
        out = input("> ")

        if out.upper() == "E":
            exit()
        elif out == "":
            break