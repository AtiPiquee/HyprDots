import csv
from typing import List, Tuple, Dict

"""
Exporting results to a .csv file
"""

header = ["valeur", "compte", "pourcentage"]

def csv_export(statistics: List[Tuple[int, int, float]], filename: str) -> str:
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, delimiter=";", fieldnames=header, quoting=csv.QUOTE_NUMERIC)
            writer = writeheader()

            for valeur, count, pct in statistics:
                writer.writerow({header[0]: valeur}, {header[1]: count}, {header[2]: pct})
        return f"Résultats bien exportés dans {filename}"   
    except:
        return f"Les résultats n'ont pas pu être exportés dans {filename}"
    """

    with open(filename, "w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, delimiter=";", fieldnames=header, quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for valeur, count, pct in statistics:
            writer.writerow({header[0]: valeur}, {header[1]: count}, {header[2]: pct})

        return f"Résultats bien exportés dans {filename}"   

