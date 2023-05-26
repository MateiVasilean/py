spectacole = []

def citeste_fisier(nume_fisier):
    with open(nume_fisier) as f:
        for line in f:
            start_hour, start_minute, end_hour, end_minute = map(int, line.strip().split())
            start = start_hour * 60 + start_minute
            end = end_hour * 60 + end_minute
            spectacole.append((start, end))

def citeste_tastatura():
    n = int(input("Introduceti numarul de spectacole noi: "))
    for i in range(n):
        start_hour, start_minute, end_hour, end_minute = map(int, input(f"Introduceti intervalul de timp pentru spectacolul {i+1}: ").strip().split())
        start = start_hour * 60 + start_minute
        end = end_hour * 60 + end_minute
        spectacole.append((start, end))

def afiseaza_spectacole():
    print("Spectacole:")
    for i, (start, end) in enumerate(spectacole):
        print(f"{i+1}. {int(start/60)}:{(start%60)} - {int(end/60)}:{(end%60)}")

def sortare_spectacole():
    spectacole.sort(key=lambda x: x[1])

def rezolvare_problema():
    sortare_spectacole()
    program = []
    end_time = 0
    for start, end in spectacole:
        if start >= end_time:
            program.append((start, end))
            end_time = end
    print("Orarul selectat:")
    for i, (start, end) in enumerate(program):
        print(f"{i+1}. {int(start/60)}:{(start%60)} - {int(end/60)}:{(end%60)}")

def info_autor():
    print("Autor: Matei Vasilean")

print("\nMENIU")
print("CF. Citire date din fișier")
print("CT. Citire date de la tastatura")
print("A. Afișare date")
print("AS. Afisare date sortate")
print("R. Rezolvare problema")
print("I. Info autor")
print("X. Termina programul")

while True:
    optiune = input("Introduceti optiunea: ")
    if optiune == "CF":
        nume_fisier = input("Introduceti numele fisierului: ")
        citeste_fisier(nume_fisier)
    elif optiune == "CT":
        citeste_tastatura()
    elif optiune == "A":
        afiseaza_spectacole()
    elif optiune == "AS":
        sortare_spectacole()
        afiseaza_spectacole()
    elif optiune == "R":
        rezolvare_problema()
    elif optiune == "I":
        info_autor()
    elif optiune == "X":
        break

print(f"")