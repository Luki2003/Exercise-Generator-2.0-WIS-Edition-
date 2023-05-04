import os
import random
import shutil
import tabulate
import statistics
from externalFunctions import *

def aufgabentyp10():
    opt = random.randint(0,2)

    while True:    
        os.system("cls")
        print_start()
        print("")
        print(mJust("Aufgaben-Typ 10"))
        print("")
        print(mJust("Bestimmen sie das geometrische Mittel:"))
        print("")
        if opt == 0:
            values = [random.randint(1, 20) for i in range(0, 10)]
            n = len(values)
            print(mJust(", ".join(map(str, values))))
        elif opt == 1:
            values1 = [i for i in range(1, 9)]
            values2 = [random.randint(1, 9) for i in range(0, 8)]
            n = sum(values2)
            values1.insert(0, "a")
            values2.insert(0, "h(a)")
            tabl = tabulate.tabulate([values1, values2], tablefmt="fancy_grid", stralign="center", numalign="center")
            table_width = len(tabl.split("\n")[0])
            breite, hoehe = shutil.get_terminal_size()
            padding = " " * ((breite - table_width) // 2)
            tabl_list = tabl.split("\n")
            for line in tabl_list:
                print(padding + line)
        else:
            values1 = [i for i in range(1, 6)]
            values2 = [random.randint(0, 2) for i in range(0, 4)]
            values2 = [x / 10 for x in values2]
            temp = 1 - sum(values2[0:])
            values2.append(temp)
            values1.insert(0, "a")
            values2.insert(0, "f(a)")
            tabl = tabulate.tabulate([values1, values2], tablefmt="fancy_grid", stralign="center", numalign="center")
            table_width = len(tabl.split("\n")[0])
            breite, hoehe = shutil.get_terminal_size()
            padding = " " * ((breite - table_width) // 2)
            tabl_list = tabl.split("\n")
            for line in tabl_list:
                print(padding + line)
        print("")
        print_end()
        out = input("> ")

        if out.upper() == "E":
            exit()
        elif out == "":
            break

    if opt == 0:
        geometric = round(statistics.geometric_mean(values), 2)
    elif opt == 1:
        geometric = round(prod([(values1[i] ** values2[i]) for i in range(1, 9)]) ** (1/n), 2)
    else:
        geometric = round(prod([values1[i] ** values2[i] for i in range(1, len(values2))]), 2)

    while True:    
        os.system("cls")
        print_start()
        print("")
        print(mJust("Aufgaben-Typ 10"))
        print("")
        print(mJust("Bestimmen sie das geometrische Mittel:"))
        print("")
        if opt == 0:
            print(mJust(", ".join(map(str, values))))
        elif opt == 1:
            for line in tabl_list:
                print(padding + line)
        else:
            for line in tabl_list:
                print(padding + line)
        print("")
        print("")
        print(mJust("Lösung:"))
        print("")
        print(mJust(str(geometric)))
        print("")
        print_end()
        out = input("> ")

        if out.upper() == "E":
            exit()
        elif out == "":
            break