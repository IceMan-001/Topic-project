from collections import defaultdict
from reporting import get_report
from tokenizing import tokenize
from cli import parser


def get_text(source="stdin") -> str:
    match source:
        case "stdin":
            return input("Текст для анализа: ")
        case _ as filepath:
            with open(filepath, encoding="utf-8") as fp:
                return fp.read()


def count_words(words: list[str]) -> dict:
    counter = defaultdict(int)
    for word in words:
        counter[word] += 1
    return counter


def get_top_words(counter: dict, limit: int = 10) -> tuple[tuple]:
    def by_value(item):
        return item[1]

    sorted_words = sorted(counter.items(), key=by_value, reverse=True)
    return sorted_words[:limit]


def main():
    args = parser.parse_args()

    text = get_text(args.filename)
    words = tokenize(text, args.normalize, args.pos)
    words_counter = count_words(words)
    top_words = get_top_words(words_counter, limit=args.limit)
    get_report(top_words, str(args.limit), ''.join(args.recording))


main()
