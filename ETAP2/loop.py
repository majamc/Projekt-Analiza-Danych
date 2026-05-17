import intro
import eda

liczbaPowtórzeń = 1

def main():
    intro.wczytajDane()
    intro.normalizujDane()

    # tu zmieniamy ilość klastów
    eda.optimise_k_means(20)

main()