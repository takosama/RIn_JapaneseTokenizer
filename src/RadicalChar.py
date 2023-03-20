import json
from src.JsonDownloader import JsonDownloader


class RadicalChar:
    def __init__(self, kanji2element_path):
        JsonDownloader().download(kanji2element_path)
        with open(kanji2element_path, encoding="utf-8") as f:
            self.kanji2element = json.load(f)
        self.all_radical = set(
            [element for elements in self.kanji2element.values() for element in elements])

    def get_radical_chars(self, char):
        ret = []
        for kanji in char:
            if kanji in self.all_radical:
                ret.append(kanji)
            ret += self.convert(kanji)
        return ret

    def convert(self, element):
        result = []
        queue = [element]
        visited = set()
        while queue:
            node = queue.pop(0)
            if node in visited:
                continue
            visited.add(node)
            if node in self.kanji2element:
                for child in self.kanji2element[node]:
                    queue.append(child)
            else:
                result.append(node)
        return result
