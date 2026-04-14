import argparse


def parser_args() -> tuple[int, int, int, str]:
    parser = argparse.ArgumentParser(description='Traitement des résultats donnés par la fonction randint afin d\'en tirer des statistiques')
    parser.add_argument("--tests", type=int, required=True, help="Nombre de tests à faire")
    parser.add_argument("--start", type=int, required=True, help="Valeur de départ")
    parser.add_argument("--end", type=int, required=True, help="Valeur de fin")
    parser.add_argument("--file", type=str, required=False, help="Nom du fichier d'exportation des résultats")

    args = parser.parse_args()

    tests = args.tests
    start = args.start
    end = args.end
    file = args.file

    return tests, start, end