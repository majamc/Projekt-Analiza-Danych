# moduł przechowuje:
# oryginalne i znormalizowane krotki danych,
# słowniki normalizacyjne do zmiennych tekstowych,
# funkcje wczytywania i wypisywania krotek,
# funkcję normalizacji danych
import os

def test():
    wczytajDane()
    wypiszDane()
    normalizujDane()
    wypiszKrotkiNormal()

krotkiDane=[]
krotkiNormal=[]
zdenormalizowaneKlastry = []
zdenormalizowaneKlastryBezNrCentroid = []
zdenormalizowaneCentroidy = []

sciezkaDoDanychCsv = os.path.join('..','TopBabyNamesbyState.csv')

# definicje słowników normalizacyjnych dla zmiennych tekstowych
states={'AK':2,'AL':4,'AR':6,'AZ':8,'CA':10,'CO':12,'CT':14,'DC':16,'DE':18,
        'FL':20,'GA':22,'HI':24,'IA':26,'ID':28,'IL':30,'IN':32,'KS':34,'KY':36,
        'LA':38,'MA':40,'MD':42,'ME':44,'MI':46,'MN':48,'MO':50,'MS':52,'MT':54,
        'NC':56,'ND':58,'NE':60,'NH':62,'NJ':64,'NM':66,'NV':68,'NY':70,'OH':72,
        'OK':74,'OR':76,'PA':78,'RI':80,'SC':82,'SD':84,'TN':86,'TX':88,'UT':90,
        'VA':92,'VT':94,'WA':96,'WI':98,'WV':100,'WY':102}
sex=   {'F':0,'M':1}
names= {'Mary':1,'Linda':2,'Debra':3,'Lisa':4,'Michelle':5,'Jennifer':6,'Jessica':7,
        'Samantha':8,'Ashley':9,'Hannah':10,'Madison':11,'Emma':12,'Isabella':13,
        'Olivia':14,'Kimberly':15,'Angela':16,'Amanda':17,'Emily':18,'Mia':19,
        'Sophia':20,'Barbara':21,'Susan':22,'Karen':23,'Patricia':24,'Alexis':25,
        'Kayla':26,'Katherine':27,'Deborah':28,'Donna':29,'Sarah':30,'Ava':31,
        'Brittany':32,'Helen':33,'Shirley':34,'Carol':35,'Taylor':36,'Chloe':37,
        'Betty':38,'Sharon':39,'Julie':40,'Lori':41,'Addison':42,'Dorothy':43,
        'Margaret':44,'Megan':45,'Jasmine':46,'Melissa':47,'Judith':48,
        'Nancy':49,'Sandra':50,'Joan':51,'Alyssa':52,'Ruth':53,'Cindy':54,'Brenda':55,
        'John':56,'Robert':57,'Michael':58,'David':59,'Christopher':60,'Jacob':61,
        'Ethan':62,'James':63,'Aiden':64,'William':65,'Mason':66,'Justin':67,
        'Jason':68,'Joshua':69,'Angel':70,'Anthony':71,'Daniel':72,'Alexander':73,
        'Liam':74,'Matthew':75,'Ryan':76,'Jayden':77,'George':78,'Richard':79,
        'Noah':80,'Carter':81,'Tyler':82,'Logan':83,'Samuel':84,'Elijah':85,
        'Larry':86,'Austin':87,'Owen':88,'Wyatt':89,'Jose':90,'Joe':91,
        'Isaiah':92,'Benjamin':93,'Nicholas':94,'Andrew':95,}

def wczytajDane():
# wczytuje dane ze wskazanego pliku tekstowego do listy krotkiDane
   import csv
   with open('Dane.txt','r') as csvfile:
      csvreader = csv.reader(csvfile)
      for krotka in csvreader:
         if 'State' in krotka: #warunek żeby nie wczytywać nazw kolumn z pliku z danymi
            continue
         else: krotkiDane.append(krotka)

def wypiszDane():
# wypisuje zawartość listy krotkiDane do interpretera
   for krotka in krotkiDane:
       print(krotka[0]," ",krotka[1]," ",krotka[2],'%-10s'%(krotka[3]),'%4s'%krotka[4])

def wypiszKrotkiNormal():
# wypisuje zawartość listy krotkiNormal do interpretera
   print('KROTKI NORMAL')
   for krotka in krotkiNormal:
      print ('%7.3f %7.3f %7.3f %7.3f %7.3f %4d'%(krotka[0],krotka[1]
                                                  ,krotka[2],krotka[3]
                                                  ,krotka[4],krotka[5]))

def minMaxOcc():
   #oblicza minimalną i maksymalną liczbę wystąpień
   occ = []
   for row in krotkiDane:
      occ.append(int(row[4]))
   minOcc = min(occ)
   maxOcc = max(occ)
   return minOcc, maxOcc

def normalizujDane():
# normalizuje dane surowe z listy *krotki* i wpisuje je do listy *krotkiNormal*
# -1 oznacza, że nie wpisano jeszcze numeru klastra, do którego należy krotka

   minOcc, maxOcc = minMaxOcc()

   for i in range(len(krotkiDane)):
      krotka=[]

      #STATE zakres 0-1
      first = krotkiDane[i][0]
      stateNorm = (states[first]-2)/(102-2)
      krotka.append(stateNorm)

      #GENDER 0 lub 1
      second=krotkiDane[i][1]
      krotka.append(sex[second])

      #YEAR normalizacja Min-Max
      third=krotkiDane[i][2]
      result=(int(third)-1910)/(2012-1910)
      krotka.append(result)

      #NAME zakres normalizacja Min-Max
      forth = krotkiDane[i][3]
      nameNorm = (names[forth]-1)/(95-1)
      krotka.append(nameNorm)

      #OCCURRENCES normalizacja Min-Max
      fifth = krotkiDane[i][4]
      result = (int(fifth) - minOcc) / (maxOcc - minOcc)
      krotka.append(result)

      #numer klastra
      krotka.append(-1)
      #dodanie rekordu
      krotkiNormal.append(krotka)

def denormalizujDane(klastry):
   #denormalizuje dane z klastrów żeby można je było łatwo przeczytać
   global zdenormalizowaneKlastry
   minOcc, maxOcc = minMaxOcc()
   zdenormalizowaneKlastryTmp = []
   for i in range(len(klastry)):
      daneCentroidow = []
      for j in range(len(klastry[i])):
         stateNmbr = (klastry[i][j][0]*(102-2))+2
         if int(stateNmbr) % 2 == 0:
            stateNmbr = int(stateNmbr)
         else:
            stateNmbr = int(stateNmbr)+1
            
         for key, val in states.items():
            if val == stateNmbr:
               state = key
               break

         if klastry[i][j][1] == 1:
            sex = 'M'
         else: sex = 'F'

         year = int((klastry[i][j][2]*(2012-1910))+1910)

         nameNmbr = int(round(klastry[i][j][3]*(95-1))+1)
         for key, val in names.items():
            if val == nameNmbr:
               name = key
               break
            #odkomentowac jakby cos sie zepsulo
            #else: name = nameNmbr

         occurences =  int((klastry[i][j][4]*(maxOcc - minOcc))+minOcc)

         daneTmp = [state, sex, year, name, occurences, klastry[i][j][5]]
         daneCentroidow.append(daneTmp)
      zdenormalizowaneKlastryTmp.append(daneCentroidow)
   zdenormalizowaneKlastry = zdenormalizowaneKlastryTmp

def denormalizujCentroidy(centroidy):
   #denormalizuje dane z centroid żeby można je było łatwo przeczytać
   global zdenormalizowaneCentroidy
   minOcc, maxOcc = minMaxOcc()
   zdenormalizowaneCentroidyTmp = []
   for i in range(len(centroidy)):
      stateNmbr = (centroidy[i][0]*(102-2))+2
      if int(stateNmbr) % 2 == 0:
         stateNmbr = int(stateNmbr)
      else:
         stateNmbr = int(stateNmbr)+1
         
      for key, val in states.items():
            if val == stateNmbr:
               state = key
               break

      if centroidy[i][1] == 1:
            sex = 'M'
      else: sex = 'F'

      year = int((centroidy[i][2]*(2012-1910))+1910)

      nameNmbr = int(round((centroidy[i][3]*(95-1)))+1)
      for key, val in names.items():
            if val == nameNmbr:
               name = key
               break
            #odkomentowac jakby cos sie zepsulo
            #else: name = nameNmbr

      occurences =  int((centroidy[i][4]*(maxOcc - minOcc))+minOcc)
      daneTmp = [state, sex, year, name, occurences]
      zdenormalizowaneCentroidyTmp.append(daneTmp)
   zdenormalizowaneCentroidy = zdenormalizowaneCentroidyTmp
   
def formatujKlastry():
   #usuwa nr centroida do ktorego naleza dane aby ladnie mozna je bylo wyswietlic
   global zdenormalizowaneKlastryBezNrCentroid
   zdenormalizowaneKlastryBezNrCentroid = zdenormalizowaneKlastry.copy()
   for i in range(len(zdenormalizowaneKlastry)):
      for j in range(len(zdenormalizowaneKlastry[i])):
         zdenormalizowaneKlastryBezNrCentroid[i][j].pop(5)

