from colorama import Fore, Style, init
import js2py
import sys
from pathlib import Path

init()

def setcolor(color):
    color = color.upper()
    return getattr(Fore, color)

def ripristina():
    return Style.RESET_ALL

file = sys.argv[1]

with open(Path(file), "r", encoding="utf-8") as f:
    filec = f.read()

try:
    risultato = js2py.eval_js(filec)
except Exception as e:
    print(setcolor("RED") + "Errore nell'esecuzione di:" + ripristina())
    print("   " + file)
    print("Messaggio Errore:")
    print("    " + str(e))
    print(ripristina())
else:
    print(risultato)
