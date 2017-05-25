import copy
import yaml
from procedures import *


def build_test_info(test_num, test_args, test_arg_names, test_valid_results, test_result):
    """
    Build and return string describing the test in a legible form, given the information of the test
    """
    # Determine if test was successful or not
    test_info = "Fail. "
    if test_result in test_valid_results:
        test_info = "Success! "
    # Add test number
    test_number = "Test #{} - ".format(test_num)
    test_info += test_number
    # Add info about the arguments of the test
    for arg, name in zip(test_args, test_arg_names):
        arg_info = "{}: {}, ".format(name, arg)
        test_info += arg_info
    # Add the expected results of the test
    expected_results_info = "Expected Answers: "
    for valid_result in test_valid_results:
        expected_results_info += "{}, ".format(valid_result)
    test_info += expected_results_info
    # Add returned result of the test
    proc_result = "Returned Answer: {}".format(test_result)
    test_info += proc_result
    return test_info


with open("procedure_info.yml", "r") as procedure_info:
    proc_data = yaml.load(procedure_info)

with open("tests.yml", "r") as tests_info:
    test_dict = yaml.load(tests_info)

for proc_info in proc_data:
    if proc_info['run']:
        proc_name = proc_info['procedure']
        algo_name = proc_info['name']
        procedure = globals()[proc_name]
        test_type = proc_info['type']
        arg_names = test_dict[test_type]['arg_names']
        tests = test_dict[test_type]['tests']
        print('"{}" Tests:'.format(algo_name))
        for index, test in enumerate(tests):
            # Duplicate all args so that mutable objects are not modified by the procedure
            original_args = test["args"]
            copied_args = map(copy.copy, original_args)
            valid_results = test["results"]
            returned_result = procedure(*copied_args)
            test_information = build_test_info(index + 1, original_args, arg_names, valid_results, returned_result)
            print(test_information)
        print()
