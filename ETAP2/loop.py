import intro
import eda
import calcul

#zwiekszam do 10,by wykres liniowy pokazał trend spadku błędu w czasie
liczbaPowtórzeń = 10

def main():
    print('\nLICZBA KLASTRÓW', calcul.liczbaKlastrów)
    intro.wczytajDane()
    intro.normalizujDane()

    # Losujemy centroidy raz na początku, aby obie metryki startowały z tego samego punktu
    calcul.losujCentroidy()
    poczatkowe_centroidy = calcul.Centroidy.copy()

    #słowniki do zbierania historii błędów do wykresu liniowego
    historie_bledow = {'euklides': [], 'manhattan': []}
    metryki_do_testu = ['euklides', 'manhattan']

    for metryka in metryki_do_testu:
        #ten print to dla estetyki mozemy usunac
        print(f"\n=================== START EKSPERYMENTU: {metryka.upper()} ===================")
        #przywracamy identyczne centroidy startowe dla sprawiedliwego porównania
        calcul.Centroidy = poczatkowe_centroidy.copy()

        intro.denormalizujCentroidy(calcul.Centroidy)
        calcul.wypiszCentroidyDenormalizowane()
        calcul.przypiszKrotkomNumeryKlastrów(metryka)
        calcul.utwórzKlastry()
        intro.denormalizujDane(calcul.klastry)
        intro.formatujKlastry()
        eda.tabeleDlaKlastrów()

        repeat = 0
        while repeat < liczbaPowtórzeń:
            # 1. Logika obliczania błędu AKTUALNEGO stanu (do wykresu liniowego)
            błed_iteracji = 0
            for i in range(len(calcul.Centroidy)):
                for krotka in calcul.klastry[i]:
                    if metryka == 'manhattan':
                        błed_iteracji += calcul.Manhattan(krotka, calcul.Centroidy[i])
                    else:
                        błed_iteracji += calcul.EuklidesPower(krotka, calcul.Centroidy[i])
            historie_bledow[metryka].append(błed_iteracji)

            calcul.newCentroidy()
            intro.denormalizujCentroidy(calcul.Centroidy)
            calcul.wypiszCentroidyDenormalizowane()
            calcul.przypiszKrotkomNumeryKlastrów(metryka)
            calcul.utwórzKlastry()
            intro.denormalizujDane(calcul.klastry)
            intro.formatujKlastry()
            eda.tabeleDlaKlastrów()
            repeat += 1

    #po zakończeniu obu pętli generujemy wspólny wykres liniowy
    eda.wykres_liniowy_metryk(historie_bledow['euklides'], historie_bledow['manhattan'])
    # tu zmieniamy ilość klastów
    eda.optimise_k_means(20)

main()