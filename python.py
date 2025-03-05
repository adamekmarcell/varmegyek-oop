class Megye:
    def __init__(self, nev, szekhely, terulet, varosok_szama, nepsuruseg, lakossag, regio):
        self.nev = nev
        self.szekhely = szekhely
        self.terulet = int(terulet)
        self.varosok_szama = int(varosok_szama)
        self.nepsuruseg = int(nepsuruseg)
        self.lakossag = int(lakossag)
        self.regio = regio

class Orszag:
    def __init__(self, megyek):
        self.megyek = megyek

    def legnepesebb_megye(self):
        return max(self.megyek, key=lambda m: m.lakossag)
    
    def legkisebb_megye(self):
        return min(self.megyek, key=lambda m: m.terulet)
    
    def összes_megye_adat(self):
        for megye in self.megyek:
            print(f"Megye neve: {megye.nev}, székhelye: {megye.szekhely}, területe: {megye.terulet}m^2, városok száma: {megye.varosok_szama} db, népsűrűség: {megye.nepsuruseg} fő/km^2, lakosság: {megye.lakossag} fő, régió: {megye.regio}")

    def atlag_nepesseg(self):
        ossz_nepesseg = sum(m.lakossag for m in self.megyek) 
        return ossz_nepesseg / len(self.megyek)
    
    def összes_megye_szekhely(self):
        for megye in self.megyek:
            print(f"Megye neve: {megye.nev}, székhelye: {megye.szekhely}.")


with open("vármegyék.csv","r", encoding="utf-8") as fajl:
    sorok = fajl.readlines()

megyek = [Megye(*sor.strip().split(",")) for sor in sorok[1:]]

magyarorszag = Orszag(megyek)

print("Összes megyének a neve: ")
magyarorszag.összes_megye_adat()

print("Legnépesebb megye", magyarorszag.legnepesebb_megye().nev)
print("Legkisebb területű megye", magyarorszag.legkisebb_megye().nev)
print("Magyarország átlag népessége megyénként: ", int(magyarorszag.atlag_nepesseg()))

print("Minden megye székhelye: ")
magyarorszag.összes_megye_szekhely()



# Csoportosítsd a megyéket régiók szerint, és írd ki, hogy mely régióban hány megye található.
# Írj egy programot, amely megtalálja azt a megyét, amelyik a legtöbb várossal rendelkezik.
# Rendezd a megyéket lakosság szerint csökkenő sorrendben, és írd ki az első 5-öt.
# Írj egy programot, amely kiválogatja és kiírja azokat a megyéket, ahol a népsűrűség nagyobb, mint 100 fő/km².
# Kérj be a felhasználótól egy megye nevét, és írd ki a megye adatait (székhely, terület, lakosság stb.).
# Legkevésbé népes megye keresése
# Legnagyobb területű megye
# Városok átlagos száma megyénként
# Régiók összlakossága
# Utóbbit exportáld ki egy regio_osszlakossag.txt nevű fájlba áttekinthetően

