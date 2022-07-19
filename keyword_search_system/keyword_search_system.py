import os
import regex as re


def parser(s: str) -> tuple:
    s = s.removeprefix('@kw ')

    keywords = re.findall(r"\b([a-zA-Z\d]+)(\||&)([a-zA-Z\d]+)\b", s, overlapped=True)
    if "n(!" in s:
        not_kws = [f for f in re.findall(r"n\(((![a-zA-Z\d]+)+)\)", s)[0][0].split('!') if f]
    else:
        not_kws = []

    _and = []
    _or = []
    _not = []

    if keywords:
        for keyword_1, operator, keyword_2 in keywords:
            if operator == "&":
                _and.append(keyword_1)
                _and.append(keyword_2)
            elif operator == "|":
                _or.append(keyword_1)
                _or.append(keyword_2)
            else:
                continue
    if not_kws:
        _not = not_kws

    # remove duplicates
    return list(dict.fromkeys(_and)), list(dict.fromkeys(_or)), list(dict.fromkeys(_not))


def get_files(folder: str, *, _not: list, _and: list, _or: list) -> list:
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


def parse(string_to_parse: str, folder: str) -> list:
    _and, _or, _not = parser(string_to_parse)
    return get_files(folder, _not=_not, _and=_and, _or=_or)


# I don't even care about readability or ease of use anymore, it just works, albeit in a very specific way
# furthermore, I really like list comprehensions if you couldn't tell
if __name__ == '__main__':
    kw_str = ""
    path = ""
    print(parse(kw_str, path))
    # print(parse("@kw untitled|happy", "C:\\Users\\Yammington\\Downloads"))
