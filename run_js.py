from colorama import Fore, Style, init
import js2py
import sys
from pathlib import Path
from require import require

init()

def setcolor(color):
    return getattr(Fore, color.upper())

def ripristina():
    return Style.RESET_ALL


context = js2py.EvalJs({})

context.require = require


file = sys.argv[1]

with open(Path(file), "r", encoding="utf-8") as f:
    filec = f.read()


try:
    risultato = context.execute(filec)

    if risultato is not None:
        print(risultato)

except Exception as e:
    print(setcolor("RED") + "Errore nell'esecuzione di:" + ripristina())
    print("   " + file)
    print("Messaggio Errore:")
    print("    " + str(e))
    print(ripristina())
