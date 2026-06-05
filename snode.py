from colorama import Fore, Style, init
import js2py

init()

def setcolor(color):
    color = color.upper()
    return getattr(Fore, color)

def ripristina():
    return Style.RESET_ALL

while True:
    comando = input("> ")

    if comando.startswith("."):
        if comando == ".help":
            print(".help -> Questo menu")
            print(".about -> About Snode")
            print(".license -> Licenza")

        elif comando == ".about":
            print("Snode è una piccola copia di Node.js fatta in Python e Dromi.")
            print(setcolor("GREEN") + "Suggerimento: " + ripristina() +
                  " Questa è solo la REPL. Esplora altro negli altri file!")

        elif comando == ".license":
            print("Snode è sotto la licenza Apache 2.0: guarda il File LICENSE per più informazioni.")

        else:
            print(setcolor("RED") + "Errore: il comando che inizia con . non è stato trovato." + ripristina())
            print(setcolor("GREEN") + "Suggerimento: " + ripristina() +
                  " I comandi predefiniti della REPL iniziano con '.'")

    else:
        try:
            risultato = js2py.eval_js(comando)
        except Exception as e:
            print(setcolor("RED") + "Errore nell'esecuzione di:" + ripristina())
            print("   " + comando)
            print("Messaggio Errore:")
            print("    " + str(e))
        else:
            print(risultato)
