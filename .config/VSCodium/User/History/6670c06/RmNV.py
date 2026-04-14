import argparse


def parser_arg():
    parser.add_argument("--test", type=int, required=True, help="Number of tests to do")
    parser.add_argument("--start", type=int, required=True, help="Starting value")
    parser.add_argument("--end", type=int, required=True, help="End value")

    args = parser.parse_args()

    test = args.test
    start = args.start
    end = args.end

    return input_file, Path(input_file), [champs, departement, output_file]