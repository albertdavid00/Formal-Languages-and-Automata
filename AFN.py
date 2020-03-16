cuvant = input()
f = open("intrare.txt")
if cuvant == 'λ' or cuvant == '':
    print("Cuvantul apartine limbajului recunoscut de automat")
else:
    L_stari_fin = [int(x) for x in f.readline().split()]

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
    Lista = []
    for x in L_tranzitii:
        if x[0] != y:
            Tranzitii.append(Lista)
            Lista = []
            y = x[0]
            Lista.append(tuple((x[1], x[2])))
        else:
            Lista.append(tuple((x[1], x[2])))

    Tranzitii.append(Lista)
    start = 0
    last = 1
    coada = [(0,cuvant[0],0)]
    Sol = []
    while start < last:
        for x in Tranzitii[coada[start][0]]:
            if len(coada[start]) != 1:
                if x[1] == coada[start][1]:
                    if coada[start][2] < len(cuvant)-1:
                        coada.append((x[0],cuvant[coada[start][2]+1],coada[start][2]+1))
                    else:
                        coada.append((x[0],))
                    last += 1
            else:
                Sol.append(coada[start][0])
                break
        start += 1
    ok = False
    for x in Sol:
        if x in L_stari_fin:
            ok = True
    if ok == True:
        print("Cuvantul apartine limbajului recunoscut de automat")
    else:
        print("Cuvantul nu apartine limbajului recunoscut de automat")