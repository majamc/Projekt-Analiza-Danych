import intro
import calcul
import eda

liczbaPowtórzeń=1
# ograniczenie liczby powtórzeń pętli

def main():
    print('\nLICZBA KLASTRÓW ',calcul.liczbaKlastrów)
    intro.wczytajDane()
    intro.normalizujDane()
    calcul.losujCentroidy()
    
    intro.denormalizujCentroidy(calcul.Centroidy)
    #calcul.wypiszCentroidy()
    calcul.wypiszCentroidyDenormalizowane()
    calcul.przypiszKrotkomNumeryKlastrów()
    calcul.utwórzKlastry()
    intro.denormalizujDane(calcul.klastry)
    #calcul.wypiszKlastry()
    #calcul.wypiszKlastryDenormalizowane()
    intro.formatujKlastry()
    eda.tabeleDlaKlastrów()

    #tu zmieniamy ilość klastów
    eda.optimise_k_means(15)
    
    # poniżej założono blokadę pętli (zdjełam blokade)
    repeat=0
    while repeat < liczbaPowtórzeń:
        calcul.newCentroidy()
        intro.denormalizujCentroidy(calcul.Centroidy)
        #calcul.wypiszCentroidy()
        calcul.wypiszCentroidyDenormalizowane()
        calcul.przypiszKrotkomNumeryKlastrów()
        calcul.utwórzKlastry()
        intro.denormalizujDane(calcul.klastry)
        #calcul.wypiszKlastry()
        #calcul.wypiszKlastryDenormalizowane()
        intro.formatujKlastry()
        eda.tabeleDlaKlastrów()
        repeat+=1

main()