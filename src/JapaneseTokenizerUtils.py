from src.JapaneseChar import JapaneseChar
from src.RadicalChar import DataLoader

import json


class JapaneseTokenizerUtils:
    def __init__(self):
        DataLoader().Generate_Char2Radical_json()

    def get_all_radical_dict(self):
        with open("char2radical.json", "r", encoding="utf-8") as f:
            return {key: value for key, value in json.load(f).items()}
