import intro
import calcul
import analysis

liczbaPowtórzeń=10 #powtórzenia pętli

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
    analysis.tabeleDlaKlastrów()

    #tu zmieniamy ilość klastów
    analysis.optimise_k_means(10) #metoda łokcia do analizy liczby klastrów
    
    #blokada pętli
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
        analysis.tabeleDlaKlastrów()
        repeat+=1

main()