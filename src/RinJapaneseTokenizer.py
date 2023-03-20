from src.JapaneseTokenizerUtils import JapaneseTokenizerUtils


class RinJapaneseTokenizer:
    def __init__(self, kanji2element_path="kanji2element.json"):
        self.util = JapaneseTokenizerUtils(kanji2element_path)

    def encode(self, text):
        tokenize_splitted = [
            self.util.radical_char.get_radical_chars(i) for i in text]
        tokenize_splitted = [j for i in tokenize_splitted for j in i]

        dic = self.util.get_all_radical_dict()
        return [dic[i] if i in dic else -1 for i in tokenize_splitted]

    def decode(self, tokens):
        text = ""
        for token in tokens:
            if token == -1:
                text += "[UNK]"
                continue
            # valueからkeyを取得
            for key, value in self.util.get_all_radical_dict().items():
                if value == token:
                    text += key
                    break
        return text
