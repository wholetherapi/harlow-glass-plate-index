"""Build the Harlow name index from the OCR output."""

import csv
from collections import defaultdict


def group_by_name(rows: list[dict]) -> dict[str, list[str]]:
    index: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        index[row["name"]].append(row["plate_numbers"])
    return dict(index)


if __name__ == "__main__":
    with open("index/names.csv", encoding="utf-8") as handle:
        print(group_by_name(list(csv.DictReader(handle))))
