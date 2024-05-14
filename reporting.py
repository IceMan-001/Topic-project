import json
import csv
import os
from time import strftime


def populate_date():
    base_path = "reports"

    if not os.path.exists('reports'):
        os.mkdir('reports')

    unix = str(strftime('%d-%m-%Y %H-%M'))
    folder = f"{base_path}/{unix}"
    if not os.path.exists(folder):
        os.mkdir(folder)

    return unix


def get_report(top_words, limit, destination: str = "stdout"):
    base_path = "reports"
    file_name_for_report = 'top_' + limit + '.' + destination
    match file_name_for_report.rsplit(".", maxsplit=1):
        case ["stdout"]:
            print(top_words)
        case [_, "json"]:
            with open(f"{base_path}\\{populate_date()}\\{file_name_for_report}", "w", encoding="utf-8") as fp:
                json.dump(dict(top_words), fp, ensure_ascii=False, indent=2)
        case [filename, "xls" | "xlsx" | "csv" | "tsv"]:
            with open(f"{base_path}\\{populate_date()}\\{file_name_for_report}", "w", newline="") as fp:
                writer = csv.writer(fp)
                writer.writerows(top_words)



