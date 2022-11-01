s=input()
L=[]
while s != "-1": #citim lista de cuvinte de la tastatura deocamdata
    L.append(s)
    s=input()
import random #punem libraria pentru alegerea random
#print(L[int(random.uniform(0,11453))])
cuv = L[ int( random.uniform( 0 , 11453 ) ) ] #selectam cuvantul din lista de cuvinte
print(cuv)
gasit=False
aux=""
#cele 5 incercari
for i in range( 0 , 5 ):
    aux = input()
    if aux is cuv: #comparam cuvantul citit cu cel ales
        gasit=True
        break
    #verificam literele cuvantului citit sa le comparam cu cuvantul ales
    for j in range(0,len(aux)):
        if aux[j] == cuv[j]: #daca litera este in cuvantul ales si este pe pozitie punem G de la green
            print("G",end='')
        elif aux[j] in cuv: #daca litera este in cuvant dar nu este pe pozitie punem Y de la yellow
            print("Y",end='')
        else: #daca litera nu este deloc punem N
            print("N",end='')
    print("\n")
if gasit is False:
    print("Negasit")
else:
    print("Gasit")
