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
    expected_results_info = "Expected Answers: {}, ".format(test_valid_results)
    test_info += expected_results_info
    # Add returned result of the test
    proc_result = "Returned Answer: {}".format(test_result)
    test_info += proc_result
    return test_info


with open("tests.yml", "r") as tests:
    test_data = yaml.load(tests)

for procedure_data in test_data:
    if procedure_data['run']:
        proc_name = procedure_data['procedure']
        algo_name = procedure_data['name']
        procedure = globals()[proc_name]
        arg_names = procedure_data['arg_names']
        tests = procedure_data['tests']
        print('"{}" Tests:'.format(algo_name))
        for index, test in enumerate(tests):
            args = test["args"]
            valid_results = test["results"]
            returned_result = procedure(*args)
            test_information = build_test_info(index + 1, args, arg_names, valid_results, returned_result)
            print(test_information)
        print()
