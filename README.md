<div align="center">

  <img width="100" height="100" alt="Snode logo" src="https://github.com/user-attachments/assets/8e9f966b-9a49-4b22-b15f-ed5dec2d8b95" />

  # Snode


</div>

---

## Cos'è Snode?

Snode è un piccolo runner di JavaScript fatto in Python e Dromi.

---

## Ma perché esiste Snode?

Snode nasce come progetto sperimentale per esplorare come si possa creare un runtime JavaScript simile a Node.js utilizzando Python.

L’idea è:

- capire come funziona un runtime JS in pratica
- costruire un sistema di esecuzione semplice con Js2Py
- sperimentare un sistema di moduli (`require`)
- creare un package manager leggero (SPM)

👉 Snode non vuole sostituire Node.js, ma essere un progetto educativo e creativo per imparare come funzionano i runtime e gli ecosistemi di sviluppo.


---

## Setup Iniziale

Verifica di aver installato Python:

```bash
python
```

e poi esci dalla REPL di Python:

```shellOutput
Python 3.12.0 on MySYS x64 - Compiled 05.12.2020 15:10
Type "license", "copyright", "help" for more information.
>>>exit()
```

ora clona il Repo:

```bash
git clone https://github.com/dromilang/snode.git
```

e fai i comandi:

```bash
cd snode
pip install -r requirements.txt
```

poi:

```bash
python snode.py
```
 apparirá la REPL di Snode:

```shellOutput
Snode 1.0.0 Alpha 0
Digita .help per più informazioni.
>
```
 
qui potrai digitate i comandi JS:

```shellOutput
>var addizione = 2 + 4
>addizione
6
> console.log("Ciao mondo Snode!")
Ciao mondo Snode!
```
