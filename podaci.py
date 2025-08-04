import json
import os
from datetime import datetime
import csv

DATA_FILE = 'data.json'

# Ucitavanje podataka iz JSON fajla
def ucitaj_podatke():
    if not os.path.exists(DATA_FILE):
        return {"troskovi": [], "budzet": {}}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Snimanje podataka u JSON fajl
def sacuvaj_podatke(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

# Dodavanje novog troska
def dodaj_trosak(opis, kolicina, kategorija):
    data = ucitaj_podatke()
    troskovi_id = max([e['id'] for e in data['troskovi']] + [0]) + 1
    trosak = {
        "id": troskovi_id,
        "datum": datetime.now().strftime('%Y-%m-%d'),
        "opis": opis,
        "kolicina": float(kolicina),
        "kategorija": kategorija,
    }
    data['troskovi'].append(trosak)
    sacuvaj_podatke(data)
    return troskovi_id

# Prikaz svih troskova
def lista_troskova():
    return ucitaj_podatke()['troskovi']

# Brisanje troska po ID-u
def obrisi_trosak(trosak_id):
    data = ucitaj_podatke()
    data['troskovi'] = [e for e in data['troskovi'] if e['id'] != trosak_id]
    sacuvaj_podatke(data)

# Azuriranje troska
def azuriraj_troskove(trosak_id, opis=None, kolicina=None, kategorija=None):
    data = ucitaj_podatke()
    for e in data['troskovi']:
        if e['id'] == trosak_id:
            if opis:
                e['opis'] = opis
            if kolicina:
                e['kolicina'] = float(kolicina)
            if kategorija:
                e['kategorija'] = kategorija
            break
    sacuvaj_podatke(data)

# Racunanje sume troskova, opcionalno po mesecu
def sumarizacija(month=None):
    data = ucitaj_podatke()
    troskovi = data['troskovi']
    if month:
        troskovi = [
            e for e in troskovi
            if e['datum'].startswith(f"{datetime.now().year}-{str(month).zfill(2)}")
        ]
    return sum(e['kolicina'] for e in troskovi)

# Postavljanje budzeta za mesec
def postavi_budzet(month, kolicina):
    data = ucitaj_podatke()
    kljuc = f"{datetime.now().year}-{str(month).zfill(2)}"
    data['budzet'][kljuc] = float(kolicina)
    sacuvaj_podatke(data)

# Prikaz statusa budzeta
def status_budzet(month):
    data = ucitaj_podatke()
    kljuc = f"{datetime.now().year}-{str(month).zfill(2)}"
    potroseno = sumarizacija(month)
    budzet = data['budzet'].get(kljuc, 0)
    return potroseno, budzet

# Eksport u CSV fajl
def export_to_csv(filename):
    data = ucitaj_podatke()
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["id", "datum", "opis", "kolicina", "kategorija"])
        writer.writeheader()
        writer.writerows(data['troskovi'])

#README
#gpt komentari kod naziva funkcija...
#zfill(2) koristim samo zbog zahtevanja dvoclanog meseca u formatu yyymm...
#ucitavanje,upisivanje,crud,sumarizacija,postavljanje,status vezan za budzete, slanje u CSV fajl
#pozivanje funkcija u glavnom fajlu(pracenje_troskova.py)
