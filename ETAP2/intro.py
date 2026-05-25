import csv

krotkiDane=[]
krotkiNormal=[]
zdenormalizowaneKlastry = []
zdenormalizowaneKlastryBezNrCentroid = []
zdenormalizowaneCentroidy = []

#slowniki normalizacyjne
gender = {"Female": 0, "Male": 1}
medicalCondition = {"Cancer": 0, "Obesity": 1, "Diabetes": 2, "Arthritis": 3, "Hypertension": 4, "Asthma": 5}
medicationName = {"Lipitor": 0, "Ibuprofen": 1, "Aspirin": 2, "Paracetamol": 3, "Penicillin": 4}
admissionType = {"Elective": 0, "Urgent": 1, "Emergency": 2}

def wczytajDane():
#wczytanie danych ze zbioru do listy krotkiDane
   with open('HealthcareDataset.csv','r') as csvfile:
      csvreader = csv.reader(csvfile)
      for krotka in csvreader:
         if 'Gender' in krotka: #warunek żeby nie wczytywać nazw kolumn z pliku z danymi
            continue
         else: krotkiDane.append(krotka)
         
def minMaxAge():
   #oblicza minimalny i maksymalny wiek
   age = []
   for row in krotkiDane:
      age.append(int(row[0]))
   minAge = min(age)
   maxAge = max(age)
   return minAge, maxAge

def normalizujDane():
#normalizowanie danych z listy krotkiDane i wpisanie ich do listy krotkiNormal
#-1 oznacza, że nie wpisano jeszcze numeru klastra, do którego należy krotka
   minAge, maxAge = minMaxAge()

   for i in range(len(krotkiDane)):
      krotka=[]

      #AGE normalizacja Min-Max
      first = krotkiDane[i][0]
      ageNorm = (int(first) - minAge) / (maxAge - minAge)
      krotka.append(ageNorm)

      #GENDER 0 lub 1
      second=krotkiDane[i][1]
      krotka.append(gender[second])

      #MEDICAL CONDITION normalizacja Min-Max ze slownika normalizacyjnego
      third=krotkiDane[i][2]
      conditionNorm = medicalCondition[third]/5
      krotka.append(conditionNorm)

      #MEDICATION normalizacja Min-Max ze slownika normalizacyjnego
      forth = krotkiDane[i][3]
      medicationNorm = medicationName[forth]/4
      krotka.append(medicationNorm)

      #ADMISSION TYPE normalizacja Min-Max ze slownika normalizacyjnego
      fifth = krotkiDane[i][4]
      admissionNorm = admissionType[fifth]/2
      krotka.append(admissionNorm)

      #numer klastra (narazie -1)
      krotka.append(-1)
      krotkiNormal.append(krotka)
      
def denormalizujDane(klastry):
   #denormalizowanie danych z klastrów żeby można je było łatwo przeczytać
   global zdenormalizowaneKlastry
   minAge, maxAge = minMaxAge()
   zdenormalizowaneKlastryTmp = []
   for i in range(len(klastry)):
      daneCentroidow = []
      for j in range(len(klastry[i])):
         age = int((klastry[i][j][0]*(maxAge - minAge))+minAge)

         if klastry[i][j][1] == 1:
            gender = 'Male'
         else: gender = 'Female'

         conditionNmbr = int(klastry[i][j][2]*5)
         for key, val in medicalCondition.items():
            if val == conditionNmbr:
               condition = key
               break

         medicationNmbr = int(klastry[i][j][3]*4)
         for key, val in medicationName.items():
            if val == medicationNmbr:
               medication = key
               break
           
         admissionNmbr = int(klastry[i][j][4]*2)
         for key, val in admissionType.items():
            if val == admissionNmbr:
               admission = key
               break

         daneTmp = [age, gender, condition, medication, admission, klastry[i][j][5]]
         daneCentroidow.append(daneTmp)
      zdenormalizowaneKlastryTmp.append(daneCentroidow)
   zdenormalizowaneKlastry = zdenormalizowaneKlastryTmp

def denormalizujCentroidy(centroidy):
   #denormalizowanie danych z centroid żeby można je było łatwo przeczytać
   global zdenormalizowaneCentroidy
   minAge, maxAge = minMaxAge()
   zdenormalizowaneCentroidyTmp = []
   for i in range(len(centroidy)):
      age = int((centroidy[i][0]*(maxAge - minAge))+minAge)

      if centroidy[i][1] == 1:
            gender = 'Male'
      else: gender = 'Female'

      conditionNmbr = int(centroidy[i][2]*5)
      for key, val in medicalCondition.items():
            if val == conditionNmbr:
               condition = key
               break

      medicationNmbr = int(centroidy[i][3]*4)
      for key, val in medicationName.items():
            if val == medicationNmbr:
               medication = key
               break
           
      admissionNmbr = int(centroidy[i][4]*2)
      for key, val in admissionType.items():
            if val == admissionNmbr:
               admission = key
               break

      daneTmp = [age, gender, condition, medication, admission]
      zdenormalizowaneCentroidyTmp.append(daneTmp)
   zdenormalizowaneCentroidy = zdenormalizowaneCentroidyTmp
   
def formatujKlastry():
   #usuwanie nr centroidy do ktorego naleza dane aby ladnie mozna je bylo wyswietlic
   global zdenormalizowaneKlastryBezNrCentroid
   zdenormalizowaneKlastryBezNrCentroid = zdenormalizowaneKlastry.copy()
   for i in range(len(zdenormalizowaneKlastry)):
      for j in range(len(zdenormalizowaneKlastry[i])):
         zdenormalizowaneKlastryBezNrCentroid[i][j].pop(5)