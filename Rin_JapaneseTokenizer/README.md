# Rin_JapaneseTokenizer

[main.py](https://www.notion.so/main-py-a0662ce483784e6facc1bed5ce187057)

[src](https://www.notion.so/src-ef7fb55782f94d46906b31b661d107c4)

# Rin_JapaneseTokenizer

This repository contains the source code for Rin_JapaneseTokenizer, a tool for tokenizing Japanese text. By using this library, Japanese text can be tokenized taking into account radicals. This can potentially result in more accurate results when inputting Japanese text into machine learning models. Currently, machine learning models often overlook radical information when simply tokenizing Japanese text, which can result in inaccurate results. However, by using this library and taking into account radicals, more accurate results can be obtained.

To use the library:

1. Clone this repository or download and extract the zip file.
2. Import the `japanese_tokenizer.py` file located in the `src` directory.
Using the `JapaneseTokenizer` class, Japanese text can be tokenized while taking radicals into account. Additionally, the `tokenize` method can be used to easily tokenize Japanese text.
3. Create an instance of the `JapaneseTokenizer` class as follows:

```
tokenizer = JapaneseTokenizer()

```

1. Use the `tokenize` method to tokenize the Japanese text:

```
text = "このトークンライブラリは、漢字を部首に分解してトークン化しています。"
tokens = tokenizer.tokenize(text)
print(tokens)

```

Output:

```
[248, 275, 352, -1, 327, 395, 385, 316, 366, 385, 386, 276, -1, 1171, 1428, 758, 432, 666, 550, 794, 311, 1569, 465, 666, 228, 1643, 1291, 272, 569, 565, 528, 1498, 1684, 565, 1226, 252, 267, 352, -1, 327, 395, 604, 603, 478, 252, 267, 233, 291, 254, -1]

```

By using the `JapaneseTokenizer` class, Japanese text can be easily tokenized while taking radicals into account.

This library is called Rin_JapaneseTokenizer and is a tool for tokenizing Japanese text while taking radicals into account. By using this library, more accurate results can be obtained when inputting Japanese text into machine learning models. Additionally, this library automatically downloads files from [https://github.com/yagays/kanjivg-radical](https://github.com/yagays/kanjivg-radical) and uses files under the CC-BY-SA-4.0 license. The program itself is released under the MIT license.

License Notice:

- Rin_JapaneseTokenizer: MIT License
- [https://github.com/yagays/kanjivg-radical:](https://github.com/yagays/kanjivg-radical:) CC-BY-SA-4.0 License

# Rin_JapaneseTokenizer

このリポジトリには、Rin_JapaneseTokenizerのソースコードが含まれています。Rin_JapaneseTokenizerは、日本語のテキストをトークン化するためのツールです。このライブラリを使用することで、日本語のテキストを部首を考慮したトークン化することができます。これにより、日本語のテキストを機械学習のモデルに入力する際、より精度の高い結果を得ることができるかもしれません。例えば、現在の機械学習のモデルは、日本語のテキストを単純にトークン化するため、部首の情報を見落とし、結果が不正確になることがあります。しかし、このライブラリを使用することで、部首を考慮することで、より正確な結果を得ることができます。

使い方は以下の通りです。

1. このリポジトリをクローンするか、zipファイルをダウンロードして解凍します。
2. `src` ディレクトリ内の `japanese_tokenizer.py` ファイルをインポートします。
`JapaneseTokenizer` クラスを使用することで、日本語のテキストを部首を考慮してトークン化することができます。これにより、日本語のテキストを機械学習のモデルに入力する際、より精度の高い結果を得ることができます。また、`tokenize` メソッドを使用することで、日本語のテキストを簡単にトークン化することができます。
3. 以下のように、`JapaneseTokenizer` クラスのインスタンスを作成します。
    
    ```
    tokenizer = JapaneseTokenizer()
    
    ```
    
4. `tokenize` メソッドを使用して、日本語のテキストをトークン化します。
    
    ```
    text = "このトークンライブラリは、漢字を部首に分解してトークン化しています。"
    tokens = tokenizer.tokenize(text)
    print(tokens)
    
    ```
    
    出力結果：
    
    ```
    [248, 275, 352, -1, 327, 395, 385, 316, 366, 385, 386, 276, -1, 1171, 1428, 758, 432, 666, 550, 794, 311, 1569, 465, 666, 228, 1643, 1291, 272, 569, 565, 528, 1498, 1684, 565, 1226, 252, 267, 352, -1, 327, 395, 604, 603, 478, 252, 267, 233, 291, 254, -1]
    
    ```
    
    以上のように、`JapaneseTokenizer` クラスを使用することで、日本語のテキストを簡単に部首を考慮したトークン化することができます。
    
    このライブラリは Rin_JapaneseTokenizer と呼ばれ、日本語のテキストを部首を考慮してトークン化するためのツールです。このライブラリを使用することで、日本語のテキストを機械学習のモデルに入力する際、より精度の高い結果を得ることができます。また、このライブラリは、[https://github.com/yagays/kanjivg-radical](https://github.com/yagays/kanjivg-radical) のファイルを自動でダウンロードし、CC-BY-SA-4.0ライセンスのファイルを使用しています。プログラム自体はMITライセンスで公開されています。
    
    ライセンス表記：
    
    - Rin_JapaneseTokenizer: MIT License
    - [https://github.com/yagays/kanjivg-radical:](https://github.com/yagays/kanjivg-radical:) CC-BY-SA-4.0 License