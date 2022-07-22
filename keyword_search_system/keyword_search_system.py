import os
import regex as re


def parse(s: str, folder: str) -> list:
    """
    :param s: string to parse
    :param folder: folder to search
    :return: list of paths to files

    Keyword search system

    String syntax:
        @kw <kw|kw&kw> n(<!kw!kw>)

        Where the contents of <> are logical keywords, and the contents of n() keywords to be excluded from the search.
        @kw is a command to search for keywords.

    Example:
        @kw g1|g2|g3&g4|g5&g6 n(-g5-g6!g7!g8)

    Returns a list of files in a given folder that match the keywords.
    """
    s = s.removeprefix('@kw ')

    keywords = re.findall(r"\b([a-zA-Z\d]+)(\||&)([a-zA-Z\d]+)\b", s, overlapped=True) if "|" in s or "&" in s else []
    _not = [f for f in re.findall(r"n\(((![a-zA-Z\d]+)+)\)", s)[0][0].split('!')] if "!" in s else []

    _and = []
    _or = []

    if keywords:
        for m1, op, m2 in keywords:
            if op == "&":
                _and.append(m1)
                _and.append(m2)
            elif op == "|":
                _or.append(m1)
                _or.append(m2)
            else:
                continue

    # remove all duplicates
    _and, _or, _not = list(dict.fromkeys(_and)), list(dict.fromkeys(_or)), list(dict.fromkeys(_not))

    files = os.listdir(folder)
    if _not:
        def keywords_not_in_file(f):
            return all([x not in f.lower() for x in _not])

        files = [f for f in files if keywords_not_in_file(f)]

    if _and:
        def all_keywords_in_file(f):
            return all([x in f.lower() for x in _and])

        files = [f for f in files if all_keywords_in_file(f)]

    if _or:
        def any_keywords_in_file(f):
            return any([x in f.lower() for x in _or])

        files = [f for f in files if any_keywords_in_file(f)]

    return [os.path.join(folder, f) for f in files]


if __name__ == '__main__':
    kw_str = ""
    path = ""
    print(parse(kw_str, path))
    # example:
    # print(parse("@kw untitled|happy", "C:\\Users\\Yammington\\Downloads"))
