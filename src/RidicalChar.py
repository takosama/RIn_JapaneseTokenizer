from src.KanjiToRadical import KanjiToRadical


class RadicalChar:
    def __init__(self, kanji2element_path):
        self.kanji2element = KanjiToRadical(kanji2element_path)
        self.all_radical = {
            element for elements in self.kanji2element.kanji2element.values() for element in elements}

    def get_radical_chars(self, char):
        ret = []
        for kanji in char:
            if kanji in self.all_radical:
                ret.append(kanji)
            ret += self.kanji2element.convert(kanji)
        return ret
