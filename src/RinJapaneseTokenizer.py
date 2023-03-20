from src.JapaneseTokenizerUtils import JapaneseTokenizerUtils
from src.JsonDownloader import JsonDownloader

class RinJapaneseTokenizer:
    def __init__(self, kanji2element_path="kanji2element.json"):
        JsonDownloader().download(kanji2element_path)
        self.util = JapaneseTokenizerUtils(kanji2element_path)

    def tokenize(self, text):
        tokenize_splited = []
        [tokenize_splited.extend(self.util.radical_char.get_radical_chars(i)) for i in text]
        tokenize_splited_nums = [self.util.all_radical_dic.get(i, -1) for i in tokenize_splited]
        return tokenize_splited_nums

    def decode(self, tokens):
        text = ""
        for token in tokens:
            if token == -1:
                text += "[UNK]"
                continue
            #valueからkeyを取得
            for key, value in self.util.all_radical_dic.items():
                if value == token:
                    text += key
                    break
        return text
