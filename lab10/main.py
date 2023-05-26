class islands:
    def __init__(self, ins1, ins2):
        self.ins1 = ins1
        self.ins2 = ins2

def read_file(filename):
    list_islands = []
    with open(filename) as f:
        n = int(f.readline())
        ins_start = int(f.readline())
        for line in f:
            ins1, ins2 = map(int, line.strip().split())
            list_islands.append(islands(ins1, ins2))
    return n, ins_start, list_islands

def print_elements(ins_start, list_islands):
    print(ins_start)
    for elements in list_islands:
        print(elements.ins1, elements.ins2)

def Plimbare(insula_crt, k):
    global n, x, list_islands
    if n == k:
        print(x)
    else:
        for i in range(n):
            if Posibil(i, k, insula_crt):
                x[k] = i
                if insula_crt == list_islands[i].ins1:
                    ins = list_islands[i].ins2
                else:
                    ins = list_islands[i].ins1
                Plimbare(ins, k + 1)

def Posibil(alfa, k, ins_crt):
    global x, list_islands
    for j in range(k):
        if x[j] == alfa:
            return False

    return list_islands[alfa].ins1 == ins_crt or list_islands[alfa].ins2 == ins_crt

filename = "/Users/matei/Documents/lab10/data.txt"
n, ins_start, list_islands = read_file(filename)
print_elements(ins_start, list_islands)
x = [0] * n
Plimbare(ins_start, 0)