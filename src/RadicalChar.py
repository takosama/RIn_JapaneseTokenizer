import json
from src.JapaneseChar import JapaneseChar
from src.JsonDownloader import JsonDownloader


class DataLoader:
    def __init__(self, kanji2element_path="kanji2element.json"):
        JsonDownloader().download(kanji2element_path)
        with open(kanji2element_path, encoding="utf-8") as f:
            self.kanji2element = json.load(f)
        self.kanji2element = {
            key: value for key, value in self.kanji2element.items()}

    def Generate_Char2Radical_json(self, kanji2element_path="kanji2element.json"):
        japanese_char = JapaneseChar()

        all_radical_dict = set()
        [all_radical_dict.update(i) for i in [list(i)
                                              for i in self.kanji2element.values()]]

        for i in japanese_char.get_japanese_chars():
            if i not in all_radical_dict:
                if len(i) == 1:
                    all_radical_dict.add(i)
                elif len(i) == 2:
                    all_radical_dict.update(i)

        all_radical_dict = sorted(all_radical_dict)
        save_path = "radical_dic.json"
        import json
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump({j: i for i, j in enumerate(all_radical_dict)},
                      f, ensure_ascii=False, indent=4)

        return {j: i for i, j in enumerate(all_radical_dict)}

    def get_radical_chars(self, char):
        ret = []
        for kanji in char:
            if kanji in self.kanji2element:
                ret.append(self.kanji2element[kanji])
            else:
                ret.append(-1)
        return ret
