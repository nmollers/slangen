getallenlijst = input('Voer hier 5 getallen in gescheiden door een spatie: ').split()

print(sorted(getallenlijst, reverse=True, key=float))