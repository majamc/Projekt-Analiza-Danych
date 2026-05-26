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
    analysis.optimise_k_means(50)
    
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
        analysis.tabeleDlaKlastrów()
        repeat+=1

main()