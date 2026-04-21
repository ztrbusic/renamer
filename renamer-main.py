from pathlib import Path
import sys
from unidecode import unidecode

def read_folder_names(path: Path) -> list:
    folder_list = []
    for x in path.rglob("*"):
        if x.is_dir():
            folder_list.append(x)
    return folder_list

def rename(path: Path):
    to_change = [" ", ",", ".", "_", "---", "--"]
    n = 1
    l = []
    for x in path.rglob("*"):
        if x.is_dir():
            if x.suffix:
                temp = x.stem + x.suffix
            else:
                temp = x.stem
            for change in to_change:
                temp = temp.replace(change, "-")
            temp = unidecode(temp[:1].upper() + temp[1:])
#            l = [y.stem for y in x.parent.iterdir()]
            if temp in l:
                n += 1
                new_path = Path(str(x.parent) + "/" + temp + "-" + str(n))
            else:
                new_path = Path(str(x.parent) + "/" + temp)
            x.replace(new_path)
            l.append(temp)


if sys.argv[1] == "read":
    with open("renamer-dir-list.txt", "w") as f:
        for x in read_folder_names(Path(sys.argv[2])):
            f.write(f"{x.stem}\n")

if sys.argv[1] == "execute":
        rename(Path(sys.argv[2]))




