
from src.RadicalChar import DataLoader
from src.JapaneseTokenizerUtils import JapaneseTokenizerUtils

class RinJapaneseTokenizer:
    def __init__(self):
        self.util = JapaneseTokenizerUtils()
        self.radicalCHar = DataLoader() 

    def encode(self, text):
        tokenize_splitted = []
        for i in text:
            tokenize_splitted.extend( (i))
        tokenize_splitted_nums = [self.radicalCHar.kanji2element[i] for i in tokenize_splitted]
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
