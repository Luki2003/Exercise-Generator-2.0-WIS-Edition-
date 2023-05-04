import os
import random
from externalFunctions import *

def aufgabentyp3():
    tasks = []
    aufgabenstellungen = []
    with open("src/Aufgabentyp 3 - (Bestimmen von häufbaren und nicht häufbaren Merkmalen).txt", "r", encoding="utf-8") as file:
        for line in file:
            tasks.append(line)

    
    randVal = random.randint(0, len(tasks)-1)
    task, solution = tasks[randVal].split(" | ")

    while True:
        os.system("cls")
        print_start()
        print("")
        print(mJust("Aufgaben-Typ 3"))
        print("")
        print(mJust("Geben Sie an, ob das folgende Merkmal häufbar ist oder nicht:"))
        print("")
        print(mJust(task))
        print("")
        print_end()
        out = input("> ")

        if out.upper() == "E":
            exit()
        elif out == "":
            break

    while True:
        os.system("cls")
        print_start()
        print("")
        print(mJust("Aufgaben-Typ 3"))
        print("")
        print(mJust("Geben Sie an, ob das folgende Merkmal häufbar ist oder nicht:"))
        print("")
        print(mJust(task))
        print("")
        print("")
        print(mJust("Lösung:"))
        print("")
        print(mJust(solution))
        print("")
        print_end()
        out = input("> ")

        if out.upper() == "E":
            exit()
        elif out == "":
            break