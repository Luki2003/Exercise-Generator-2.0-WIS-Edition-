import os
import random
from externalFunctions import *

def aufgabentyp4():
    tasks = []
    aufgabenstellungen = []
    with open("src/Aufgabentyp 4 - (Bestimmen von häufbaren und stetigen Merkmalen).txt", "r", encoding="utf-8") as file:
        for line in file:
            tasks.append(line)

    
    randVal = random.randint(0, len(tasks)-1)
    task, solution = tasks[randVal].split(" | ")

    while True:
        os.system("cls")
        print_start()
        print("")
        print(mJust("Aufgaben-Typ 4"))
        print("")
        print(mJust("Geben Sie an, ob das folgende Merkmal stetig oder diskret ist:"))
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
        print(mJust("Aufgaben-Typ 4"))
        print("")
        print(mJust("Geben Sie an, ob das folgende Merkmal stetig oder diskret ist:"))
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