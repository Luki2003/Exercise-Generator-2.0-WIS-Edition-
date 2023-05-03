aufgaben = []
lösungen = []
gesamt = []

with open("tempAufgaben.txt", "r", encoding="utf-8") as file:
    for line in file:
        aufgaben.append(line.strip())

with open("tempLösungen.txt", "r", encoding="utf-8") as file:
    for line in file:
        lösungen.append(line.strip())

gesamt = [aufgaben[i] + " | " + lösungen[i] + "\n" for i in range(0, len(aufgaben))]

with open("tempGesamt.txt", "w", encoding="utf-8") as file:
    file.writelines(gesamt)