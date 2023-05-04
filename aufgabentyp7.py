import os
import random
import statistics
from externalFunctions import *

def aufgabentyp7():
    randInt = random.randint(0,1)

    if randInt == 0:
        values = [random.randint(0,50) for i in range(0, 9)]
    else:
        values = [random.randint(0,50) for i in range(0, 10)]

    while True:    
        os.system("cls")
        print_start()
        print("")
        print(mJust("Aufgaben-Typ 7"))
        print("")
        print(mJust("Bestimmen sie den Median:"))
        print("")
        print(mJust(", ".join(map(str, values))))
        print("")
        print_end()
        out = input("> ")

        if out.upper() == "E":
            exit()
        elif out == "":
            break

    median = statistics.median(values)

    if (median % 1) == 0:
        median = int(median)

    while True:    
        os.system("cls")
        print_start()
        print("")
        print(mJust("Aufgaben-Typ 7"))
        print("")
        print(mJust("Bestimmen sie den Median:"))
        print("")
        print(mJust(", ".join(map(str, values))))
        print("")
        print("")
        print(mJust("Lösung:"))
        print("")
        print(mJust(str(median)))
        print("")
        print_end()
        out = input("> ")

        if out.upper() == "E":
            exit()
        elif out == "":
            break