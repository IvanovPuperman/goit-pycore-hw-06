import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def show_structure(path, indent=""):
    for item in path.iterdir():
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}")
            show_structure(item, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN}{item.name}")

if len(sys.argv) < 2:
    print("Вкажіть шлях до директорії")
    sys.exit()

path = Path(sys.argv[1])

if not path.exists():
    print("Шлях не існує")
    sys.exit()
if not path.is_dir():
    print("Це не директорія")
    sys.exit()

show_structure(path)