from src.RinJapaneseTokenizer import RinJapaneseTokenizer

if __name__ == '__main__':
    text = "凜"
    text2 = "このトークンライブラリは、漢字を部首に分解してトークン化しています。"
    rin_tokenizer = RinJapaneseTokenizer()
    print(rin_tokenizer.encode(text))
    print(rin_tokenizer.decode(rin_tokenizer.encode(text)))
    print(rin_tokenizer.encode(text2))
    print(rin_tokenizer.decode(rin_tokenizer.encode(text2)))

