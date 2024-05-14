import re
import pymorphy3


def tokenize(
    text: str,
    normalize: bool = True,
    filter_pos: bool | tuple[str] = False,
    filter_stopwords: bool = True,
) -> list[str]:
    preprocessed_text = text.upper()
    tokens = re.split("\W+", preprocessed_text)
    tokens = [token for token in tokens if token.isalpha()]

    analyzer = pymorphy3.MorphAnalyzer()

    if filter_pos:
        tokens_ = []

        for token in tokens:
            try:
                if analyzer.parse(token)[0].tag.POS in filter_pos:
                    tokens_.append(token)
            except Exception:
                pass

        tokens = tokens_

    if normalize:
        tokens = [analyzer.parse(token)[0].normal_form for token in tokens]

    if filter_stopwords:
        with open("stopwords-ru.txt", encoding="utf-8") as fp:
            stop_words = fp.read().splitlines()
        return [token for token in tokens if token.lower() not in stop_words]
    return tokens
