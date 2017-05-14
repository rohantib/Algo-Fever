import procedures


def linear_search_test():
    tests = [
        {"args": ([1, 2, 3], 3, 2), "results": [1]},
        {"args": ([5, 2, 9, 1, 5], 5, 5), "results": [0, 4]},
        {"args": ([19028, 378193, 91789472, 28383728], 4, 91789472), "results": [2]},
        {"args": ([2], 1, 3), "results": ["NOT-FOUND"]},
        {"args": ([9, 2, 5, 7, 1, 4], 6, 10), "results": ["NOT-FOUND"]},
        {"args": ([3, 4, 1, 2, 8], 5, 8), "results": [4]}
             ]
    print('"Linear Search" Tests: ')
    for index, test in enumerate(tests):
        args = test["args"]
        valid_results = test["results"]
        test_result = procedures.linear_search(*test["args"])
        test_info = "Test #{} - Array: {}, Search Query: {}, Expected Answers: {}, Returned Answer: {}".format(
            index + 1, args[0], args[2], valid_results, test_result)
        if test_result in valid_results:
            print("Success!", test_info)
        else:
            print("Fail.", test_info)
    print()


def better_linear_search_test():
    tests = [
        {"args": ([1, 2, 3], 3, 2), "results": [1]},
        {"args": ([5, 2, 9, 1, 5], 5, 5), "results": [0, 4]},
        {"args": ([19028, 378193, 91789472, 28383728], 4, 91789472), "results": [2]},
        {"args": ([2], 1, 3), "results": ["NOT-FOUND"]},
        {"args": ([9, 2, 5, 7, 1, 4], 6, 10), "results": ["NOT-FOUND"]},
        {"args": ([3, 4, 1, 2, 8], 5, 8), "results": [4]}
             ]
    print('"Better Linear Search" Tests: ')
    for index, test in enumerate(tests):
        args = test["args"]
        valid_results = test["results"]
        test_result = procedures.better_linear_search(*test["args"])
        test_info = "Test #{} - Array: {}, Search Query: {}, Expected Answers: {}, Returned Answer: {}".format(
            index + 1, args[0], args[2], valid_results, test_result)
        if test_result in valid_results:
            print("Success!", test_info)
        else:
            print("Fail.", test_info)
    print()


def sentinel_linear_search_test():
    tests = [
        {"args": ([1, 2, 3], 3, 2), "results": [1]},
        {"args": ([5, 2, 9, 1, 5], 5, 5), "results": [0, 4]},
        {"args": ([19028, 378193, 91789472, 28383728], 4, 91789472), "results": [2]},
        {"args": ([2], 1, 3), "results": ["NOT-FOUND"]},
        {"args": ([9, 2, 5, 7, 1, 4], 6, 10), "results": ["NOT-FOUND"]},
        {"args": ([3, 4, 1, 2, 8], 5, 8), "results": [4]}
             ]
    print('"Better Linear Search" Tests: ')
    for index, test in enumerate(tests):
        args = test["args"]
        valid_results = test["results"]
        test_result = procedures.sentinel_linear_search(*test["args"])
        test_info = "Test #{} - Array: {}, Search Query: {}, Expected Answers: {}, Returned Answer: {}".format(
            index + 1, args[0], args[2], valid_results, test_result)
        if test_result in valid_results:
            print("Success!", test_info)
        else:
            print("Fail.", test_info)
    print()
