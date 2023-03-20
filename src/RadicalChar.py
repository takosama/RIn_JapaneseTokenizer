import json
import os
import urllib3


class DataLoader:
    def __init__(self):
        pass

    def __init__(self, kanji2element_path):
        self.download(kanji2element_path)
        with open(kanji2element_path, encoding="utf-8") as f:
            self.kanji2element = json.load(f)
        self.all_radical = set(
            [element for elements in self.kanji2element.values() for element in elements])

    def _download_json_file(self, url, file_path):
        if not os.path.exists(file_path):
            print(f'{file_path}を{url}からダウンロードしています')
            http = urllib3.PoolManager()
            r = http.request('GET', url)
            with open(file_path, "wb") as f:
                f.write(r.data)
            f.close()

    def download(self, kanji2element_path):
        url = 'https://raw.githubusercontent.com/yagays/kanjivg-radical/master/data/kanji2element.json'
        self._download_json_file(url, kanji2element_path)


class RadicalChar:
    def __init__(self, kanji2element_path="kanji2element.json"):
        self.dataloader = DataLoader(kanji2element_path)
        self.kanji2element = self.dataloader.kanji2element
        self.all_radical = self.dataloader.all_radical

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
