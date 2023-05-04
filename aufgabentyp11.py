import os
import random
import tabulate
import shutil
import statistics
from externalFunctions import *

def aufgabentyp11():
    opt = random.randint(0,2)
    opt = 2

    while True:    
        os.system("cls")
        print_start()
        print("")
        print(mJust("Aufgaben-Typ 11"))
        print("")
        print(mJust("Bestimmen sie die mittlere absolute Abweichung:"))
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
            values2 = [0.2, 0, 0.1, 0.1, 0.6]
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
        median = statistics.median(values)
        mean_abs_deviation = round(sum(abs(x - median) for x in values) / len(values), 2)
    elif opt == 1:
        del values1[0]
        del values2[0]
        temp = []
        for i in range(1, len(values2)):
            for j in range(1, values2[i]):
                temp.append(values1[i])
        median = statistics.median(temp)        
        mean_abs_deviation = round(sum(abs(values1[i] - median) * values2[i] for i in range(0, len(values2))) / n, 2)
    else:
        del values1[0]
        del values2[0]
        temp = 0
        median = 0
        for i in range(1, len(values2)):
            temp += values2[i]
            if temp >= 0.5:
                median = values1[i]
                break      
        mean_abs_deviation = round(sum(abs(values1[i] - median) * values2[i] for i in range(0, len(values2))), 2)

    while True:    
        os.system("cls")
        print_start()
        print("")
        print(mJust("Aufgaben-Typ 11"))
        print("")
        print(mJust("Bestimmen sie die mittlere absolute Abweichung:"))
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
        print(mJust(str(mean_abs_deviation)))
        print("")
        print_end()
        out = input("> ")

        if out.upper() == "E":
            exit()
        elif out == "":
            break