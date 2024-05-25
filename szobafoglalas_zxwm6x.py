from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Szoba(ABC):
    def __init__(self, szobaszam):
        self.szobaszam = szobaszam

    @abstractmethod
    def ar(self):
        pass

class EgyagyasSzoba(Szoba):
    def ar(self):
        return 15000

class KetagyasSzoba(Szoba):
    def ar(self):
        return 25000

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, datum, napok):
        self.szoba = szoba
        self.datum = datum
        self.napok = napok

    def get_ar(self):
        szoba_ar = self.szoba.ar()
        foglalas_ar = szoba_ar * self.napok
        print(f"A foglalás ára: {foglalas_ar} HUF (Szoba ára: {szoba_ar} HUF/éjszaka)")
        return foglalas_ar

    def __repr__(self):
        return f"Szoba: {self.szoba.szobaszam}, Dátum: {self.datum}, Napok: {self.napok}"

def foglalas_letrehozasa(szalloda, foglalasok):
    szoba_szam = input("Kérem a szoba számát: ")
    datum_str = input("Kérem a foglalás kezdő dátumát (ÉÉÉÉ-HH-NN): ")
    datum = datetime.strptime(datum_str, "%Y-%m-%d")
    napok = int(input("Kérem a foglalás napjainak számát: "))

    szoba = next((sz for sz in szalloda.szobak if sz.szobaszam == szoba_szam), None)
    if not szoba:
        print("Hiba: A megadott szoba nem létezik.")
        return

    if datum < datetime.now():
        print("Hiba: A foglalás kezdő dátuma nem lehet a múltban.")
        return

    if napok < 1:
        print("Hiba: A foglalásnak legalább egy napra kell szólnia.")
        return

    foglalt_szobak = [f.szoba for f in foglalasok if f.datum <= datum <= f.datum + timedelta(days=f.napok)]
    if szoba in foglalt_szobak:
        print("Hiba: A megadott szoba már foglalt ezen a napon.")
        return

    foglalas = Foglalas(szoba, datum, napok)
    foglalasok.append(foglalas)
    foglalas.get_ar()
    print("Foglalás sikeresen létrehozva.")

def foglalas_lemondasa(foglalasok):
    print("Foglalások:")
    for i, foglalas in enumerate(foglalasok):
        print(f"{i+1}. {foglalas}")

    try:
        foglalas_index = int(input("Kérem a lemondandó foglalás sorszámát: "))
        if foglalas_index < 1 or foglalas_index > len(foglalasok):
            raise ValueError()
    except ValueError:
        print("Hiba: Érvénytelen sorszám.")
        return

    foglalasok.pop(foglalas_index - 1)
    print("Foglalás sikeresen lemondva.")

def foglalasok_listazasa(foglalasok):
    print("Foglalások:")
    for foglalas in foglalasok:
        print(f"- {foglalas}")

def main():
    # Szálloda létrehozása
    szalloda = Szalloda("Kényelmes Szálloda")

    # Szobák létrehozása és hozzáadása a szállodához
    egyagyas1 = EgyagyasSzoba("101")
    egyagyas2 = EgyagyasSzoba("102")
    egyagyas3 = EgyagyasSzoba("103")
    egyagyas4 = EgyagyasSzoba("104")
    egyagyas5 = EgyagyasSzoba("105")
    ketagyas1 = KetagyasSzoba("201")
    ketagyas2 = KetagyasSzoba("202")
    ketagyas3 = KetagyasSzoba("203")
    ketagyas4 = KetagyasSzoba("204")
    ketagyas5 = KetagyasSzoba("205")
    szalloda.add_szoba(egyagyas1)
    szalloda.add_szoba(egyagyas2)
    szalloda.add_szoba(egyagyas3)
    szalloda.add_szoba(egyagyas4)
    szalloda.add_szoba(egyagyas5)
    szalloda.add_szoba(ketagyas1)
    szalloda.add_szoba(ketagyas2)
    szalloda.add_szoba(ketagyas3)
    szalloda.add_szoba(ketagyas4)
    szalloda.add_szoba(ketagyas5)

    # Foglalások létrehozása
    foglalasok = [
        Foglalas(egyagyas1, datetime(2024, 4, 21), 2),
        Foglalas(egyagyas2, datetime(2024, 4, 22), 3),
        Foglalas(ketagyas1, datetime(2024, 4, 23), 1),
        Foglalas(ketagyas2, datetime(2024, 4, 24), 4),
        Foglalas(ketagyas3, datetime(2024, 6, 25), 2),
        Foglalas(ketagyas4, datetime(2024, 5, 19), 9),
        Foglalas(egyagyas5, datetime(2024, 4, 26), 2)
    ]

    while True:
        print("\nVálassz műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Művelet kiválasztása (1/2/3/4): ")

        if valasztas == "1":
            foglalas_letrehozasa(szalloda, foglalasok)
        elif valasztas == "2":
            foglalas_lemondasa(foglalasok)
        elif valasztas == "3":
            foglalasok_listazasa(foglalasok)
        elif valasztas == "4":
            print("Kilépés...")
            break
        else:
            print("Hiba: Érvénytelen művelet.")

if __name__ == "__main__":
    main()
