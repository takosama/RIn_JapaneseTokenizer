from src.RinJapaneseTokenizer import RinJapaneseTokenizer

if __name__ == '__main__':
    text = "凜このトークンライブラリは、漢字を部首に分解してトークン化しています。"
    rin_tokenizer = RinJapaneseTokenizer()
    print(rin_tokenizer.tokenize(text))
    print(rin_tokenizer.decode(rin_tokenizer.tokenize(text)))

#todo tokenizeの部首取得を少し直す