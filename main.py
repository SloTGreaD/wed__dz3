import argparse
import logging
from pathlib import Path
from shutil import copyfile
from threading import Thread


parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument("--source", "-s", help="Source folder", required=True)
parser.add_argument("--output", "-o", help="Source folder", default="dist")

print(parser.parse_args())
args = vars(parser.parse_args())
print(args)

source = Path(args.get("source"))
output = Path(args.get("output"))

folders = []


def garbage_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            garbage_folder(el)

def copy_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:]
            ext_folder = output / ext 
            try: 
                ext_folder.mkdir(exist_ok=True, parents=True)
                copyfile(el, ext_folder / el.name)
            except OSError as err:
                logging.error(err)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")

    folders.append(source)
    garbage_folder(source)
    print(folders)
    
    threads = []
    for folder in folders:
        th = Thread(target=copy_folder, args=(folder,))
        th.start()
        threads.append(th)
    [th.join() for th in threads]
    print(f"you can delete {source}")
    