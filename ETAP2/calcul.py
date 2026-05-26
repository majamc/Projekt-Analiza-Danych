import math
import random
import intro
import numpy as np

liczbaKlastrów=5 #poczatkowa liczba klastrów
klastry=[] #klaster = lista krotekNormal położonych najbliżej centroidy
Centroidy=[]

def losujCentroide():
    #losowanie początkowego położenia centroidy dla pojedynczego klastra
    centroida = []

    age = random.uniform(0, 1)
    centroida.append(age)

    gender = random.choice([0, 1])
    centroida.append(gender)

    condition = random.uniform(0, 1)
    centroida.append(condition)

    medication = random.uniform(0, 1)
    centroida.append(medication)

    admission = random.uniform(0, 1)
    centroida.append(admission)

    return centroida

def losujCentroidy():
#losowanie początkowych położeń centroid (tyle ile klastrów)
    i=1
    while i<=liczbaKlastrów:
        Centroidy.append(losujCentroide())
        i=i+1
        
def wypiszCentroideDenormalizowana(centroida):
       print (centroida[0],centroida[1],centroida[2],
               centroida[3],centroida[4])
       
def wypiszCentroidyDenormalizowane():
#wypisanie do konsoli aktualnych wartości wszystkich zdenormalizowanych centroid
   print('CENTROIDY')
   for centroida in intro.zdenormalizowaneCentroidy:
      wypiszCentroideDenormalizowana(centroida)

def EuklidesPower(krotkaNormal,centroida):
#zwraca kwadrat odległości euklidesowej danej krotkiNormal od danej centroidy
   suma=0
   for i in range(0,len(krotkaNormal)-1):
       if i != 1:
          dif=centroida[i]-krotkaNormal[i]
          difpow=math.pow(dif,2)
          suma+=difpow
   distance=math.sqrt(suma)
   return math.pow(distance,2)

def Manhattan(krotkaNormal,centroida):
#zwraca odleglosc manhattan dla danej krotkiNormal od danej centroidy
    idx = [0,2,3,4] #bez 1 bo nie liczy sie płci
    
    krotkaFormated = np.array([krotkaNormal[i] for i in idx])
    centroidaFormated = np.array([centroida[i] for i in idx])
    
    distance = np.sum(np.abs(krotkaFormated - centroidaFormated))
    return distance
      
def przypiszKrotkomNumeryKlastrów(metodaOdleglosci):
#przypisanie każdej znormalizowanej krotce najbliższej centroidy
    for krotkaNormal in intro.krotkiNormal:
        minimum=1e100
        for i in range(len(Centroidy)):
            if metodaOdleglosci == 'manhattan':
                next=Manhattan(krotkaNormal,Centroidy[i])
            else: next=EuklidesPower(krotkaNormal,Centroidy[i])
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
        
def wypiszKlasterDenormalizowany(nrKlastra):
    print('NUMER KLASTRA ',nrKlastra)
    for krotka in intro.zdenormalizowaneKlastry[nrKlastra]:
        print (krotka[0],krotka[1],krotka[2],krotka[3],krotka[4],krotka[5])
        
def wypiszKlastryDenormalizowane():
#wypisanie w konsoli aktualnych wartości wszystkich zdenormalizowanych klastrów
    for numer in range(0,len(Centroidy)):
       wypiszKlasterDenormalizowany(numer)
       
def newCentroide(klaster):
#oblizanie nowego położenienia centroidy w danym klastrze
#zwraca wynik w postaci nowej centroidy dla wskazanego klastra
    #poprawa błędu dzielenia przez 0
    if len(klaster) == 0:
        return losujCentroide()

    sumCondition=sumMedication=sumAge=sumAdmission=0
    numFemName=numMalName=0
    centroida=[]
    for krotka in klaster:
        sumCondition+=krotka[2]
        sumMedication+=krotka[3]
        sumAge+=krotka[0]
        sumAdmission+=krotka[4]
        if krotka [1]==1:
            numFemName+=1
        else:
            numMalName+=1
    
    centroida.append(sumAge/len(klaster))
    
    #czy w centroidzie jest więcej mężczyzn niż kobiet
    if numFemName>=numMalName:
        centroida.append(1)
    else:
        centroida.append(0)

    centroida.append(sumCondition/len(klaster))
    centroida.append(sumMedication/len(klaster))
    centroida.append(sumAdmission/len(klaster)) 
    return centroida

def newCentroidy():
    global Centroidy
    noweCentroidy=[]
    print('\nprzesunięto centroidy ------------')
    for nr in range(liczbaKlastrów):
        noweCentroidy.append(newCentroide(klastry[nr]))
    Centroidy = noweCentroidy

