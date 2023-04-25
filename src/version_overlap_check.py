"""
    Description: Checks for version overlap of keys in csv files
    Author: William Lee

"""
import csv
# import sys

# check_failed_flag = False
# failed_files = []
def scan_file(filename:str, overlap_list:int)->int:
    """Checks input filename for overlaps in start and end versions

    Args:
        filename (str): name of the input file
        overlap_list (dict): a dictionary of keys with overlaps and their indices

    Returns:
        int: Count of number of overlaps found in input
    """
    # TODO: Implement getopt options for input settings
    KEY_COLUMN_NAME = 'key_id'
    START_COLUMN_NAME = 'startv'
    END_COLUMN_NAME = 'endv'

    key_check = {}
    overlap_count = 0
    overlap_list = {}

    with open(filename, 'r', encoding='utf-8') as csv_in:
        csv_reader = csv.DictReader(csv_in, delimiter=',')
        line_count = 1
        for row in csv_reader:
            key_value = row[KEY_COLUMN_NAME]
            start_value = row[START_COLUMN_NAME]
            end_value = row[END_COLUMN_NAME]
            # Check if key exists
            if key_value in key_check:
                # Current version case
                if end_value == '':
                    # Has existing current version that clashes with new current version
                    if key_check[key_value]['has_current_version']:
                        # Add old current version to tracker
                        if overlap_list.get(key_value):
                            overlap_list[key_value].update({
                                key_check[key_value]['current_version_line']: [start_value, '']
                            })
                        else:
                            overlap_list.update({
                                key_value: {
                                    key_check[key_value]['current_version_line']: [start_value, '']
                                }
                            })
                        # Add new current version to tracker and checked list
                        overlap_list[key_value].update({
                            line_count: [start_value, '']
                        })
                        key_check[key_value]['lines'].update({
                            line_count: [start_value, '']
                        })
                    # Set record as existing current version
                    else:
                        key_check[key_value].update({
                            'has_current_version': True,
                            'current_version_line': line_count
                        })
                        # Check if current version overlaps with an existing key
                        for k, v in key_check[key_value]['lines'].items():
                            if int(start_value) < int(v[1]):
                                # Add current version to tracker
                                if overlap_list.get(key_value):
                                    overlap_list[key_value].update({
                                        line_count: [start_value, end_value]
                                    })
                                else:
                                    overlap_list.update({
                                        key_value: {
                                            line_count: [start_value, end_value]
                                        }
                                    })
                                # Add existing key to tracker
                                overlap_list[key_value].update({
                                    k: v
                                })
                else:
                    for k, v in key_check[key_value]['lines'].items():
                        # Check if record is within previous version ranges
                        if not ((int(start_value) < int(v[0]) and int(end_value) <= int(v[0])) or
                                (int(start_value) >= int(v[1]) and int(end_value) > int(v[1])) or
                                (int(end_value) <= int(v[0]) and int(v[1]) == '')):
                            # Add record to tracker
                            if overlap_list.get(key_value):
                                overlap_list[key_value].update({
                                    line_count: [start_value, end_value]
                                })
                            else:
                                overlap_list.update({
                                    key_value: {
                                        line_count: [start_value, end_value]
                                    }
                                })
                            # Add existing key to tracker
                            overlap_list[key_value].update({
                                k: v
                            })
                    # Add record to checked list
                    key_check[key_value]['lines'].update({
                        line_count: [start_value, end_value]
                    })
            else:
                # First current version case
                if end_value == '':
                    key_check.update({
                        key_value: {
                            'lines': {line_count: [start_value, '']},
                            'has_current_version': True,
                            'current_version_line': line_count
                        }
                    })
                else:
                    key_check.update({
                        key_value: {
                            'lines': {line_count: [start_value, end_value]},
                            'has_current_version': False,
                            'current_version_line': None
                        }
                    })
            line_count += 1

        print(f'[{filename}]')
        for key in overlap_list.values():
            for entry in key:
                overlap_count += 1
        print('Number of version overlaps found:', overlap_count)

    # Check for overlaps in this file
    if overlap_count > 0:
        print('List of overlapping versions for keys and their index:', overlap_list)
    #     check_failed_flag = True
    #     failed_files.append(filename)

    return overlap_list

# Prints run status for file(s)
# if check_failed_flag:
#     print(f"Run ended. Version overlap found in dataset(s): {failed_files}")
#     sys.exit("Checks failed.")
# else:
#     print("Run ended. No overlaps found: Checks passed.")
