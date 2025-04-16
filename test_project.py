from project import txt_load
from project import txt_analyze
from project import txt_popstop
import pytest

def main():
    test_project()


def test_txt_loat(tmp_path):
    # Tworzymy tymczasowy plik z testowym tekstem
    test_file = tmp_path / "sample.txt"
    test_file.write_text("BIM is the future of design and construction")

    # Wywołanie funkcji
    result = txt_load(str(test_file))

    # Spodziewana lista słów
    expected = ["BIM", "is", "the", "future", "of", "design", "and", "construction"]

    assert result == expected

def test_txt_analyze():
    lista = ["a","b"]
    assert txt_analyze(lista) == [
        {"slowo": lista[0].capitalize(), "ilosc": 1},
        {"slowo": lista[1].capitalize(), "ilosc": 1}
    ]


def test_txt_popstop(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "")
    lista = [
        {"slowo": "A", "ilosc": 1},
        {"slowo": "Kot", "ilosc": 1},
        {"slowo": "Pies", "ilosc": 2}
    ]
    assert txt_popstop(lista) == [
        {"slowo": "Kot", "ilosc": 1},
        {"slowo": "Pies", "ilosc": 2}
    ]

if __name__ == "__main__":
    main()
