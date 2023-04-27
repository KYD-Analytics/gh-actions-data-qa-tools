"""
    Description: Checks for version overlap of keys in csv files
    Author: William Lee

"""
import csv

def scan_file(filename:str) -> tuple[int, dict]:
    """Checks input filename for overlaps in start and end versions

    Args:
        filename (str): name of the input file

    Returns:
        tuple: returns a count (int) and key + index of overlaps (dict)
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
            # Check if key exists in checked list
            if key_value in key_check:
                # Check if invalid start version (non-integer value)
                if not start_value.isdigit():
                    if overlap_list.get(key_value):
                        overlap_list[key_value].update({
                            line_count: 'Invalid start value'
                        })
                    else:
                        overlap_list.update({
                            key_value: {
                                line_count: 'Invalid start value'
                            }
                        })
                # Current version case (versions that have start values but no end values)
                elif end_value == '':
                    # Check if current version overlaps with an existing key in checked list
                    for k, v in key_check[key_value].items():
                        if int(start_value) < int(v[1]):
                            # Add current version to tracker list
                            if overlap_list.get(key_value):
                                overlap_list[key_value].update({
                                    line_count: [start_value, 99999]
                                })
                            else:
                                overlap_list.update({
                                    key_value: {
                                        line_count: [start_value, 99999]
                                    }
                                })
                            # Add existing key to tracker list
                            overlap_list[key_value].update({
                                k: v
                            })
                    # Add current version to checked list
                    key_check[key_value].update({
                        line_count: [start_value, 99999]
                    })
                # If start version is larger than end version, add to tracker list
                elif int(start_value) > int(end_value):
                    if overlap_list.get(key_value):
                        overlap_list[key_value].update({
                            line_count: 'Start value greater than end value'
                        })
                    else:
                        overlap_list.update({
                            key_value: {
                                line_count: 'Start value greater than end value'
                            }
                        })
                else:
                    for k, v in key_check[key_value].items():
                        # Check if record is within previous version ranges
                        if not ((int(start_value) < int(v[0]) and int(end_value) <= int(v[0])) or
                                (int(start_value) >= int(v[1]) and int(end_value) > int(v[1])) or
                                (int(end_value) <= int(v[0]) and v[1] == 99999)):
                            # Add record to tracker list
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
                            # Add existing key to tracker list
                            overlap_list[key_value].update({
                                k: v
                            })
                    # Add record to checked list
                    key_check[key_value].update({
                        line_count: [start_value, end_value]
                    })
            else:
                # First current version case
                if end_value == '':
                    key_check.update({
                        key_value: {
                            line_count: [start_value, 99999]
                        }
                    })
                else:
                    key_check.update({
                        key_value: {
                            line_count: [start_value, end_value]
                        }
                    })
            line_count += 1

        # Calculate counts for overlaps from tracker list
        print(f'[{filename}]')
        for key in overlap_list.values():
            overlap_count += len(key)
        print('Number of version overlaps found:', overlap_count)

    # Print keys and indices if overlaps exist
    if overlap_count > 0:
        print('List of overlapping versions for keys and their index:', overlap_list)

    return overlap_count, overlap_list
