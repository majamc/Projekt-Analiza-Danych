# moduł przechowuje:
# oryginalne i znormalizowane krotki danych,
# słowniki normalizacyjne do zmiennych tekstowych,
# funkcje wczytywania i wypisywania krotek,
# funkcję normalizacji danych
import math

def test():
    wczytajDane()
    wypiszDane()
    normalizujDane()
    wypiszKrotkiNormal()

krotkiDane=[]
krotkiNormal=[]
zdenormalizowaneKlastry = []
zdenormalizowaneCentroidy = []

# definicje słowników normalizacyjnych dla zmiennych tekstowych
states={'AK':2,'AL':4,'AR':6,'AZ':8,'CA':10,'CO':12,'CT':14,'DC':16,'DE':18,
        'FL':20,'GA':22,'HI':24,'IA':26,'ID':28,'IL':30,'IN':32,'KS':34,'KY':36,
        'LA':38,'MA':40,'MD':42,'ME':44,'MI':46,'MN':48,'MO':50,'MS':52,'MT':54,
        'NC':56,'ND':58,'NE':60,'NH':62,'NJ':64,'NM':66,'NV':68,'NY':70,'OH':72,
        'OK':74,'OR':76,'PA':78,'RI':80,'SC':82,'SD':84,'TN':86,'TX':88,'UT':90,
        'VA':92,'VT':94,'WA':96,'WI':98,'WV':100,'WY':102}
sex=   {'F':0,'M':1}
#2 razy musi byc narazie samantha bo z jakiegos powodu inaczej jej nie czyta???? postaram sie to naprawic 
names= {'Mary':1,'Linda':2,'Debra':3,'Lisa':4,'Michelle':5,'Jennifer':6,'Jessica':7,
        'Samantha':8,'Ashley':9,'Hannah':10,'Madison':11,'Emma':12,'Isabella':13,
        'Olivia':14,'Kimberly':15,'Angela':16,'Amanda':17,'Emily':18,'Mia':19,
        'Sophia':20,'Barbara':21,'Susan':22,'Karen':23,'Patricia':24,'Alexis':25,
        'Kayla':26,'Katherine':27,'Deborah':28,'Donna':29,'Sarah':30,'Ava':31,
        'Brittany':32,'Helen':33,'Shirley':34,'Carol':35,'Taylor':36,'Chloe':37,
        'Betty':38,'Sharon':39,'Julie':40,'Lori':41,'Addison':42,'Dorothy':43,
        'Samantha':44,'Margaret':45,'Megan':46,'Jasmine':47,'Melissa':48,'Judith':49,
        'Nancy':50,'Sandra':51,'Joan':52,'Alyssa':53,'Ruth':54,'Cindy':55,'Brenda':56,
        'John':57,'Robert':58,'Michael':59,'David':60,'Christopher':61,'Jacob':62,
        'Ethan':63,'James':64,'Aiden':65,'William':66,'Mason':67,'Justin':68,
        'Jason':69,'Joshua':70,'Angel':71,'Anthony':72,'Daniel':73,'Alexander':74,
        'Liam':75,'Matthew':76,'Ryan':77,'Jayden':78,'George':79,'Richard':80,
        'Noah':81,'Carter':82,'Tyler':83,'Logan':84,'Samuel':85,'Elijah':86,
        'Larry':87,'Austin':88,'Owen':89,'Wyatt':90,'Jose':91,'Joe':92,
        'Isaiah':93,'Benjamin':94,'Nicholas':95,'Andrew':96,}

def wczytajDane():
# wczytuje dane ze wskazanego pliku tekstowego do listy krotkiDane
   import csv
    #używam dane mini do testowania
   with open('dane_midi.txt','r') as csvfile:
      csvreader = csv.reader(csvfile)
      for krotka in csvreader:
         krotkiDane.append(krotka)

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
      nameNorm = (names[forth]-1)/(96-1)
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

         year = int((klastry[i][j][2]*(2020-1910))+1910)

         nameNmbr = int(round(klastry[i][j][3]*(96-1))+1)
         for key, val in names.items():
            if val == nameNmbr:
               name = key
               break
            #chwilowa zaslepka jakby cos sie zepsulo
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

      year = int((centroidy[i][2]*(2020-1910))+1910)

      nameNmbr = int(round((centroidy[i][3]*(96-1)))+1)
      for key, val in names.items():
            if val == nameNmbr:
               name = key
               break
            #chwilowa zaslepka jakby cos sie zepsulo
            #else: name = nameNmbr

      occurences =  int((centroidy[i][4]*(maxOcc - minOcc))+minOcc)
      daneTmp = [state, sex, year, name, occurences]
      zdenormalizowaneCentroidyTmp.append(daneTmp)
   zdenormalizowaneCentroidy = zdenormalizowaneCentroidyTmp

