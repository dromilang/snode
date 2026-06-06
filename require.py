import os
import js2py

MODULES_DIR = "snode_modules"


def _get_global_modules_dir():
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        MODULES_DIR
    )


def _get_local_modules_dir():
    return os.path.join(os.getcwd(), MODULES_DIR)


def require(name):
    """
    require() per Snode con supporto locale + globale
    """

    # possibili percorsi (priorità: locale -> globale)
    paths = [
        os.path.join(_get_local_modules_dir(), name, "index.js"),
        os.path.join(_get_global_modules_dir(), name, "index.js")
    ]

    module_path = None

    for p in paths:
        if os.path.exists(p):
            module_path = p
            break

    if not module_path:
        raise ImportError(f"Modulo '{name}' non trovato (locale o globale)")

    with open(module_path, "r", encoding="utf-8") as f:
        code = f.read()

    # ambiente isolato per il modulo
    module = js2py.EvalJs({})
    module.execute("var exports = {};")

    module.execute(code)

    return module.exports
