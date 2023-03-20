from src.RinJapaneseTokenizer import RinJapaneseTokenizer

if __name__ == '__main__':
    text = "このトークンライブラリは、漢字を部首に分解してトークン化しています。"
    rin_tokenizer = RinJapaneseTokenizer()
    print(rin_tokenizer.tokenize(text))