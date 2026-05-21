import intro
import eda
import calcul

liczbaPowtórzeń = 1

def main():
    print('\nLICZBA KLASTRÓW', calcul.liczbaKlastrów)
    intro.wczytajDane()
    intro.normalizujDane()
    calcul.losujCentroidy()
    
    intro.denormalizujCentroidy(calcul.Centroidy)
    calcul.wypiszCentroidyDenormalizowane()
    calcul.przypiszKrotkomNumeryKlastrów()
    calcul.utwórzKlastry()
    intro.denormalizujDane(calcul.klastry)
    intro.formatujKlastry()
    eda.tabeleDlaKlastrów()

    # tu zmieniamy ilość klastów
    eda.optimise_k_means(20)
    
    repeat=0
    while repeat < liczbaPowtórzeń:
        calcul.newCentroidy()
        intro.denormalizujCentroidy(calcul.Centroidy)
        calcul.wypiszCentroidyDenormalizowane()
        calcul.przypiszKrotkomNumeryKlastrów()
        calcul.utwórzKlastry()
        intro.denormalizujDane(calcul.klastry)
        intro.formatujKlastry()
        eda.tabeleDlaKlastrów()
        repeat+=1
main()