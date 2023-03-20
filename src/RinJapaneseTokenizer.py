
from src.JapaneseTokenizerUtils import JapaneseTokenizerUtils


class RinJapaneseTokenizer:
    def __init__(self, kanji2element_path="kanji2element.json"):
        self.util = JapaneseTokenizerUtils(kanji2element_path)

    def encode(self, text):
        tokenize_splitted = []
        for i in text:
            tokenize_splitted.extend(self.util.radical_char.get_radical_chars(i))
        tokenize_splitted_nums = [self.util.get_all_radical_dict().get(i,-1) for i in tokenize_splitted]
        return tokenize_splitted_nums

    def decode(self, tokens):
        text = ""
        for token in tokens:
            if token == -1:
                text += "[UNK]"
                continue
            #valueからkeyを取得
            for key, value in self.util.get_all_radical_dict().items():
                if value == token:
                    text += key
                    break
        return text
