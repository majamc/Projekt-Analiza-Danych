# Projekt-Analiza-Danych

Raport: https://docs.google.com/document/d/1wHmuxrQfZSwljyn2gp2vbEx-G4hBysHu6RXtZ2plnlo/edit?usp=sharing

**Instrukcja uruchomienia**

1. Upewnij się, że masz zainstalowanego pythona i pip
2. Zklonuj repozytorium https://github.com/majamc/Projekt-Analiza-Danych
3. Otwórz kod w dowolnym edytorze kodu
4. Zainstaluj potrzebne biblioteki za pomocą `pip install requirements.txt`
5. Wejdź do dowolnego etapu projektu i uruchom za pomocą `python loop.py`

**Struktura kodu**
Kod jest podzielony na dwa etapy:

- etap 1, który zawiera analizę zbioru TopBabyNamesByState
- etap 2, który zawiera analizę zbioru HealthcareDataset

Każdy z etapów posiada następujące pliki z kodem:

- intro - zajmuje się wczytaniem, normalizacją i denormalizacją danych
- calcul - zajmuje się losowaniem i przesuwaniem centroid oraz tworzeniem klastrów
- analisys - zajmuje się wykresami, formatowaniem oraz analizą zbioru
- loop - wywołanie wszystkich potrzebnych metod do klastrowania
