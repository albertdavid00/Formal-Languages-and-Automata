'''
input:
stari finale
nr_stari
nr_tranzitii
tranzitii
'''

cuvant = input()
f = open("intrare.txt")

L_stari_fin = [int(x) for x in f.readline().split()]
if (cuvant == '#' or cuvant == '') and 0 in L_stari_fin:
    print("Cuvantul apartine limbajului recunoscut de automat")
else:
    nr_stari = int(f.readline())
    L_stari = []
    for i in range(0, nr_stari):
        L_stari.append(i)

    nr_tranzitii = int(f.readline())
    L_tranzitii = []

    for i in range(nr_tranzitii):
        t = f.readline().split()
        t[0], t[1] = int(t[0]), int(t[1])
        L_tranzitii.append(tuple(t))

    y = L_tranzitii[0][0]
    Tranzitii = []
    # lista de liste de tuple-uri in care retinem pentru fiecare stare in ce stari se duce si cu ce litere
    Lista = []
    for x in L_tranzitii:
        if x[0] != y:
            Tranzitii.append(Lista)
            Lista = []
            y = x[0]
            Lista.append(tuple((x[1], x[2],x[3],x[4])))
        else:
            Lista.append(tuple((x[1], x[2],x[3],x[4])))

    Tranzitii.append(Lista)
    stack = ("Z",)
    start = 0
    last = 1
    coada = [(0, cuvant[0], 0, stack)]
    Sol = []
    while start < last:                 # simulez o coada de forma (stare, litera , index litera cuvant, stack)
        stare = coada[start][0]
        if len(Tranzitii) > stare:
            for x in Tranzitii[coada[start][0]]:               # pt fiecare stare adaug in coada toate starile in care poate merge
                if len(coada[start]) != 2:          # posibil 2
                    if x[1] == coada[start][1]:
                        if coada[start][2] < len(cuvant)-1:
                            if coada[start][3][-1][-1] == x[2]:
                                aux  = list(coada[start][3])
                                aux.pop()
                                if x[3] != "#":
                                    for y in x[3][::-1]:
                                        aux.append(y)
                                coada.append((x[0],cuvant[coada[start][2]+1],coada[start][2]+1, tuple(aux)))
                                last +=1
                        else:
                            if coada[start][3][-1][-1] == x[2]:
                                aux = list(coada[start][3])
                                aux.pop()
                                if x[3] != "#":
                                    for y in x[3][::-1]:
                                        aux.append(y)
                                coada.append((x[0],tuple(aux)))
                                last += 1
                    elif x[1] == "#":
                        if coada[start][2] < len(cuvant)-1:
                            if coada[start][3][-1][-1] == x[2]:
                                aux = list(coada[start][3])
                                aux.pop()
                                if x[3] != "#":
                                    for y in x[3][::-1]:
                                        aux.append(y)
                            coada.append((x[0],cuvant[coada[start][2]],coada[start][2],tuple(aux)))
                            last +=1
                        else:
                            coada.append((x[0],coada[start][3]))        # adaug doar starea si stiva
                            last += 1

                else:
                    Sol.append((coada[start][0], coada[start][1]))             # adaug in Sol starile in care se opreste cuvantul si stiva respectiva
                    #break
                    if x[1] == "#":
                        if coada[start][1][-1][-1] == x[2]:
                            aux = list(coada[start][1])
                            aux.pop()
                            if x[3] != "#":
                                for y in x[3][::-1]:
                                    aux.append(y)
                            coada.append((x[0],tuple(aux)))
                            last += 1
        else:
            if len(coada[start]) == 2:
                Sol.append((stare,coada[start][1]))
        start += 1
    ok = False
    for x in Sol:
        if x[0] in L_stari_fin:
            if (len(x[1]) == 0) or (len(x[1]) == 1 and x[1][-1] == "Z"):
                ok = True
    if ok == True:
        print("Cuvantul apartine limbajului recunoscut de automat")
    else:
        print("Cuvantul nu apartine limbajului recunoscut de automat")