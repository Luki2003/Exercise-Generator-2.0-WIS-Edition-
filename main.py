import os
import shutil
import random
import tabulate
import collections
import numpy
import statistics

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

def aufgabentyp5():
    tasks = []
    aufgabenstellungen = []
    with open("src/Aufgabentyp 5 - (Bestimmen der Messskala von Merkmalen).txt", "r", encoding="utf-8") as file:
        for line in file:
            tasks.append(line)

    
    randVal = random.randint(0, len(tasks)-1)
    task, solution = tasks[randVal].split(" | ")

    while True:
        os.system("cls")
        print_start()
        print("")
        print(mJust("Aufgaben-Typ 5"))
        print("")
        print(mJust("Geben Sie die Messskala für das folgende Merkmal an:"))
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
        print(mJust("Aufgaben-Typ 5"))
        print("")
        print(mJust("Geben Sie die Messskala für das folgende Merkmal an:"))
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

def aufgabentyp6():
    values = [random.randint(0, 9) for i in range(0, 50)]

    opt1 = ["absolute", "relative"]
    opt2 = ["Häufigkeitverteilung", "Summenhäufigkeitsverteilung", "Resthäufigkeitsverteilung"]

    randInt1 = random.randint(0, 2)
    randInt2 = random.randint(0, 1)

    while True:    
        os.system("cls")
        print_start()
        print("")
        print(mJust("Aufgaben-Typ 6"))
        print("")
        print(mJust("Bestimmen sie die " + opt1[randInt2] + " " + opt2[randInt1] + ":"))
        print("")
        print(mJust(", ".join(map(str, values[:10])) + ","))
        print(mJust(", ".join(map(str, values[10:20])) + ","))
        print(mJust(", ".join(map(str, values[20:30])) + ","))
        print(mJust(", ".join(map(str, values[30:40])) + ","))
        print(mJust(", ".join(map(str, values[40:])) + " "))
        print("")
        print_end()
        out = input("> ")

        if out.upper() == "E":
            exit()
        elif out == "":
            break

    match randInt1:
        case 0:
            if randInt2 == 0:
                freq_vals = collections.Counter(values)
                sorted_vals = sorted(freq_vals.items())
                vals = ["a"]
                counts = ["h(a)"]

                for val, count in sorted_vals:
                    vals.append(val)
                    counts.append(count)

                tabl = tabulate.tabulate([vals, counts], tablefmt="fancy_grid", stralign="center", numalign="center")
                table_width = len(tabl.split("\n")[0])
                breite, hoehe = shutil.get_terminal_size()
                padding = " " * ((breite - table_width) // 2)
                tabl_list = tabl.split("\n")
            else:
                freq_vals = collections.Counter(values)
                sorted_vals = sorted(freq_vals.items())
                vals = ["a"]
                counts = ["f(a)"]

                for val, count in sorted_vals:
                    vals.append(val)
                    counts.append(count)

                n = len(counts)

                for i in range(1, n):
                    counts[i] = round(counts[i] / n, 2)

                tabl = tabulate.tabulate([vals, counts], tablefmt="fancy_grid", stralign="center", numalign="center")
                table_width = len(tabl.split("\n")[0])
                breite, hoehe = shutil.get_terminal_size()
                padding = " " * ((breite - table_width) // 2)
                tabl_list = tabl.split("\n")

        case 1:
            if randInt2 == 0:
                freq_vals = collections.Counter(values)
                sorted_vals = sorted(freq_vals.items())
                abs_cumulative_freq = numpy.cumsum([count for value, count in sorted_vals])
                vals = [value for value, count in sorted_vals]
                sum_counts = [abs_cumulative_freq[value-1] for value, count in sorted_vals]
                vals.insert(0, "a")
                sum_counts.insert(0, "H(a)")
                tabl = tabulate.tabulate([vals, sum_counts], tablefmt="fancy_grid", stralign="center", numalign="center")
                table_width = len(tabl.split("\n")[0])
                breite, hoehe = shutil.get_terminal_size()
                padding = " " * ((breite - table_width) // 2)
                tabl_list = tabl.split("\n")
            else:
                freq_vals = collections.Counter(values)
                sorted_vals = sorted(freq_vals.items())
                abs_cumulative_freq = numpy.cumsum([count for value, count in sorted_vals])
                vals = [value for value, count in sorted_vals]
                sum_counts = [abs_cumulative_freq[value-1] for value, count in sorted_vals]
                vals.insert(0, "a")
                sum_counts.insert(0, "F(a)")
                n = len(sum_counts)
                for i in range(1, n):
                    sum_counts[i] = round(sum_counts[i] / n, 2)
                tabl = tabulate.tabulate([vals, sum_counts], tablefmt="fancy_grid", stralign="center", numalign="center")
                table_width = len(tabl.split("\n")[0])
                breite, hoehe = shutil.get_terminal_size()
                padding = " " * ((breite - table_width) // 2)
                tabl_list = tabl.split("\n")

        case 2:
            if randInt2 == 0:
                freq_vals = collections.Counter(values)
                sorted_vals = sorted(freq_vals.items())
                abs_cumulative_freq = numpy.cumsum([count for value, count in sorted_vals])
                vals = [value for value, count in sorted_vals]
                rest_counts = [abs_cumulative_freq[-1] - abs_cumulative_freq[value-1] for value, count in sorted_vals]
                vals.insert(0, "a")
                rest_counts.insert(0, "HR(a)")
                tabl = tabulate.tabulate([vals, rest_counts], tablefmt="fancy_grid", stralign="center", numalign="center")
                table_width = len(tabl.split("\n")[0])
                breite, hoehe = shutil.get_terminal_size()
                padding = " " * ((breite - table_width) // 2)
                tabl_list = tabl.split("\n")
            else:
                freq_vals = collections.Counter(values)
                sorted_vals = sorted(freq_vals.items())
                abs_cumulative_freq = numpy.cumsum([count for value, count in sorted_vals])
                vals = [value for value, count in sorted_vals]
                rest_counts = [abs_cumulative_freq[-1] - abs_cumulative_freq[value-1] for value, count in sorted_vals]
                vals.insert(0, "a")
                rest_counts.insert(0, "FR(a)")
                n = len(rest_counts)
                for i in range(1, n):
                    rest_counts[i] = round(rest_counts[i] / n, 2)
                tabl = tabulate.tabulate([vals, rest_counts], tablefmt="fancy_grid", stralign="center", numalign="center")
                table_width = len(tabl.split("\n")[0])
                breite, hoehe = shutil.get_terminal_size()
                padding = " " * ((breite - table_width) // 2)
                tabl_list = tabl.split("\n")


    while True:
        os.system("cls")
        print_start()
        print("")
        print(mJust("Aufgaben-Typ 6"))
        print("")
        print(mJust("Bestimmen sie die " + opt1[randInt2] + " " + opt2[randInt1] + ":"))
        print("")
        print(mJust(", ".join(map(str, values[:10])) + ","))
        print(mJust(", ".join(map(str, values[10:20])) + ","))
        print(mJust(", ".join(map(str, values[20:30])) + ","))
        print(mJust(", ".join(map(str, values[30:40])) + ","))
        print(mJust(", ".join(map(str, values[40:])) + " "))
        print("")
        print("")
        print(mJust("Lösung:"))
        print("")
        for line in tabl_list:
            print(padding + line)
        print("")
        print_end()
        out = input("> ")

        if out.upper() == "E":
            exit()
        elif out == "":
            break

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

def aufgabentyp9():
    opt = random.randint(0,2)

    while True:    
        os.system("cls")
        print_start()
        print("")
        print(mJust("Aufgaben-Typ 9"))
        print("")
        print(mJust("Bestimmen sie das arithmetische Mittel:"))
        print("")
        if opt == 0:
            values = [random.randint(0, 50) for i in range(0, 15)]
            print(mJust(", ".join(map(str, values))))
        elif opt == 1:
            values1 = [i for i in range(0, 9)]
            values2 = [random.randint(0, 20) for i in range(0, 9)]
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
            values1 = [i for i in range(0, 9)]
            values2 = [random.randint(0, 20) for i in range(0, 9)]
            for i in range(0, len(values2)):
                values2[i] = round(values2[i] / len(values2), 2)
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
        arithmetic = round(statistics.mean(values), 2)
    elif opt == 1:
        arithmetic = round(sum([values1[i] * values2[i] for i in range(1, len(values2))]) / n, 2)
    else:
        arithmetic = round(sum([values1[i] * values2[i] for i in range(1, len(values2))]), 2)

    while True:    
        os.system("cls")
        print_start()
        print("")
        print(mJust("Aufgaben-Typ 9"))
        print("")
        print(mJust("Bestimmen sie das arithmetische Mittel:"))
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
        print(mJust(str(arithmetic)))
        print("")
        print_end()
        out = input("> ")

        if out.upper() == "E":
            exit()
        elif out == "":
            break

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
            values1 = [i for i in range(1, 9)]
            values2 = [random.randint(1, 9) for i in range(0, 8)]
            for i in range(0, len(values2)):
                values2[i] = round(values2[i] / len(values2), 2)
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

if __name__ == "__main__":
    aufgaben = []
    with open("settings.txt", "r", encoding="utf-8") as file:
        for line in file:
            aufgaben.append(line.strip())

    while True:
        val = random.randint(0, len(aufgaben)-1)

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
            