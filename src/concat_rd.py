"""
    Description: Takes file paths from command line arguments and concatenates the files within
    Author: William Lee

"""
import csv
import argparse
from pathlib import Path

def main():
    """Takes files from input file path, add a column for origin filename, concatenates files
        and outputs the result to an output file named in the command line argument option.
            e.g: py concat_rd.py <input file path> -o <output file path>
    """
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("input", type=str, nargs="+", help="input path dir")
    # arg_parser.add_argument("-r", "--recursive", help="BOOLEAN concatenate path recursively")
    arg_parser.add_argument("-o", "--output", type=str, help="output path dir")
    args = arg_parser.parse_args()

    # Stop the program if no output path is provided, turns output from optional to mandatory
    if not args.output:
        print('usage: concat_rd.py [-h] [-o OUTPUT] input [input ...]')
        print('concat_rd.py: error: the following arguments are required: output')
        return

    # Sort files by filename in alphabetical order
    files = sorted(args.input)
    out_path = args.output

    # Dataset header
    concatenate_csvs = [[
        'DATASET_CD',
        'KEY_CD',
        'KEY_DS',
        'CONFIG_CD',
        'START_VER_NU',
        'END_VER_NU'
    ]]

    for file in files:
        with open(file, 'r', encoding='utf-8') as csv_in:
            with open(out_path, 'w', encoding='utf-8') as csv_out:
                csv_reader = csv.reader(csv_in, delimiter=',')
                csv_writer = csv.writer(csv_out, lineterminator='\n')
                next(csv_reader)

                filename = Path(file).stem
                for row in csv_reader:
                    row.insert(0, filename)
                    concatenate_csvs.append(row)

                csv_writer.writerows(concatenate_csvs)

if __name__ == "__main__":
    main()
