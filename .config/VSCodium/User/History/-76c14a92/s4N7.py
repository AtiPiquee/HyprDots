import argparse


def parser_args() -> tuple[str]:
    """_summary_

    Returns:
        tuple[int, int, int, str]: _description_
    """
    parser = argparse.ArgumentParser(description='Test d\'un algorithme de chiffrement.')
    parser.add_argument("--text", type=str, required=True, help="Texte à chiffrer.")

    args = parser.parse_args()

    tests = args.tests
    start = args.start
    end = args.end
    file = args.file

    return tests, start, end, file