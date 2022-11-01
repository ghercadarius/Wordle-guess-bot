import random
f = open("cuvinte_wordle.txt", "r")
L=[]
for x in f:
    x = x.strip()
    L.append(x)
f.close()

cuv = L[int(random.randint(0, len(L)))]
gasit=False
i = 0
print(cuv)

while i < 5:
    aux = input()
    aux = aux.strip()
    aux = aux.upper()
    if len(aux) != 5:
        print("Cuvantul trebuie sa aiba 5 litere")
        continue
    if aux not in L:
        print("Cuvantul nu este in lista, incearca altul")
        continue
    if aux == cuv:
        print("Gasit")
        gasit = True
        break
    #verificam literele cuvantului citit sa le comparam cu cuvantul ales
    for j in range(len(aux)):
        if aux[j] == cuv[j]: #daca litera este in cuvantul ales si este pe pozitie punem G de la green
            print("G",end='')
        elif aux[j] in cuv: #daca litera este in cuvant dar nu este pe pozitie punem Y de la yellow
            print("Y",end='')
        else: #daca litera nu este deloc punem N
            print("N",end='')
    print("\n")
    i+=1
if gasit == False:
    print("Negasit")
