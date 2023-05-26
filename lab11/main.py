from ex1.module1 import Module1
from ex2.module2 import Module2
from ex3.module3 import Module3
from ex4.module4 import Module4
import os

def clear_screen():
    os.system('clear')

def problem(module_instance, condition, data_file_path):
    print(f"Conditia problemei este:\n{condition}")
    input()
    clear_screen()

    print("Datele aflate in fisier sunt:")
    with open(data_file_path) as f:
        data = f.read()
    print(data)
    input()
    clear_screen()

    print("Rezolvarea problemei:")

    if isinstance(module_instance, Module1):
        n, concurente = module_instance.read_file(data_file_path)
        module_instance.MasaRotunda(n, concurente)
    elif isinstance(module_instance, Module2):
        graph, start_city, end_city = module_instance.read_file(data_file_path)
        result = module_instance.find_paths(graph, start_city, end_city)
        module_instance.print_paths(result)
    elif isinstance(module_instance, Module3):
        dictionaries = module_instance.read_file(data_file_path)
        source_lang = input("Introduceti limba sursa: ")
        target_lang = input("Introduceti limba tinta: ")
        module_instance.solve_translation_problem(dictionaries, source_lang, target_lang)
    elif isinstance(module_instance, Module4):
        hill = module_instance.read_file(data_file_path)
        print("Toate drumurile pe care mingea poate cobori:")
    input()

while True:
    clear_screen()
    print("Laboratorul 11")
    print("--------------")
    print("1. Problema 1")
    print("2. Problema 2")
    print("3. Problema 3")
    print("4. Problema 4")
    print("5. Termina programul")
    print("--------------")
    optiune = input("Introduceti optiunea: ")
    clear_screen()

    if optiune == "1":
        from ex1.module1 import Module1
        module_instance = Module1()
        problem(module_instance, module_instance.condition, 'ex1/data_file1.txt')
    elif optiune == "2":
        from ex2.module2 import Module2
        module_instance = Module2()
        problem(module_instance, module_instance.condition, 'ex2/data_file2.txt')
    elif optiune == "3":
        from ex3.module3 import Module3
        module_instance = Module3()
        problem(module_instance, module_instance.condition, 'ex3/data_file3.txt')
    elif optiune == "4":
        from ex4.module4 import Module4
        module_instance = Module4()
        problem(module_instance, module_instance.condition, 'ex4/data_file4.txt')
    elif optiune == "5":
        break