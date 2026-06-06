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

Comunque potrete incappare in errori:

```shellOutput
>console.log(ciao)
Errore nell'esecuzione di:
    console.log(ciao)
Messaggio dell'errore:
    The variable 'ciao' is not defined
>
```

---

## SPM

SPM è il gestore di Pacchetti di Snode. Per scaricare un pacchetto, dovrete aggiungere degli url nel file `trusted_indexes.txt`. Il formato è:

```text
nomepacchetto=zips.esempio.it/url/zip/pacchetto/nomepacchetto.zip
```

Una volta fatto, provate a fare:

```bash
python spm.py install nomepacchetto -g
```

- `python` - Python
- `spm.py` - Il file di SPM
- `install` - per installare
- `nomepacchetto` - il nome del pacchetto
- `-g` lo installa globalmente, non per il progetto

---

## Require

La funzione `require()` integrata permette di includere moduli:

```shellOutput
>var hello_world = require("__snode_hello__")
>hello_world
Ciao mondo!
>var tzdata = require("simple_tzdata")
>tzdata.europeRome()
{-9223372036854775808 2996 0 LMT}
{-3252098996 2996 0 RMT}
{-2403565200 3600 0 CET}
{-1690765200 7200 1 CEST}
    --snip--
```

---

# Note e Credits

Snode è un progetto in fase **Alpha**, quindi:
- può contenere bug
- alcune funzioni possono cambiare
- è ancora sperimentale

Snode è creato con Python, Js2Py, colorama e tanta sperimentazione.
