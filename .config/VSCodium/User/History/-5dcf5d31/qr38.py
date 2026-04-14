import csv
from typing import List, Tuple, Dict

"""
Exporting results to a .csv file
"""

header = ["valeur", "compte", "pourcentage"]

def csv_export(statistics, filename) -> bool:
    with open(filename, "w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, delimiter=";", fieldnames=header, quoting=csv.QUOTE_NUMERIC)
        writer = writeheader()
