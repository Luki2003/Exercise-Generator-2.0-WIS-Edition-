import os
import random
from externalFunctions import *

def aufgabentyp2():
    tasks = []
    aufgabenstellungen = []
    with open("src/Aufgabentyp 2 - (Bestimmen von Ereignis- und Bestandsmassen).txt", "r", encoding="utf-8") as file:
        for line in file:
            tasks.append(line)

    
    randVal = random.randint(0, len(tasks)-1)
    task, solution = tasks[randVal].split(" | ")

    while True:
        os.system("cls")
        print_start()
        print("")
        print(mJust("Aufgaben-Typ 2"))
        print("")
        print(mJust("Geben Sie an, ob die Grundgesamtheit eine Bestands- oder Ereignismasse ist:"))
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
        print(mJust("Aufgaben-Typ 2"))
        print("")
        print(mJust("Geben Sie an, ob die Grundgesamtheit eine Bestands- oder Ereignismasse ist:"))
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