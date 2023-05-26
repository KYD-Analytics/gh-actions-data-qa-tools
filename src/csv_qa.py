"""
    Description: Checks overlapping versions on multiple files using custom column names
    Author: William Lee

"""
import sys
import getopt
from pathlib import Path
from version_overlap_check import scan_file

def main(argv:any):
    """Runs the scan_file function from version_overlap_check on multiple files
        and allow targeting of custom column names. Prints filenames of failed checks,
        indices of overlaps and amount of overlaps found.

    Args:
        argv (any): Arguments from command line 
            e.g: csv_qa.py -k <keyname> -s <startname> -e <endname> <csv file path>
    """
    key_column_name = ''
    start_column_name = ''
    end_column_name = ''

    # Get values in options and argv
    try:
        opts, args = getopt.getopt(argv, "hk:s:e:", ["key=", "start=", "end="])
    except getopt.GetoptError:
        print ('csv_qa.py -k <keyname> -s <startname> -e <endname>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('csv_qa.py -k <keyname> -s <startname> -e <endname>')
        elif opt in ("-k", "--key"):
            key_column_name = arg
        elif opt in ("-s", "--start"):
            start_column_name = arg
        elif opt in ("-e", "--end"):
            end_column_name = arg
    # Provide default value for options
    if key_column_name == '':
        key_column_name = 'key_id'
        print('Value for key not found, default value will be used.')
    if start_column_name == '':
        start_column_name = 'startv'
        print('Value for start not found, default value will be used.')
    if end_column_name == '':
        end_column_name = 'endv'
        print('Value for end not found, default value will be used.')

    failed_files = []
    checked_files = []
    # Check multiple files for overlapping versions
    for file in args:
        output = scan_file(file, key=key_column_name, start=start_column_name, end=end_column_name)
        # print(f'[{file}]')
        # print('Number of version overlaps found:', output[0])
        if output[0] > 0:
            failed_files.append(file)
            # print('List of overlapping versions for keys and their index:', output[1])
        checked_files.append(Path(file).stem)

    # Print filenames that failed checks or print that all checks had passed
    if len(failed_files) > 0:
        print(f"Run ended. Version overlap found in dataset(s): {failed_files}")
        sys.exit("Checks failed.")
    else:
        print("Run ended. No overlaps found in files: ", checked_files)

if __name__ == "__main__":
    main(sys.argv[1:])
