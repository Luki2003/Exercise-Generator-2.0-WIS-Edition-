import os
import random
from externalFunctions import *

def aufgabentyp1():
    tasks = []
    aufgabenstellungen = []
    with open("src/Aufgabentyp 1 - (Bestimmen von Merkmalsträger, Merkmal & Merkmalsausprägung).txt", "r", encoding="utf-8") as file:
        for line in file:
            tasks.append(line)

    randVal = random.randint(0, len(tasks)-1)
    task, solution = tasks[randVal].split(" | ")

    while True:
        os.system("cls")
        print_start()
        print("")
        print(mJust("Aufgaben-Typ 1"))
        print("")
        print(mJust("Geben Sie für die folgenden Fragestellungen Merkmalsträger, Merkmal und eine Merkmalsausprägung an:"))
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
        print(mJust("Aufgaben-Typ 1"))
        print("")
        print(mJust("Geben Sie für die folgenden Fragestellungen Merkmalsträger, Merkmal und eine Merkmalsausprägung an:"))
        print("")
        print(mJust(task))
        print("")
        print("")
        print(mJust("Lösung:"))
        print("")
        print(mJust("Merkmalsträger: " + solution.split(", ")[0]))
        print(mJust("Merkmal: " + solution.split(", ")[1]))
        print(mJust("Merkmalsausprägung: " + solution.split(", ")[2]))
        print("")
        print_end()
        out = input("> ")

        if out.upper() == "E":
            exit()
        elif out == "":
            break