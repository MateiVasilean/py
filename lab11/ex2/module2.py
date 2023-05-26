class Module2:
    def __init__(self):
        self.condition = """Între n oraşe există o reţea de şosele care unesc două oraşe între ele. Să se determine toate posibilităţile de alegere 
a şoselelor, astfel încât să se ajungă din oraşul s în oraşul d."""

    def find_paths(self, graph, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]
        if start not in graph:
            return []

        paths = []

        for city in graph[start]:
            if city not in path:
                new_paths = self.find_paths(graph, city, end, path)
                for new_path in new_paths:
                    paths.append(new_path)

        return paths

    def read_file(self, data_file_path):
        graph = {}
        start_city = None
        end_city = None

        with open(data_file_path) as f:
            num_cities = int(f.readline().strip())

            for _ in range(num_cities):
                line = f.readline().strip()
                city, *connections = line.split()
                graph[city] = connections

            start_city = f.readline().strip()
            end_city = f.readline().strip()

        return graph, start_city, end_city

    def print_paths(self, paths):
        if len(paths) > 0:
            print("Toate posibilitatile:")
            for path in paths:
                print(' - '.join(path))
        else:
            print("Nu exista o solutie valida")