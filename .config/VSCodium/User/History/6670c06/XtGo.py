import argparse


def parser_args() -> tuple[int, int, int]:
    parser = argparse.ArgumentParser(description='Traitement des résultats donnés par la fonction randint afin d\'en tirer des statistiques')
    parser.add_argument("--tests", type=int, required=True, help="Number of tests to do")
    parser.add_argument("--start", type=int, required=True, help="Starting value")
    parser.add_argument("--end", type=int, required=True, help="End value")

    args = parser.parse_args()

    tests = args.tests
    start = args.start
    end = args.end

    return tests, start, end