import argparse
from podaci import (
    dodaj_trosak,
    lista_troskova,
    obrisi_trosak,
    azuriraj_troskove,
    sumarizacija,
    postavi_budzet,
    status_budzet,
    export_to_csv
)

parser = argparse.ArgumentParser(description="Aplikacija za praćenje troškova")

subparsers = parser.add_subparsers(dest = 'command')

#help komanda opisuje samo cemu sluzi komanda nema funkciju/samo kada se funckija bude pozvala bice ispisan help kao !explanation!

#dodavanje
add_parser = subparsers.add_parser('add', help="Dodaj novi trošak")
add_parser.add_argument('--opis', required=True)
add_parser.add_argument('--kolicina', required=True, type=float)
add_parser.add_argument('--kategorija', default='Ostalo')

#lista
subparsers.add_parser('list', help="Prikaži sve troškove")

#Brisanje
del_parser = subparsers.add_parser('delete', help="Brisanje troska po ID-ju")
del_parser.add_argument('--id', required=True, type=int)

#Azuriranje
update_praser = subparsers.add_parser('update', help="Azuriranje postojecih troskova")
update_praser.add_argument('--id',type = int,required = True)
update_praser.add_argument('--opis')
update_praser.add_argument('--kolicina',type=float)
update_praser.add_argument('--kategorija')

#Sumarizacija
summary_praser = subparsers.add_parser('summary',help="Prikaz ukupnih troskova")
summary_praser.add_argument('--mesec',type=int)

#podesavanje budzeta
buget_praser = subparsers.add_parser('set-budget')
buget_praser.add_argument('--mesec',type=int,required=True)
buget_praser.add_argument('--kolicina',type=float,required=True)

status_parser = subparsers.add_parser('budget-status', help="Prikaz potrosnje / budzeta")
status_parser.add_argument('--mesec', required=True, type=int)

#Export
export_praser = subparsers.add_parser('export')
export_praser.add_argument('--fajl',required=True)

args = parser.parse_args()

if args.command == 'add':
    id = dodaj_trosak(args.opis,args.kolicina,args.kategorija)
    print(f"Trosak dodat (ID: {id})")
elif args.command == 'list':
    troskovi = lista_troskova()
    print(f"ID DATUM OPSI KOLICINA KATEGORIJA")
    for e in troskovi:
        print(f"{e['id']:>3} {e[datum]} {e[opis]:<13} {e[kolicina]:<8.2f} {e[kategorija]}")

elif args.command == 'delete':
    obrisi_trosak(args.id)
    print(f"Trosak je uspesno obrisan!")

elif args.komanda == 'update':
    azuriraj_troskove(args.id, args.opis, args.kolicina, args.kategorija)
    print("Trošak uspešno ažuriran.")

elif args.komanda == 'summary':
    ukupno = sumarizacija(args.mesec)
    if args.mesec:
        print(f"Ukupni troskovi za mesec {args.mesec}: {ukupno} RSD")
    else:
        print(f"Ukupni troskovi: {ukupno} RSD")

elif args.komanda == 'set-budget':
    postavi_budzet(args.mesec, args.kolicina)
    print(f"Budzet za mesec {args.mesec} postavljen na {args.kolicina} RSD")

elif args.komanda == 'budget-status':
    potroseno, budzet = status_budzet(args.mesec)
    print(f"Potroseno je: {potroseno} RSD")
    print(f"Budzet: {budzet} RSD")
    print(f"Preostalo: {budzet - potroseno} RSD")

elif args.komanda == 'export':
    export_to_csv(args.fajl)
    print(f"Podaci izvezeni u fajl: {args.fajl}")

else:
    parser.print_help()
