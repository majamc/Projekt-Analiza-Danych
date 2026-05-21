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
    calcul.przypiszKrotkomNumeryKlastrów('manhattan') #jećli chce się uzyć mahnattan to zmienić na 'manhattan' (jakiekolwiek inne słowo będzie oznaczało, że kod użyje euklidesa)
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
        calcul.przypiszKrotkomNumeryKlastrów('manhattan') #tutaj tez trzeba zmieniac
        calcul.utwórzKlastry()
        intro.denormalizujDane(calcul.klastry)
        intro.formatujKlastry()
        eda.tabeleDlaKlastrów()
        repeat+=1
main()