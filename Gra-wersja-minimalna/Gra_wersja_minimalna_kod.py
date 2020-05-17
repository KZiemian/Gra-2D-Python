#!/usr/bin/python3


"""Napisał: Kamil Ziemian
Na podstawie kursu H. S. Kinsleya "Game Development in Python 3 With
PyGame", z jego kanału YouTubwego sentdex:
https://www.youtube.com/watch?v=ujOTNg17LjI&index=1&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO
Grafiki "Bohater.png" i "Tlo.png": Barbara Chudzik
Korekta kodu: Gabriela Kaczka, Filip Ziętkowski


Na kanale Kinsleya jest dużo innych cennych materiałów, można tam również
znaleźć dodatkową pomoc w instalacji PyGame'a na Windowsie."""


import pygame
pygame.init()


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)


display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))


pygame.display.set_caption("Gra w fizyke")

clock = pygame.time.Clock()

frames_per_second = 30


hero_img = pygame.image.load("Bohater.png")


background_img = pygame.image.load("Tlo.png")


hero_width = 140
hero_height = 100


def hero(x, y):
    """Funkcja która rysuje ,,bohatera'' w zdanym punkcie.

    ,,Bohatera'' reprezentuje obiekt hero_img, do którego załadowaliśmy
    obrazek przedstawiający go. Sposób rysowania jest następujący:
    lewy górny róg obrazka znajdzie się w punkcie o współrzędnych x, y."""

    game_display.blit(hero_img, (x, y))


delta_space = 5


x_max = (display_width - hero_width)


def game_loop():
    """Gra to jedna wielka pętla while, każdy przebieg ciała tej pętli to
    jednak klatka (frame) gry.

    x i y to zmienne rządzące położeniem ,,bohatera'' na ekranie.
    W linijce poniżej określamy początkowe położenie bohatera.

    Położenie to zostało dobrane metodą prób i błędów, tak by przy domyślnych
    ustawieniach grafiki, ,,bohater'' pojawił się w dobrym miejscu."""
    x = (display_width * 0.45)
    y = (display_height * 0.67)

    delta_x = 0
    delta_y = 0

    play_game = True

    while play_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_game = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    delta_x = -delta_space

                if event.key == pygame.K_RIGHT:
                    delta_x = delta_space

            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT) \
                   or (event.key == pygame.K_RIGHT):

                    delta_x = 0

        x += delta_x
        y += delta_y

        if x <= 0:
            delta_x = 0.0
            x = 0.0
        elif x >= x_max:
            delta_x = 0.0
            x = x_max
        # game_display.fill(white) # W pamięci komputera ,,wypełniamy'' tło
        # kolorem białym.
        game_display.blit(background_img, (0, 0))  # W pamięci komputera
        # rysujemy tło gry.

        hero(x, y)

        pygame.display.update()

        clock.tick(frames_per_second)


game_loop()


pygame.quit()
quit()
