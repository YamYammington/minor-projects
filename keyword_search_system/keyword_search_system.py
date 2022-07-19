import os
import regex as re
# my masterpiece


def parser(s_):
    """
    :param s_: string to be parsed
    :return: tuple of 3 lists of keywords

    Initial parser. It initializes the string, then splits it into keywords and excludes.
    """
    s = s_.removeprefix('@kw ')

    keywords = re.findall(r"\b([a-zA-Z\d]+)(\||&)([a-zA-Z\d]+)\b", s, overlapped=True) if "|" in s or "&" in s else []
    not_kws = [f for f in re.findall(r"n\(((![a-zA-Z\d]+)+)\)", s)[0][0].split('!')] if "!" in s else []

    _and = []
    _or = []
    _not = []

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
    if not_kws:
        _not = not_kws

    # remove all duplicates
    return list(dict.fromkeys(_and)), list(dict.fromkeys(_or)), list(dict.fromkeys(_not))


def get_files(folder: str, *, _not: list, _and: list, _or: list) -> list:
    """
    :param folder: folder to search
    :param _not: list of keyword to be excluded
    :param _and: list of keywords to be included if all are present
    :param _or: list of keywords to be included if any are present
    :return: list of files in folder that match the keywords

    This uses functions to check if conditions are met.

    _not:
        if none of the excluded keywords are in the filename, the file is included
    _and:
        if all the keywords are in the filename, the file is included
    _or:
        if any of the keywords are in the filename, the file is included
    """
    files = os.listdir(folder)

    # I got a massive headache writing this
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
    _and, _or, _not = parser(s)
    return get_files(folder, _not=_not, _and=_and, _or=_or)


# I don't even care about readability or ease of use anymore, it just works, albeit in a very specific way
# furthermore, I really like list comprehensions if you couldn't tell
if __name__ == '__main__':
    kw_str = ""
    path = ""
    print(parse(kw_str, path))
    # print(parse("@kw untitled|happy", "C:\\Users\\Yammington\\Downloads"))
