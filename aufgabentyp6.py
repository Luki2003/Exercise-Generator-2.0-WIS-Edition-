import os
import random
import tabulate
import collections
import numpy
from externalFunctions import *

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