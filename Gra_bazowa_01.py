#!/usr/bin/python
#-*- coding: utf-8 -*-

u"""Autor: Kamil Ziemian
Na podstawie kursu H. S. Kinsleya ,,Game Development in Python 3 With
PyGame'', z jego kanału YouTubwego sentdex:
https://www.youtube.com/watch?v=ujOTNg17LjI&index=1&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO
Poprawki: Gabriela Kaczka, Filip Ziętkowski


Na kanale Kinsleya jest dużo innych cennych materiałów, można tam również
znaleźć dodatkową pomoc w instalacji PyGame'a na Windowsie."""


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
u"""Każdy dobry pomysł na usprawnienie tej gry, będzie pozytywnie wpływał
na ocenę. Skrypt nie jest zapewne zbyt zoptymalizowany, pisany był z myślą
o możliwe szybkim przejściu do fizyki, a nie stworzeniu eleganckiego kodu."""
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 19 kwietnia 2017 roku, to dalej jest prawdą.


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
u"""W tej wersji gry sterujemy strzałkami w lewo i w prawo."""
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



######################################################################


u"""Skrypt ,,Gra_bazowa_1.py'' zawiera minimalną ilość kodu który pozwala
grze działać i odpowiadać na działania gracza. Jest ona jednak nudna,
bo nic się nie dzieje.

Każda kolejna wersja tego pliku zawiera jedną, czasem tylko kilkulinijkową,
ale ważną zmianę w programie. Plik ,,Gra_punkt_mater.py'' zawiera pełen kod
na którym będziemy bazowali w pierwszej podejściu do fizyki w grach.
(Skoro Państwo to czytają, oznacza to, że te skrypty zostały wybrane,
jako domyślne środowisko.) Takie rozczłonkowanie kodu źródłowego zostało
dokonane świadomie, aby maksymalnie ograniczyć zagubienie jakiego
doświadcza wielu ludzi (ja go doświadczam) patrząc po raz pierwszy
w kilkaset linii programu.

Niektórzy z Państwa mogą uważać, że moich komentarzy jest za dużo,
przez co ciężko jest ten kod czytać, jest to o tyle prawda, że przytłaczająca
część tych plików stanowią opisy, wyjaśnienia, uwagi, etc.

Proszę wziąć jednak pod uwagę następujący fakt: na tych zajęciach zawsze są
osoby, które nie potrafią same ani napisać ani zrozumieć kodu w Pythonie.
Moje komentarze są skierowane właśnie dla takich osób, aby miały możliwie
dobre materiały do nauki. Ci którzy dobrze znają programowania mogą napisać
program samodzielnie, bądź skorzystać z pliku Gra_bazowa_01_kod.py.

Wiem, że istnieje standard pisania notek dokumentacyjnych Pythona,
choć zwykle muszę sięgać do PEP 257. Niestety w tych skryptach się do niego
nie stosuje. Nie wiem bowiem jako pogodzić te standardy, z celem
pedagogicznym jakiem mają one służyć. Wszystkie bowiem te komentarze mają
być materiałem do nauki dla osoby, która będzie chciała zrozumieć działanie
kod źródłowego, nie zaś tej która będzie potrzebowała uzyskać z poziomu
powłoki czy programu informacje o danej funkcji czy klasie.

Mam nadzieję, że będzie się je Państwu dobrze czytało."""



######################################################################
# Importowanie modułów/bibliotek

import pygame # Główny moduł Pythona z którego będziemy korzystać
# (zaskakujące). Pozwala w łatwy sposób wyświetlać grafikę 2D.


######################################################################



pygame.init()
u"""Z pewnych względów technicznych musimy zaincjalizować PyGame
zanim będziemy mogli z niego korzystać. W ten sposób po prostu aktywujemy
jego zawartość. Jest to jedyny moduł Pythona jaki znam, który wymaga
takiego postępowania."""



##############################
# Kolory

u"""PyGame, z nieznanych mi powodów, nie definiuje palety domyślnych kolorów,
za to pozwala je samemu ustawić. Kolor w PyGame reprezentuje trójelementowa
krotka (ang. tuple), która zawiera liczby od 0 do 255. Element pierwszy
odpowiada natężenie koloru czerwonego (R), drugi zielonego (G),
trzeci niebieskiego (B)."""

black = (0, 0, 0) # Nie ma nic, ciemno.
white = (255, 255, 255) # Kolor biały to suma wszystkich kolorów.
red = (255, 0, 0)


##############################
# Parametry wyświetlanego obrazu

display_width = 800 # Wysokość i szerokość okienka gry.
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))
u"""Tworzymy okienko w którym będzie wyświetlana gra. Jako argument podajemy
dwuelementowa krotkę (ang. tuple), zawierającą rozmiar/rozdzielczość
okienka, które zostanie utworzone."""

pygame.display.set_caption('Gra w fizyke') # Ustawianie nazwy okna z grą.



##############################
# Ustawienie częstości odświeżania obrazu

clock = pygame.time.Clock() # Tworzy zegar, który zlicza ilość klatek
# na sekundę.

frames_per_second = 30 # Zmienna definiująca ilość klatek na sekundę,
# lub po ,,polsku'' fpsów.


##############################
# Ładowanie obrazków dla gry

hero_img = pygame.image.load('Bohater.png')
u"""Ładujemy do gry obrazek przedstawiający ,,bohatera'', który znajduje się
 w pliku Bohater.png. Obrazek ma być w tym samym katalogu/folderze, inaczej
 trzeba będzie podawać ścieżkę dostępu. Zmieniając nazwę pliku zawierającego
 rysunek, proszę pamiętać, że musi się być zawarta w cudzysłowie.
 (To wszystko można zrobić w bardziej wyrafinowany sposób, ale ten komentarz
 został na pisany dla osób, które nie orientują się w tym wszystkim.)"""

background_img = pygame.image.load('Tlo.png') # Ładujemy tło gry.


def hero(x, y):
    u"""Funkcja która rysuje ,,bohatera'' w zdanym punkcie.

    ,,Bohatera'' reprezentuje obiekt hero_img, do którego załadowaliśmy
    obrazek przedstawiający go. Sposób rysowania jest następujący:
    lewy górny róg obrazka znajdzie się w punkcie o współrzędnych x, y."""
    
    # Ważne! Ważne! Ważne! Ważne! Ważne! Ważne! Ważne! Ważne! Ważne!
    u"""PyGame używa następującego układu współrzędnych. Położenie (0, 0)
    to lewy górny róg ekranu. Wraz ze wzrostem x idziemy w prawo,
    a ze wzrostem y, w dół."""
    
    game_display.blit(hero_img, (x, y)) # Strasznie dużo pisania, a funkcja
    # bardzo krótka.



######################################################################
# Stałe o różnym charakterze używane w grze

delta_space = 5
u"""Pomocnicza zmienna do kontroli prędkości przesuwania się ,,bohatera''.
Jeśli dobrze rozumiem jednostką jest jeden piksel, jednak jeśli tak jest,
to nie wiem co dokładnie PyGame robi z ułamkową odległością w pikselach."""


    
######################################################################
# Główna pętla gry

def game_loop():
    u"""Gra to jedna wielka pętla while, każdy przebieg ciała tej pętli to
    jednak klatka (frame) gry."""

    u"""x i y to zmienne rządzące położeniem ,,bohatera'' na ekranie.
    W linijce poniżej określamy początkowe położenie bohatera.

    Położenie to zostało dobrane metodą prób i błędów, tak by przy domyślnych
    ustawieniach grafiki, ,,bohater'' pojawił się w dobrym miejscu."""
    x = (display_width * 0.45)
    y = (display_height * 0.67)

    u"""Proszę Państwa, nie jestem game developerem, za to przez wiele lat
    studiowałem fizykę. Z tego powodu nie wiem jakie są standardy nazywania
    zmiennych i funkcji w branży produkcji gier komputerowych, za to
    przywykłem do tych stosowanych w naukach fizycznych oraz matematyce
    i ich właśnie używam. Jak powiedziałem, nie wiem czy są dobre jeśli
    chodzi o standardy gamedevu, ale mają tę zaletę, że zwykle pozostają się
    w zgodzie z oznaczeniami wzorów, które zwykle się Państwu wygooglują."""

    u"""Animację ruchu w grze tworzymy, poprzez rysowanie obiektów w każdej
    klatce w innym miejscu. A w jakim miejscu mamy jej narysować? To zależy
    od decyzji gracza i praw fizyki, o czym jest cały ten kurs;)."""

    delta_x = 0
    u"""Zmienna do przesuwania ,,bohater'' w kierunku osi x. Pozycja
    ,,bohatera'' zmieni się o tyle pikseli (jeśli dobrze rozumiem)
    w następnej klatce animacji."""
    delta_y = 0 


    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Ważne Ważne Ważne Ważne Ważne Ważne Ważne Ważne Ważne Ważne Ważne

    play_game = True # W grę gramy, dopóki ta zmienna ma wartość True.
    # Całkiem logiczne.

    ##############################
    # Kluczowa pętla gry.
    while play_game:
        u"""Jak napisano wyżej, gra to jedna wielka pętla while,
        każdy przebieg ciała tej pętli to jednak klatka (frame) gry."""

        ##############################
        # Pętla sprawdzająca wydarzenia.
        
        for event in pygame.event.get():
            u"""PyGame cały czas zbiera ogromną ilość danych o działaniu
            gracza, pygame.event.get() to metoda która zwraca listę
            wszystkich tych wydarzeń (eventów) jakie rozegrały się
            w ciągu ostatniej klatki. Event jest obiektem, posiada więc
            różne metody i atrybuty.
            
            Najprawdopodobniej zbiera on wszystkie wydarzenia, od czasu
            ostatniego użycia metody event.get(), ale jeszcze tego
            nie sprawdziłem. Najważniejsze, że nie zdarzyło mi się,
            by jakieś wydarzenie było przez tę metodę przegapione.
            
            Przebiegamy wiec tę listę za pomocą pętli for, sprawdzamy
            wszystkie rzeczy jakie zrobił użytkownik, szukając czy któreś
            z nich nie powinno wpłynąć na grę."""

            # print event
            # Dla Pythona 2
            # print(event)
            # Dla Pythona 3
            u"""Możemy wypisać listę zdarzeń z danej klatki w powłoce Pythona
            w której uruchomiliśmy ten skrypt. Warto choć raz zobaczyć
            to samemu."""



            ##############################
            # Przechwytywnie wydarzeń.
            
            if event.type == pygame.QUIT:
                u"""Event jest obiektem, posiada jak swój atrybut swój typ.
                Typ ten pobieramy przez event.type.

                PyGame mam wbudowaną ogromną ilość typów wydarzeń,
                analogiczny do typów zmiennych. event.type zwraca typ
                elementu event, zaś pygame.QUIT oznacza naciśniecie X
                w prawym górnym rogu okna.

                Jeśli usuniemy ten warunek, kliknięcie w tego X w prawym
                górnym rogu nic nie da."""
                
                play_game = False # Powinno być jasne, czemu to kończy grę.


            if event.type == pygame.KEYDOWN:
                u"""Sprawdzamy czy jakiś klawisz został WCIŚNIĘTY. Jeżeli
                WCIŚNIEMY jakiś klawisz i go przytrzymamy, to otrzymujemy
                tylko jedno wydarzenie pygame.KEYDOWN, w tej klatce w której
                NACISNĘLIŚMY klawisz. Aby uzyskać ten sygnał ponownie,
                należy WCISNĄĆ jakiś inny klawisz.

                Jeżeli więc wciśniemy klawisz strzałki w lewo i przytrzymamy,
                instrukcja warunkowa zostanie wykonana w pierwszej przebiegu
                pętli po wciśnięciu tego klawisza i w żadnej innej.

                Ta własność wraz z resztą kodu prowadzi do powstania buga.
                Jeśli wciśniemy i będziemy trzymać strzałkę w lewo,
                następnie wciśniemy i puścimy strzałkę w prawo, zatrzymamy
                ,,bohatera''.

                Dlaczego tego nie poprawiłem? Z kilku powodów.
                Najważniejszym powodem była chęć pokazania, jakie niewinne
                konstrukcje programistyczne mogą prowadzić do błędów w grach.
                Po drugie, przemyślenie tego problemu pomogło mi bardzo
                w zrozumieniu działania tej gry. Mam nadzieję, że Państwu
                też pomoże."""


                ##############################
                # Skoro wiemy, że jakiś klawisz jest wciśnięty, sprawdźmy,
                # czy coś robi.
                
                if event.key == pygame.K_LEFT:
                    u"""Sprawdzamy który klawisz został wciśnięty.
                    Jeśli jest to strzałka w lewo, to przesuniemy się
                    o -delta_space = -5."""
                    delta_x = -delta_space

                if event.key == pygame.K_RIGHT:
                    delta_x = delta_space


            ##############################
            if event.type == pygame.KEYUP:
                u"""Sprawdzamy czy puściliśmy jakiś klawisz."""
                if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT):
                    u"""Jeśli puścimy strzałkę w lewo lub prawo, to musimy
                    zastopować ruch w kierunku x."""
                    
                    delta_x = 0


        ###################################################################
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # Ważne Ważne Ważne Ważne Ważne Ważne Ważne Ważne Ważne Ważne Ważne

        # To jest fragment kodu, w którym zwykle będziemy programować fizykę.


        u"""Fizyka w grach komputerowych polega na tym, żeby obiekty w grze
        wyświetlać w miejscach, które wynika z działań gracza i przyjętych
        w grze praw fizyki. Fizyka ta może być Hollywoodzka.

        Fizyka w tej grze sprowadza się do tego, jak obliczyć współrzędne
        położenia ,,bohatera'' x i y. Sens całego kursu dla tej gry,
        to w tym momencie policzenie x i y na podstawie działań gracza
        oraz przyjętych praw fizyki.

        Te obliczenia to często dosłownie kilka linijek kodu Pythona."""

        x += delta_x # Zmieniamy położenie ,,bohatera'' w kierunku x
        # o wielkość delta_x.
        y += delta_y

        u"""W tym momencie taki kod jest zupełnie wystarczający:
        x_(n + 1) = x_n + delta_x,
        y_(n + 1) = y_n + delta_y.
        Przy bardziej zaawansowanych metodach, może być wymagany bardziej
        skomplikowany kod."""



        ##############################
        # Wyświetlanie grafiki
        
        u"""Jest kilka powodów dla których należy najpierw wszystko policzyć,
        utworzyć dane numeryczne wszystkich obiektów graficznych, a dopiero
        potem narysować nową klatkę animacji.

        1) Kiedy ostatni raz sprawdzałem, najwięcej mocy obliczeniowej
        pochłania nie utworzenie numerycznych danych obiektów graficznych
        w pamięci, lecz właśnie narysowanie ich na ekranie. Brzmi to
        rozsądnie, lecz muszę się w tej materii upewnić.

        2) Załóżmy, że wedle obliczeń dwa obiekty powinny znajdować się
        w tym samym miejscu, np. ciało przenika przez ścianę. Stosowane
        algorytmy numeryczne często prowadzą do takiej sytuacji. Czego
        jednak gracz nie widzi, to nie jest bugiem. Dlatego jeżeli
        wykryjemy to zdarzenie przed wyświetleniem klatki na ekranie,
        to możemy je poprawić ręcznie i pokazać animację pozbawiony błędu.
        
        Dlatego najpierw przechwytujemy działanie graczy, wykonujemy
        obliczenia AI, fizyki, oświetlenia, dokonujemy poprawek etc.,
        w wyniku których mamy gotowy zestaw danych i dopiero wtedy
        go wyświetlamy. Nawet utworzenie danych odnośnie obiektów graficznych
        lepiej jest zrobić przed załadowaniem wszystkiego na ekran."""

        # gameDisplay.fill(white) # W pamięci komputera ,,wypełniamy'' tło
        # kolorem białym.
        game_display.blit(background_img, (0, 0)) # W pamięci komputera
        # rysujemy tło gry.

        hero(x, y) # Wciąż w pamięci komputera rysujemy ,,bohatera''.

        u"""W tym momencie tło i ,,bohater'' są ,,narysowani'' W PAMIĘCI
        komputera, ale nie są wyświetlani na ekranie komputera. Dopiero
        poniższa komenda to robi."""

        pygame.display.update() # Upgraduje całe okno, czyli rysujemy
        # je od nowa na podstawie danych z powyższej części pętli.

        clock.tick(frames_per_second) # Ilość klatek animacji na sekundę,
        # czyli ile razy zegar ma tyknąć w tym czasie.



##################################################



game_loop() # Uruchamiamy grę, wywołując funkcję game_loop. Jedna gra
# to jedno wywołanie tej funkcji.

pygame.quit()
u"""PyGame tak jak został włączony (zainicjalizowany),
# musi zostać odpowiednio wyłączony. Nie znam drugiego modułu Pythona,
# gdzie trzeba to robić."""

quit() # Wychodzimy z Pythona. Ta opcja może się przydać.
