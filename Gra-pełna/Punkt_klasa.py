#!/usr/bin/python
#-*- coding: utf-8 -*-

class Point(object):

    u"""Instancję klasy tworzymy:
    nazwa_instancji = nazwa_klasy(argumenty).
    Argumenty potrzebne do utworzenia instancji określamy w widocznej
    niżej metodzie __init__."""
    
    def __init__(self, x, y):
        u"""Jest to pierwsza rzecz robiona po utworzeniu instancji
        klasy. Jest to pewien analog, choć niepełny konstruktora w C++.
        Przez nazwę self odwołujemy się do tworzonej instancji klasy
        (choć użycie 'self' jest tylko konwencją nie częścią języka,
        to nie stosowanie się do niej grozi byciem zaatakowanym,
        przez osobę która przeczyta taki kod)."""
        
        self.x = float(x)
        self.y = float(y)
        u"""Aby się dostać do atrybutu (zmiennej instancji),
        piszemy nazwa_instancji.nazwa_atrybutu."""
        

    def move(self, delta_x = 0.0, delta_y = 0.0):
        u"""Definiujemy metodę instancji. Aby jej użyć, należy napisać
        nazwa_instancji.nazwa_metody(argumenty).
        Jeżeli przypiszemy wartość argumentom już w definicja,
        staną się one argumentami domyślnymi."""
        self.x += float(delta_x)
        self.y += float(delta_y)

    def nowa_zmienna(self, x = '?'):
        u"""To głupi przykład."""
        self.nowa_zmienna = x

    def __str__(self):
        u"""Jest to jedna z tzw. metod specjalnych. Dzięki niej napisanie
        w kodzie 'print nazwa_instancji' wypisze string zwracany
        przez tę metodę."""
        return 'Jest x = %-.1f, y = %-.1f' % (self.x, self.y)
    
    u"""Można przeładować np. operator dodawiani +"""
    



if __name__ == '__main__':

    pt1 = Point(0, 0) # Tworzymy dwa punkty.
    pt2 = Point(1.0, 2)

    print 'pt1', pt1
    print 'pt2', pt2
    pt1.move(-2)
    print 'pt1', pt1

    pt2.nowa_zmienna() # To jest wywołanie metody z domyślną wartością.
    print pt2.nowa_zmienna # A to wypisuje nam wartość zmiennej,
    # która ,,przypadkiem'' nazywa się tak jak metoda użyta powyżej.

    pt1.cos = 'A co mi tam'
    print pt1.cos
    u"""Możemy tworzyć nowe atrybuty instancji na bieżąco,
    nie jesteśmy ograniczeni, przez te które pojawiają się
    w definicji klasy."""
    
