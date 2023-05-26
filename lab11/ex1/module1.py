class Module1:
    def __init__(self):
        self.condition = """Între n oraşe există o reţea de şosele care unesc două oraşe între ele. Să se determine toate posibilităţile de alegere 
a şoselelor, astfel încât să se ajungă din oraşul s în oraşul d."""

    def Posibil(self, i, k, mr, concurente):
        if k > 0 and concurente[mr[k-1]][i] != 0:
            return False
        if k == len(mr) - 1 and concurente[mr[0]][i] != 0:
            return False
        return True

    def afisSolutie(self, mr, nsol):
        nsol[0] += 1
        print("Varianta {} de asezare la masa rotunda:".format(nsol[0]), *map(str, mr))

    def MasaRotunda(self, n, concurente):
        asezat = [False] * n
        mr = [None] * n
        nsol = [0]

        def backtrack(k):
            if k >= n:
                self.afisSolutie(mr, nsol)
            else:
                for i in range(n):
                    if not asezat[i] and self.Posibil(i, k, mr, concurente):
                        asezat[i] = True
                        mr[k] = i
                        backtrack(k + 1)
                        asezat[i] = False

        backtrack(0)

        if nsol[0] == 0:
            print("Nu exista solutii")

    def read_file(self, filename):
        with open(filename) as f:
            n = int(f.readline())
            concurente = [[0] * n for _ in range(n)]
            
            counter = 0
            for line in f:
                row = list(map(int, line.split()))
                for elements in row:
                    if elements != 0:
                        concurente[counter][elements - 1] = 1
                        concurente[elements - 1][counter] = 1
                counter += 1

        return n, concurente