
from random import randrange
import datetime 

dzis = datetime.date.today()


print("Biblioteka filmów i seriali")

class Movie:
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
        
class Series(Movie):
    def __init__ (self, numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu 
    def __str__ (self):
        return f"{self.tytul}, S0{self.numer_odcinka}, E0{self.numer_sezonu}"

film = Movie (tytul = "Minionki na końcu świata", rok_wydania ="2025", gatunek="Familijny", liczba_odtworzen = 0)
film1 = Movie (tytul = "Powrót do przyszłej przeszłości cz.1", rok_wydania ="2020", gatunek="Fantasy", liczba_odtworzen = 0)
film2 = Movie (tytul = "Powrót do przyszłej przeszłości cz.2", rok_wydania ="2021", gatunek="Fantasy", liczba_odtworzen = 0)
film3 = Movie (tytul = "Powrót do przyszłej przeszłości cz.3", rok_wydania ="2022", gatunek="Fantasy", liczba_odtworzen = 0)
film4 = Movie (tytul = "Szklana pułapka cz.1", rok_wydania ="2000", gatunek="Triller", liczba_odtworzen = 0)
film5 = Movie (tytul = "Szklana pułapka cz.2", rok_wydania ="2002", gatunek="Triller", liczba_odtworzen = 0)

serial = Series(tytul ="Dzień z zycia Rekina" , rok_wydania="2020", gatunek="Przyrodniczy", numer_odcinka = int(4), numer_sezonu = int(2), liczba_odtworzen = 0)
serial1= Series(tytul ="Przygody Bociana Bogdana" , rok_wydania="2018", gatunek="Familijny", numer_odcinka = int(6), numer_sezonu = int(1), liczba_odtworzen = 0)
serial2= Series(tytul ="Lupin" , rok_wydania="2022", gatunek="Triller", numer_odcinka = int(6), numer_sezonu = int(1), liczba_odtworzen = 0)
serial3= Series(tytul ="Zaczarowany Ogród" , rok_wydania="1995", gatunek="Familijny", numer_odcinka = int(6), numer_sezonu = int(1), liczba_odtworzen = 0)


biblioteka_film = [film, film1, film2, film3, film4, film5]
biblioteka_serial = [serial, serial1, serial2, serial3]
biblioteka = [*biblioteka_film , *biblioteka_serial]

def get_movies():
    print("Sortowanie tytułów filmów alfabetycznie")
    return [movie for movie in biblioteka if not isinstance(movie, Series)]
        
def get_series():
    print("Sortowanie tytułów seriali alfabetycznie")
    return [movie for movie in biblioteka if isinstance(movie, Series)]
    
def search(poszukiwany_tytul):
    for movie in biblioteka:
        if movie.tytul == poszukiwany_tytul:
            return movie

def generate_views():
    id_rnd = randrange(len(biblioteka))
    biblioteka[id_rnd].play(step=randrange(100) + 1)

def run_generate():
    for i in range(10):
        generate_views()

def top_titles():
    print(f"Najpopularniejsze filmy i seriale dnia {dzis}")
    return [sorted(biblioteka, key=lambda Movie: Movie.liczba_odtworzen)]
    
print(search("Lupin"))
generate_views()
get_movies()
get_series()
print(top_titles())







# def get_movies():
#     print("Sortowanie tytułów filmów alfabetycznie")
#     by_tytul = sorted(biblioteka_film, key=lambda Movies: Movies.tytul)
#     for a in by_tytul:
#         print (a.tytul, a.rok_wydania)


# def get_series():
#     print("Sortowanie tytułów seriali alfabetycznie")
#     by_tytul = sorted(biblioteka_serial, key=lambda Series: Series.tytul)
#     for a in by_tytul:
#         print (a.tytul, a.rok_wydania)






