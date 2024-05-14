import argparse

parser = argparse.ArgumentParser("Topic Recognition", description="Get top words from text")
parser.add_argument("filename", help="path to file for analysis")
parser.add_argument("--limit", type=int, default=10, help="quantity of top words")
parser.add_argument("-n", "--normalize", action="store_true", help="casting to normal form")
parser.add_argument("--pos", action="append", choices=("VERB", "NOUN", "ADJF"), help="parts of speech")
parser.add_argument("-r", "--recording", action="append", choices=("json", "csv", "xls", "xlsx", "tsv"),
                    help="select output report format")
