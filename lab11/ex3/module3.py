class Module3:
    def __init__(self):
        self.condition = """Un student la filologie poseda n dicţionare bilingve care permit traducerea dintr-o limba i intr-o limba j cu 1<=i, 
j<=n. Sa se determine toate seturile de dicţionare care îi permit studentului să realizeze o traducere între limba s şi limba d."""

    def find_translation_sets(self, dictionaries, s, d):
        translation_sets = []
        current_set = []

        def backtrack(index):
            nonlocal current_set

            if index == len(dictionaries):
                if current_set and current_set[0][0] == s and current_set[-1][1] == d:
                    translation_sets.append(list(current_set))
                return

            current_set.append(dictionaries[index])
            if len(current_set) == 1 or current_set[-1][0] == current_set[-2][1]:
                backtrack(index + 1)
            current_set.pop()
            backtrack(index + 1)

        backtrack(0)
        return translation_sets

    def read_file(self, data_file_path):
        dictionaries = []

        with open(data_file_path) as f:
            num_dictionaries = int(f.readline().strip())

            for _ in range(num_dictionaries):
                line = f.readline().strip()
                source, destination = line.split()
                dictionaries.append((source, destination))

        return dictionaries

    def solve_translation_problem(self, dictionaries, source_language, destination_language):
        sets = self.find_translation_sets(dictionaries, source_language, destination_language)
        if sets:
            print(f"Toate seturile de dictionare care permit traducerea de la {source_language} la {destination_language}:")
            for translation_set in sets:
                print(translation_set)
        else:
            print("Nu exista un set de dictionare care să permita traducerea specificata.")