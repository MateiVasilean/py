class Module4:
    def __init__(self):
        self.condition = """Pe un deal, într-un punct oarecare, se află o minge. Să se determine toate drumurile pe care poate coborî mingea 
astfel încât să ajungă la poalele dealului."""
    
    def read_file(self, data_file_path):
        hill = []

        with open(data_file_path) as f:
            for line in f:
                row = list(map(int, line.split()))
                hill.append(row)

        return hill