f = open("cuvinte_wordle.txt", "r")
L=[]
for x in f:
    x = x.strip()
    L.append(x)
f.close()
import random #punem libraria pentru alegerea random
#print(L[int(random.uniform(0,11453))])
cuv = L[ int( random.uniform( 0 , 11453 ) ) ] #selectam cuvantul din lista de cuvinte
print(cuv)
gasit=False
aux=""
i = 0
#cele 5 incercari
while i < 5:
    aux = input()
    aux = aux.strip()
    aux = aux.upper()
    if len(aux) != 5:
        print(f"{i} Lungime incorecta")
        continue
    if aux not in L:
        print("Cuvantul nu este in lista, incearca altul")
        continue
    if aux == cuv: #comparam cuvantul citit cu cel ales
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
