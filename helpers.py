import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear_screen")


def print_libraries(library_list):
    for lib in library_list:
        print(f"{lib.name}")


def save_library_list(library_list, source = "library_list.txt"):
    with open(source, "a+") as library_list_source:
        library_list_source.seek(0)
        library_list_source.truncate(0)

        for lib in library_list:
            if lib != library_list[-1]:
                library_list_source.write(f"{lib.name},")
            else:
                library_list_source.write(f"{lib.name}")