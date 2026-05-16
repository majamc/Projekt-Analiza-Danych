#moduł przechowuje początkową liczbę klastrów,
#oraz poczatkową pustą listę klastrów i centroidów.
#UWAGA: wartości poczatkowe zmiennych modułowych
#       są dostępne po każdorazowym załadowaniu modułu

import math
import random
import intro

liczbaKlastrów=6
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
    intro.wypiszKrotkiNormal()
    utwórzKlastry()
    wypiszKlastry()
    newCentroidy()
    wypiszCentroidy()

def losujCentroide():
    # losuje początkowe położenie centroidy dla pojedynczego klastra
    centroida = []

    state = random.uniform(0, 1)
    centroida.append(state)

    sex = random.choice([0, 1])
    centroida.append(sex)

    year = random.uniform(0, 1)
    centroida.append(year)

    name = random.uniform(0, 1)
    centroida.append(name)

    evens = random.uniform(0, 1)
    centroida.append(evens)

    return centroida

def losujCentroidy():
# losuje określoną przez liczbę klastrów poczatkowe położenia centroid
    i=1
    while i<=liczbaKlastrów:
        Centroidy.append(losujCentroide())
        i=i+1

def wypiszCentroide(centroida):
       print ('%7.3f %7.3f %7.3f %7.3f %7.3f'%
              (centroida[0],centroida[1],centroida[2],
               centroida[3],centroida[4]))
       
def wypiszCentroideDenormalizowana(centroida):
       print (centroida[0],centroida[1],centroida[2],
               centroida[3],centroida[4])

def wypiszCentroidy():
# wypisuje do interpretera aktualne wartości wszystkich centroid
   print('CENTROIDY')
   for centroida in Centroidy:
      wypiszCentroide(centroida)
      
def wypiszCentroidyDenormalizowane():
# wypisuje do interpretera aktualne wartości wszystkich zdenormalizowany centroid
   print('CENTROIDY')
   for centroida in intro.zdenormalizowaneCentroidy:
      wypiszCentroideDenormalizowana(centroida)

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
    global klastry
    klastry = []
    for i in range(0,len(Centroidy)):
        klaster=[]
        for krotka in intro.krotkiNormal:
            if krotka[5]==i:
                klaster.append(krotka)
        klastry.append(klaster)

def wypiszKlaster(nrKlastra):
    print('NUMER KLASTRA ',nrKlastra)
    for krotka in klastry[nrKlastra]:
        print ('%7.3f %7.3f %7.3f %7.3f %7.3f %4d'%(krotka[0],krotka[1],
                                            krotka[2],krotka[3],
                                            krotka[4],krotka[5]))
        
def wypiszKlasterDenormalizowany(nrKlastra):
    print('NUMER KLASTRA ',nrKlastra)
    for krotka in intro.zdenormalizowaneKlastry[nrKlastra]:
        print (krotka[0],krotka[1],krotka[2],krotka[3],krotka[4],krotka[5])

def wypiszKlastry():
# wypisuje do interpretera aktualne wartości wszystkich klastrów
    for numer in range(0,len(Centroidy)):
       wypiszKlaster(numer)

def wypiszKlastryDenormalizowane():
# wypisuje do interpretera aktualne wartości wszystkich zdenormalizowanych klastrów
    for numer in range(0,len(Centroidy)):
       wypiszKlasterDenormalizowany(numer)

def newCentroide(klaster):
# oblicza nowe położenie centroidy we wskazanym klastrze
# i zwraca wynik w postaci nowej centroidy dla wskazanego klastra
    #poprawa błędu dzielenia przez 0
    if len(klaster) == 0:
        return losujCentroide()

    sumState=sumYear=sumEven=0
    sumFemName=sumMalName=numFemName=numMalName=0
    centroida=[]
    for krotka in klaster:
        sumState+=krotka[0]
        if krotka [1]==1:
            sumFemName+=krotka[3]
            numFemName+=1
        else:
            sumMalName+=krotka[3]
            numMalName+=1
        sumYear+=krotka[2]
        sumEven+=krotka[4]
    centroida.append(sumState/len(klaster))
    if numFemName>=numMalName:
        centroida.append(1)
    else:
        centroida.append(0)
    centroida.append(sumYear/len(klaster))
    if numFemName>=numMalName:
        centroida.append(sumFemName/numFemName)
    else:
        centroida.append(sumMalName/numMalName)
    centroida.append(sumEven/len(klaster))
    return centroida
def newCentroidy():
    global Centroidy
    noweCentroidy=[]
    print('\nprzesunięto centroidy ------------')
    for nr in range(liczbaKlastrów):
        noweCentroidy.append(newCentroide(klastry[nr]))
    Centroidy = noweCentroidy

