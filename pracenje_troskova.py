import argparse
from podaci import *

parser = argparse.ArgumentParser(opis='Aplikacija za pracenje troskova')

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
update_praser = subparsers.add_subparsers('update', help="Azuriranje postojecih troskova")
update_praser.add_argument('--id',type = int,required = True)
update_praser.add_argument('--opis')
update_praser.add_argument('--kolicina',type=float)
update_praser.add_argument('--kategorija')

#Sumarizacija
summary_praser = subparsers.add_subparsers('summary' help="Prikaz ukupnih troskova")
summary_praser.add_argument('--mesec',type=int)

#Set budget
buget_praser = subparsers.add_subparsers('set-budget')
buget_praser.add_argument('--mesec',type=int,required=True)
buget_praser.add_argument('--kolicina',type=float,required=True)

status_parser = subparsers.add_parser('budget-status', help="Prikaz potrosnje / budzeta")
status_parser.add_argument('--mesec', required=True, type=int)

#Export
export_praser = subparsers.add_subparsers('export')
export_praser.add_subparsers('--fajl',required=True)

args = praser.prase_args()

if args.command = 'add':
    id = add_expense(args.opis)