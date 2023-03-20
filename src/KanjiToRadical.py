import json


class KanjiToRadical:
    def __init__(self, kanji2element_path):
        with open(kanji2element_path, encoding="utf-8") as f:
            self.kanji2element = json.load(f)

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
