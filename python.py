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
    
    def atlag_varos(self):
       ossz_varos = sum(m.varosok_szama for m in self.megyek) 
       return ossz_varos / len(self.megyek)

    def összes_megye_szekhely(self):
        for megye in self.megyek:
            print(f"Megye neve: {megye.nev}, székhelye: {megye.szekhely}.")

    def csoportosit_regiok_szerint(self):
        regionális_megyék = {}
        for megye in self.megyek:
            if megye.regio not in regionális_megyék:
                regionális_megyék[megye.regio] = []
            regionális_megyék[megye.regio].append(megye)


        for regio, megyek in regionális_megyék.items():
            print(f"{regio} régióban {len(megyek)} megye található.")

    def legtobb_varos(self):
        legtobb_varosu_megye = self.megyek[0]

        for megye in self.megyek:
            if megye.varosok_szama > legtobb_varosu_megye.varosok_szama:
                legtobb_varosu_megye = megye

        return legtobb_varosu_megye

    def legnepesebb_lista(self):
        return sorted(self.megyek, key=lambda m: m.lakossag, reverse=True)

    def nagyobb_nepsuruseg(self, limit):
        keresett_megyek = []
        for m in self.megyek:
            if m.nepsuruseg > limit:
                keresett_megyek.append(m)

        return keresett_megyek
    
    def megye_adatok(self, megye_nev):
        for m in self.megyek:
            if m.nev == megye_nev:
                return m
            
        return None
    
    def legkevesbe_nepesebb_megye(self):
        return sorted(self.megyek, key=lambda m: m.lakossag)[0]
    
    def legnagyobb_teruletu_megye(self):
        return sorted(self.megyek, key=lambda m: m.terulet, reverse=True)[0]
        

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

magyarorszag.csoportosit_regiok_szerint()

print("Legtöbb városú megye: ", magyarorszag.legtobb_varos().nev)

print("Legnépesebb 5 megye: ")
for megye in magyarorszag.legnepesebb_lista()[:5]:
    print(f"Megye: {megye.nev}")

print("Megyék ahol nagyobb a népességgel:")
for megye in magyarorszag.nagyobb_nepsuruseg(100):
    print(f"Megye neve: {megye.nev} sűrűség: {megye.nepsuruseg}")

megye_nev_adatok = input("Kérem adja meg a megye nevét: ")
keresett_megye = magyarorszag.megye_adatok(megye_nev_adatok)
if keresett_megye != None:
    print(f"Megye neve: {keresett_megye.nev}, székhelye: {keresett_megye.szekhely}, területe: {keresett_megye.terulet}m^2, városok száma: {keresett_megye.varosok_szama} db, népsűrűség: {keresett_megye.nepsuruseg} fő/km^2, lakosság: {keresett_megye.lakossag} fő, régió: {keresett_megye.regio}")

print("Legkevésé népes megye: ", magyarorszag.legkevesbe_nepesebb_megye().nev)
print("Legnagyobb területű megye: ", magyarorszag.legnagyobb_teruletu_megye().nev)
print("Átlag száma a vároosoknak: ", int(magyarorszag.atlag_varos()))


