import sys

from colorama import Fore
from pathlib import Path

def draw_directory(directory: str, depth = 0):
    path = Path(directory)

    if not path.is_dir():
        print("Directory not found")
        return

    for directory_element in path.iterdir():

        # Lets add prefix for better readability of nested paths
        prefix = ""
        if depth > 0:
            prefix += "   "*depth

        if directory_element.is_dir():
            print(Fore.BLUE + f"{prefix}{directory_element}")
            draw_directory(str(directory_element), depth + 1)
        else:
            print(Fore.GREEN + f"{prefix}{directory_element}")



def main():
    if len(sys.argv) > 1:
        # Expected that first argument is path to target folder, all other args ignored
        directory_in_sys_argument = sys.argv[1]
        draw_directory(directory_in_sys_argument)
    else:
        print("No args provided! Please provide a directory path as argument")

if __name__ == "__main__":
    main()