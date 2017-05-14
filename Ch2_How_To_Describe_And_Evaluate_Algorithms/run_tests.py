from test_procedures import *

with open("tests_to_run", "r") as tests_to_run:
    for line in tests_to_run:
            line = line.strip()
            if line:
                test, should_run = line.split(":")
                if should_run == "true":
                    globals()[test]()
