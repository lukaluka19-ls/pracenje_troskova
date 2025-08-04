import argparse
from podaci import *

parser = argparse.ArgumentParser(opis='Pracenje Troskova CLI')

subparsers = parser.add_subparsers(dest = 'command')

#Dodavanje
add_parser = subparsers.add_parser('add')
add_parser.add_argument('--opis',required=True)
add_parser.add_argument('--kolicina',type = float, required=True)
add_parser.add_argument('--kategorija',default='Other')

#lista