import random
from aufgabentyp1 import *
from aufgabentyp2 import *
from aufgabentyp3 import *
from aufgabentyp4 import *
from aufgabentyp5 import *
from aufgabentyp6 import *
from aufgabentyp7 import *
from aufgabentyp8 import *
from aufgabentyp9 import *
from aufgabentyp10 import *
from aufgabentyp11 import *
from aufgabentyp12 import *
from aufgabentyp13 import *

if __name__ == "__main__":
    aufgaben = []
    with open("settings.txt", "r", encoding="utf-8") as file:
        for line in file:
            aufgaben.append(line.strip())

    while True:
        val = random.randint(0, len(aufgaben)-1)

        val = 11

        match aufgaben[val]:
            case "typ1": 
                aufgabentyp1()
            case "typ2":
                aufgabentyp2()
            case "typ3":
                aufgabentyp3()
            case "typ4":
                aufgabentyp4()
            case "typ5":
                aufgabentyp5()
            case "typ6":
                aufgabentyp6()
            case "typ7":
                aufgabentyp7()
            case "typ8":
                aufgabentyp8()
            case "typ9":
                aufgabentyp9()
            case "typ10":
                aufgabentyp10()
            case "typ11":
                aufgabentyp11()
            case "typ12":
                aufgabentyp12()
            case "typ13":
                aufgabentyp13()
            