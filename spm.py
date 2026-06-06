import os
import sys
import shutil
import requests
import zipfile
from io import BytesIO

MODULES_DIR = "snode_modules"
INDEX_FILE = "trusted_indexs.txt"


def find_package_url(name):
    if not os.path.exists(INDEX_FILE):
        return None

    with open(INDEX_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith(name + "="):
                return line.split("=", 1)[1]

    return None


def install(package, global_install=False):
    url = find_package_url(package)

    if not url:
        print(f"Errore: pacchetto '{package}' non trovato nell'index.")
        return

    try:
        print(f"Download di {package}...")

        response = requests.get(url)
        response.raise_for_status()

        zip_data = zipfile.ZipFile(BytesIO(response.content))

        if global_install:
            base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), MODULES_DIR)
        else:
            base_path = os.path.join(os.getcwd(), MODULES_DIR)

        target_path = os.path.join(base_path, package)

        os.makedirs(target_path, exist_ok=True)

        print(f"Installazione in {target_path}...")

        zip_data.extractall(target_path)

        print(f"Pacchetto '{package}' installato con successo.")

    except Exception as e:
        print(f"Errore durante installazione: {e}")


def uninstall(package):
    paths = [
        os.path.join(os.getcwd(), MODULES_DIR, package),
        os.path.join(MODULES_DIR, package)
    ]

    for path in paths:
        if os.path.exists(path):
            try:
                shutil.rmtree(path)
                print(f"Pacchetto '{package}' rimosso da {path}")
                return
            except Exception as e:
                print(f"Errore durante uninstall: {e}")
                return

    print(f"Errore: pacchetto '{package}' non trovato.")


def main():
    if len(sys.argv) < 3:
        print("Uso:")
        print("  spm install [package]")
        print("  spm install [package] -g")
        print("  spm uninstall [package]")
        return

    command = sys.argv[1]
    package = sys.argv[2]

    if command == "install":
        global_flag = "-g" in sys.argv
        install(package, global_flag)

    elif command == "uninstall":
        uninstall(package)

    else:
        print("Comando non valido.")


if __name__ == "__main__":
    main()
