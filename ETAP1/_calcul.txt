#moduł przechowuje początkową liczbę klastrów,
#oraz poczatkową pustą listę klastrów i centroidów.
#UWAGA: wartości poczatkowe zmiennych modułowych
#       są dostępne po każdorazowym załadowaniu modułu

import math
import random
import intro

liczbaKlastrów=100
# poczatkowa liczba klastrów
klastry=[]
#każdy z klastrów jest listą krotekNormal położonych najbliżej centroidy
Centroidy=[]

def test():
    print('\nLICZBA KLASTRÓW ',liczbaKlastrów)
    intro.wczytajDane()
    intro.normalizujDane()
    losujCentroidy()
    wypiszCentroidy()
    przypiszKrotkomNumeryKlastrów()
    #intro.wypiszKrotkiNormal()
    utwórzKlastry()
    wypiszKlastry()
    newCentroidy()
    wypiszCentroidy()

def losujCentroide():
# losuje początkowe położenie centroidy dla pojedynczego klastra
    centroida=[]
    state=random.randint(2,102)
    centroida.append(state)
    sex=random.choice([50,100])
    centroida.append(sex)
    year=random.randint(0,102)
    centroida.append(year)
    if sex==100:
        name=random.randint(1,56)
    else:
        name=random.randint(57,96)
    centroida.append(name)
    evens=random.uniform(0.18,140.0)
    centroida.append(evens)
    return centroida

def losujCentroidy():
# losuje określoną przez liczbę klastrów poczatkowe położenia centroid
    i=1
    while i<=liczbaKlastrów:
        Centroidy.append(losujCentroide())
        i=i+1

def wypiszCentroide(centroida):
       print ('%4d %4d %4d %4d %7.3f'%(centroida[0],centroida[1],centroida[2],centroida[3],centroida[4]))

def wypiszCentroidy():
# wypisuje do interpretera aktualne wartości wszystkich centroid
   print('CENTROIDY')
   for centroida in Centroidy:
      wypiszCentroide(centroida)

def EuklidesPower(krotkaNormal,centroida):
# zwraca kwadrat odległości euklidesowej danej krotkiNormal od danej centroidy
   suma=0
   for i in range(0,len(krotkaNormal)-1):
       if i != 1:
          dif=centroida[i]-krotkaNormal[i]
          difpow=math.pow(dif,2)
          suma+=difpow
   distance=math.sqrt(suma)
   return math.pow(distance,2)

def przypiszKrotkomNumeryKlastrów():
# przypisuje każdej znormalizowanej krotce najbliższą centroidę
    for krotkaNormal in intro.krotkiNormal:
        minimum=1e100
        for i in range(len(Centroidy)):
            next=EuklidesPower(krotkaNormal,Centroidy[i])
            if next<minimum:
                minimum=next
                minimumIndex=i
        krotkaNormal[5]=minimumIndex

def utwórzKlastry():
    for i in range(0,len(Centroidy)):
        klaster=[]
        for krotka in intro.krotkiNormal:
            if krotka[5]==i:
                klaster.append(krotka)
        klastry.append(klaster)

def wypiszKlaster(nrKlastra):
    print('NUMER KLASTRA ',nrKlastra)
    for krotka in klastry[nrKlastra]:
        print ('%4d %4d %4d %4d %7.3f %4d'%(krotka[0],krotka[1],krotka[2],krotka[3],krotka[4],krotka[5]))

def wypiszKlastry():
# wypisuje do interpretera aktualne wartości wszystkich klastrów
    for numer in range(0,len(Centroidy)):
       wypiszKlaster(numer)

def newCentroide(klaster):
# oblicza nowe położenie centroidy we wskazanym klastrze
# i zwraca wynik w postaci nowej centroidy dla wskazanego klastra
    sumState=sumYear=sumEven=0
    sumFemName=sumMalName=numFemName=numMalName=0
    centroida=[]
    for krotka in klaster:
        sumState+=krotka[0]
        if krotka [1]==100:
            sumFemName+=krotka[3]
            numFemName+=1
        else:
            sumMalName+=krotka[3]
            numMalName+=1
        sumYear+=krotka[2]
        sumEven+=krotka[4]
    centroida.append(sumState//len(klaster))
    if numFemName>=numMalName:
        centroida.append(100)
    else:
        centroida.append(50)
    centroida.append(sumYear//len(klaster))
    if numFemName>=numMalName:
        centroida.append(sumFemName//numFemName)
    else:
        centroida.append(sumMalName//numMalName)
    centroida.append(sumEven/len(klaster))
    return centroida

def newCentroidy():
    Centroidy=[]
    print('\nprzesunięto centroidy ------------')
    for nr in range(liczbaKlastrów):
        Centroidy.append(newCentroide(klastry[nr]))


