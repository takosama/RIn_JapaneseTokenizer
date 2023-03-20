class JapaneseChar:
    def __init__(self):
        self.all_sjis_chars = self.__get_japanese_chars()

    @staticmethod
    def __get_sjis_chars():
        chars = [chr(i) for i in range(0x20, 0x7f)]
        chars += [chr(i) for i in range(0xa1, 0xe0)]
        sjis_first_bytes = [i for i in range(
            0x81, 0xa0)] + [i for i in range(0xe0, 0xf0)]
        sjis_second_bytes = {i: (0x40, 0x7e) if i !=
                             0x7f else None for i in sjis_first_bytes}
        sjis_second_bytes.update({i: (0x80, 0xfc) for i in range(0x40, 0x7f)})
        sjis_second_bytes.pop(0x7f, None)
        sjis_second_bytes.pop(0xa0, None)
        sjis_second_bytes.pop(0xdf, None)
        sjis_second_bytes.pop(0xfc, None)
        for first_byte, second_byte_range in sjis_second_bytes.items():
            if second_byte_range is not None:
                for second_byte in range(second_byte_range[0], second_byte_range[1] + 1):
                    chars.append(chr(first_byte) + chr(second_byte))
        return chars

    @staticmethod
    def __get_additional_chars():
        chars = []
        chars += [chr(i) for i in range(0x3041, 0x3094)]
        chars += [chr(i) for i in range(0x30a1, 0x30f4)]
        return chars

    def __get_japanese_chars(self):
        japanese_chars = set(self.__get_sjis_chars()) | set(
            self.__get_additional_chars())
        return japanese_chars
