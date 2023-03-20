import os
import urllib3
class JsonDownloader:
    def __init__(self):
        pass

    def _download_json_file(self,url, file_path):
        if not os.path.exists(file_path):
            print(f'{file_path}を{url}からダウンロードしています')
            http = urllib3.PoolManager()
            r = http.request('GET', url)
            with open(file_path, "wb") as f:
                f.write(r.data)
            f.close()

    def download(self,kanji2element_path="kanji2element.json"):
        url='https://raw.githubusercontent.com/yagays/kanjivg-radical/master/data/kanji2element.json'
        self._download_json_file(url, kanji2element_path)