import argparse


def parser_arg():
    parser.add_argument("--test", type=int, required=True, help="Nombre de tests à effectuer")
    parser.add_argument("--start", type=int, required=True, help="Valeur de départ")
    parser.add_argument("--end", type=int, required=True, help="Valeur de fin")

    args = parser.parse_args()

    test = args.test
    start = args.start
    end = args.end

    return input_file, Path(input_file), [champs, departement, output_file]