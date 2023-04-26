"""
    Description: Tests for version_overlap_check Python file

    Author: William Lee

"""

import os
from version_overlap_check import scan_file

BASE_PATH = os.path.abspath('.')

def test_scenario1():
    """Passing test for normal back-to-back versions
    """
    test1 = 0
    count = scan_file(BASE_PATH + '/tests/test_scenario1.csv', test1)
    print(test1)
    assert count == {}

def test_scenario2():
    """Passing test for first instance of current version
    """
    test2 = 0
    count = scan_file(BASE_PATH + '/tests/test_scenario2.csv', test2)
    assert count == {}

def test_scenario3():
    """Passing test for first instance of start and end version
    """
    test3 = 0
    count = scan_file(BASE_PATH + '/tests/test_scenario3.csv', test3)
    assert count == {}

def test_scenario4():
    """Failing test for [ (] ) overlap
    """
    test4 = 0
    count = scan_file(BASE_PATH + '/tests/test_scenario4.csv', test4)
    assert count == {
        'UK': {1: ['2', '4'], 2: ['1', '3']},
        'US': {3: ['3', '7'], 4: ['1', '5']},
        'FR': {5: ['2', '3'], 6: ['1', '3']}
    }

def test_scenario5():
    """Failing test for ( [) ] overlap
    """
    test5 = 0
    count = scan_file(BASE_PATH + '/tests/test_scenario5.csv', test5)
    assert count == {
        'UK': {1: ['1', '3'], 2: ['2', '4']},
        'US': {3: ['1', '5'], 4: ['3', '7']},
        'FR': {5: ['1', '3'], 6: ['2', '3']}
    }

def test_scenario6():
    """Failing test for ([ ]) overlap
    """
    test6 = 0
    count = scan_file(BASE_PATH + '/tests/test_scenario6.csv', test6)
    assert count == {
        'UK': {1: ['1', '4'], 2: ['2', '3']},
        'US': {3: ['2', '10'], 4: ['4', '8'], 5: ['5', '6']},
        'FR': {6: ['1', '10'], 7: ['8', '10']},
        'SG': {8: ['2', '10'], 9: ['2', '7']}
    }

def test_scenario7():
    """Failing test for [( )] overlap
    """
    test7 = 0
    count = scan_file(BASE_PATH + '/tests/test_scenario7.csv', test7)
    assert count == {
        'UK': {1: ['2', '3'], 2: ['1', '4']},
        'US': {3: ['5', '6'], 4: ['4', '8'], 5: ['2', '10']},
        'FR': {6: ['8', '10'], 7: ['1', '10']},
        'SG': {8: ['2', '7'], 9: ['2', '10']}
    }

def test_scenario8():
    """Failing test for current version overlap with new current version
    """
    test8 = 0
    count = scan_file(BASE_PATH + '/tests/test_scenario8.csv', test8)
    assert count == {
        'UK': {1: ['1', 99999], 2: ['1', 99999]},
        'US': {3: ['1', 99999], 4: ['22', 99999]},
        'FR': {5: ['2', 99999], 6: ['5', 99999]},
        'SG': {7: ['1', 99999], 8: ['33', 99999], 9: ['2', 99999]}
    }

def test_scenario9():
    """Failing test for current version overlap before start of ranges (range first)
    """
    test9 = 0
    count = scan_file(BASE_PATH + '/tests/test_scenario9.csv', test9)
    assert count == {
        'UK': {1: ['10', '11'], 2: ['1', 99999]},
        'US': {3: ['4', '5'], 4: ['3', 99999]},
        'FR': {5: ['12', '20'], 6: ['12', 99999]}
    }

def test_scenario10():
    """Failing test for current version overlap before start of ranges (current version first)
    """
    test10 = 0
    count = scan_file(BASE_PATH + '/tests/test_scenario10.csv', test10)
    assert count == {
        'UK': {1: ['1', 99999], 2: ['10', '11']},
        'US': {3: ['3', 99999], 4: ['4', '5']},
        'FR': {5: ['12', 99999], 6: ['12', '20']}
    }

def test_scenario11():
    """Failing test for current version overlap after start of ranges (range first)
    """
    test11 = 0
    count = scan_file(BASE_PATH + '/tests/test_scenario11.csv', test11)
    assert count == {
        'US': {3: ['4', '8'], 4: ['7', 99999]},
        'FR': {5: ['12', '20'], 6: ['13', 99999]}
    }

def test_scenario12():
    """Failing test for current version overlap after start of ranges (current version first)
    """
    test12 = 0
    count = scan_file(BASE_PATH + '/tests/test_scenario12.csv', test12)
    assert count == {
        'US': {3: ['7', 99999], 4: ['4', '8']},
        'FR': {5: ['13', 99999], 6: ['12', '20']}
    }

def test_scenario13():
    """Passing test for having a range before a current version (range first)
    """
    test13 = 0
    count = scan_file(BASE_PATH + '/tests/test_scenario13.csv', test13)
    assert count == {}

def test_scenario14():
    """Passing test for having a range before a current version (current version first)
    """
    test14 = 0
    count = scan_file(BASE_PATH + '/tests/test_scenario14.csv', test14)
    assert count == {}

def test_scenario15():
    """Passing test for having a range before a current version (current version first)
    """
    test15 = 0
    count = scan_file(BASE_PATH + '/tests/test_scenario15.csv', test15)
    assert count == {
        'UK': {3: ['7', 99999], 4: ['10', '11']},
        'FR': {8: ['1', '5'], 9: ['2', '3'], 11: ['3', '4']}
    }

def test_scenario16():
    """Passing test for having a range before a current version (current version first)
    """
    test16 = 0
    count = scan_file(BASE_PATH + '/tests/test_scenario16.csv', test16)
    assert count == {
        'UK': {4: 'Invalid start value'},
        'FR': {9: 'Invalid start value'}
    }

def test_scenario17():
    """Passing test for having a range before a current version (current version first)
    """
    test17 = 0
    count = scan_file(BASE_PATH + '/tests/test_scenario17.csv', test17)
    assert count == {
        'UK': {4: 'Start value greater than end value'},
        'FR': {9: 'Start value greater than end value'}
    }

# def test_scenario():
#     """Test for passing case, normal back-to-back versions
#     """
#     test = 0
#     count = scan_file(BASE_PATH + '/tests/test_scenario.csv', test)
#     assert count == {
#         'UK': {},
#         'US': {},
#         'FR': {},
#         'SG': {}
#     }
