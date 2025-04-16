from tabulate import tabulate
from rich.console import Console
import string
import argparse


def main():
    # Czyszcze console przy kazdym uruchomieniu
    console = Console()
    console.clear()

    # Pobieram nazwe pliku z prompta. default jest text.txt
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", default="text.txt", help="n is a number of meows")
    args = parser.parse_args()

    # Na bazie inputu wczytuje plik
    words = txt_load(args.n)

    # Na bazie wczytanego pliku analizuje go
    zestawienie = txt_analyze(words)

    # na bazie przeanalizowanego pliku usuwam wybrane slowa postojowe
    zestawienie_no_stop_words = txt_popstop(zestawienie)

    text_sorted(zestawienie_no_stop_words)


def txt_load(x: str) -> list:
    """
    loads lines from .txt file and divides it into words

    :param x: .txt file name
    :type: string
    :return: list of words
    :rtype: list
    """
    with open(x, "r") as file:
        lines = file.read()
        words = lines.split()
        return words


def txt_analyze(y: list) -> list:
    """
    Analyzes amount of words in text

    :param y: list words
    :param type: list
    :return: list of dict {"word":word, "count": count}
    :rtype: list of dict
    """
    word_count: dict[str, int] = {}

    for word in y:
        # Aby to z unifikowac usuwam kropki i przecinki oraz robie lower() aby Bim i bim bylo jednakowe, tak samo jak Bim i Bim.
        word = word.strip(string.punctuation).capitalize()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    word_list = []
    for xx, yy in word_count.items():           # !!! trzeba pamietc o .items() !!!
        word_list.append({"slowo": xx, "ilosc": yy})

    return word_list


def txt_popstop(sw: list) -> list:
    """
    Takes list of dict of used words and subtracts words such as: a, an, the, etc...

    :param sw: list{words: , numbers:}
    :param type: list
    :rtype: list
    :return: list of words without stop_words
    """

    print()
    print("\033[91mDefault skipped words are: a, an, the\033[0m")
    to_subtract = input(
        "Type words to subtract from equation(separated by , without space): "
    )

    if to_subtract:
        stop_words = to_subtract.split(",")
    else:
        stop_words = [
            "a",
            "an",
            "the",
            "A",
            "An",
            "The"
        ]  # jesli user nie poda nic, to przypisuje wartosc domyslna

    return list(
        filter(lambda x: x["slowo"] not in stop_words, sw)
    )  # dzieki list(filter od razu przeksztalcam na liste z filtra

def text_sorted(zestawienie_no_stop_words):
    """
    Takes a list of dicts with words and sorts it either by amount ar alphabetically

    :param zestawienia_no_stop_words: list od words and amounts
    :param type: list{}
    :rtype: .txt file nad print
    :return: sorted .txt file
    """
    while True:
        choose_sort = input("Sort alphabeticaly or by amount? : alpha/amo -> ")
        if choose_sort == "alpha":
            # for row in sorted(zestawienie_no_stop_words, key=lambda z:z["slowo"]):
            # print(row)
            sorted_list = sorted(
                zestawienie_no_stop_words, key=lambda z: z["slowo"]
                )
            print(tabulate(sorted_list, headers="keys", tablefmt="grid"))

            txt_write(sorted_list, "Sorted alphabetically")
            break

        elif choose_sort == "amo":
            # for row in sorted(zestawienie_no_stop_words, key=lambda z:z["ilosc"], reverse=True):
            # print(row)
            sorted_list = sorted(
                zestawienie_no_stop_words, key=lambda z: z["ilosc"], reverse=True
            )
            print(tabulate(sorted_list, headers="keys", tablefmt="grid"))

            txt_write(sorted_list, "Sorted by amount")
            break

        else:
            continue

def txt_write(z, sorted_by):
    """
    Writes list of words with an amount to a .txt file + info on sort type

    :param z: list{words: , numbers:}
    :param sorted_by: string
    :param type: list{}
    :rtype: .txt file
    :return: .txt file with enumerated words
    """
    with open("Analyzer.txt", "w") as file:
        file.write(f"{sorted_by}\n\n")
        file.write(tabulate(z, headers="keys", tablefmt="grid"))
# FIN

if __name__ == "__main__":
    main()
