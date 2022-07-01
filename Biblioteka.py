print("Biblioteka filmów i seriali")

class Movies:
    def __init__ (self, tytul, rok_wydania, gatunek, liczba_odtworzen):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzen = liczba_odtworzen
        self.liczba_odtworzen = 0 
    def __str__ (self):
        return f'{self.tytul}, ({self.rok_wydania})'
    def play(self, step=1):
        self.liczba_odtworzen += step
        
class Series(Movies):
    def __init__ (self, numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu 
    def __str__ (self):
        return f"{self.tytul}, S0{self.numer_odcinka}, E0{self.numer_sezonu}"

film = Movies (tytul = "Minionki na końcu świata", rok_wydania ="2025", gatunek="Familijny", liczba_odtworzen = 0)
film1 = Movies (tytul = "Powrót do przyszłej przeszłości", rok_wydania ="2020", gatunek="Fantasy", liczba_odtworzen = 0)

serial = Series(tytul ="Dzień z zycia Rekina" , rok_wydania="2020", gatunek="Przyrodniczy", numer_odcinka = int(4), numer_sezonu = int(2), liczba_odtworzen = 0)
serial1= Series(tytul ="Przygody Bociana Bogdana" , rok_wydania="2018", gatunek="Familijny", numer_odcinka = int(6), numer_sezonu = int(1), liczba_odtworzen = 0)

biblioteka = [film, film1, serial, serial1]

print(serial)
print(film)
print(serial1)
print(film1)


film.play()
print(film.liczba_odtworzen)
film.play()
print(film.liczba_odtworzen)

film1.play()
film1.play()
film1.play()
print(film1.liczba_odtworzen)


#def get_movies():
for Movies in biblioteka:
    print(Movies)

print("     ")

for Series in biblioteka:
    print(Series)



#def get_series(): 
