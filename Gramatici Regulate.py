def backtracking(Stare, nr):
    for i in range(len(Tranzitii)):             # parcurg lista de tranzitii
        if Stare == Tranzitii[i][0]:
            if Tranzitii[i][1] != '#':
                aux[nr] = Tranzitii[i][1]       # incep sa construiesc cuvantul intr-o lista auxiliara
                if len(Tranzitii[i]) == 2:      # deci este o "tranzitie terminala"
                    if nr == n:
                        for x in aux:
                            if x.isalpha():
                                Solutii.append(x)           # adaug cuvantul format in aux in lista de solutii
                        Solutii.append('')            # delimitez cuvintele din lista
                elif nr == n:               # daca nu este "tranzitie terminala" dar cuvantul pe care il formez are lungime maxima
                    for x in Tranzitii:
                        if x[0] == Tranzitii[i][2]:    # verific in tranzitii daca starea urmatoare in care pot merge contine lambda
                            if x[1] == '#':            # caz in care cuvantul format devine solutie
                                for y in aux:
                                    if y.isalpha():
                                        Solutii.append(y)
                                Solutii.append('')
                elif nr < n:
                    backtracking(Tranzitii[i][2], nr + 1)    # apelez recursiv functia

def afisare(L):          # functie de afisare a cuvintelor din lista de solutii
    i = 0
    cuvant = ""
    while i < len(L):
        if L[i] != '':
            cuvant+=L[i]
        else:
            if cuvant != '':
                print(cuvant)
                cuvant = ''
        i+=1

n = int(input(" n = "))
f = open("datein.txt")
Tranzitii = []
for x in f:
    t = x.split()
    if len(t) == 2:
        Tranzitii.append([t[0], t[1]])
    else:
        Tranzitii.append([t[0], t[1], t[2]])
aux = []
for i in range(n+2):
    aux.append('')
Solutii = []
backtracking('S', 1)
afisare(Solutii)
