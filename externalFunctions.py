import shutil

def print_start():
    breite, hoehe = shutil.get_terminal_size()
    part1 = "Exercise Generator 2.0 (WIS Edition)"
    part2 = "(Beenden mit 'e' |  Weiter mit 'Enter')"
    rest = breite - len(part1) - len(part2)

    if rest <= 0:
        print(part1)
        temp = ""
        for i in range(0, breite):
            temp += "-"
        print(temp)
    else:
        for i in range(0, rest):
            part1 += " "
        part1 += part2
        print(part1)
        temp = ""
        for i in range(0, breite):
            temp += "-"
        print(temp)

def print_end():
    breite, hoehe = shutil.get_terminal_size()
    temp = ""
    for i in range(0, breite):
        temp += "-"
    print(temp)

def prod(x:list):
    temp = 1
    for element in x:
        temp *= element
    return temp

def mJust(text:str):
    breite, hoehe = shutil.get_terminal_size()
    if len(text) < breite:
        leerzeichen = (breite - len(text)) // 2
        temp = ""
        for i in range(0, leerzeichen):
            temp += " "
        temp += text
        return temp
    else:
        pos = 0
        counter = breite-1
        while True:
            if text[counter] == " ":
                pos = counter
                break

            else:
                counter -= 1

        part1 = text[:pos]
        part2 = text[pos+1:]
        leerzeichen1 = (breite - len(part1)) // 2
        leerzeichen2 = (breite - len(part2)) // 2
        temp1 = ""
        temp2 = ""
        for i in range(0, leerzeichen1):
            temp1 += " "
        for i in range(0, leerzeichen2):
            temp2 += " "
        temp1 += part1
        temp2 += part2
        tempGes = temp1 + "\n" + temp2
        return tempGes