"""
    Description: Tests for version_overlap_check Python file

    Author: William Lee

"""

import os
from version_overlap_check import scan_file

BASE_PATH = os.path.abspath('.')

def test_scenario1():
    test1 = {}
    count = scan_file(BASE_PATH + '/tests/test_scenario1.csv', test1)
    print(test1)
    assert count == 6
