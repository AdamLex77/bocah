from glob import glob
from os.path import basename, dirname, isfile


def loadModule():
    return sorted([
        basename(f)[:-3]
        for f in glob(f"{dirname(__file__)}/*.py")
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ])
