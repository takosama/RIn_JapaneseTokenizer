from src.RinJapaneseTokenizer import RinJapaneseTokenizer


def test_add():
    tokenizer=RinJapaneseTokenizer()
    assert tokenizer.encode("凜")==[1105, 715, 432, 465, 555, 666]

def test_add():
    tokenizer=RinJapaneseTokenizer()
    assert tokenizer.encode("このトークンライブラリは、漢字を部首に分解してトークン化しています。")==[248, 275, 352, -1, 327, 395, 385, 316, 366, 385, 386, 276, -1, 1171, 1428, 758, 666, 432, 794, 550, 311, 1569, 465, 666, 228, 1643, 1291, 272, 569, 565, 528, 1498, 565, 1684, 1226, 252, 267, 352, -1, 327, 395, 604, 603, 478, 252, 267, 233, 291, 254, -1]

