from driver.test_B_F1_1 import B_F1_1
from driver.test_B_F1_2 import B_F1_2
from driver.test_B_F1_3 import B_F1_3

from driver.test_B_F2_1 import B_F2_1
from driver.test_B_F2_2 import B_F2_2
from driver.test_B_F2_3 import B_F2_3

from driver.test_B_NF import B_NF
from base import Dataframe


### >>> Feature-id format
## > The format contains 4 parts: a-b-c-d
    # + a: The website we need to test in project 2. At the project 2 tasks, with id `A` for website (https://github.com/amirhamza05/Student-Management-System) while id `B`  for website (https://moodle.org/demo). But in this project for Assignment 3, this just supports id `B`
    # + b: The id feature/usecase/requirement we need to test. In task B, we just have id for requirements:
    #     - F1: Functional requirement about Login System
    #     - F2: Functional requirement about Change Password System
    #     - NF: Non-functional requirement about Change profile picture performance (do not have {c} pattern)
    # + c: The id of method that we want to test
    #     - 1: Usecase Testing Method
    #     - 2: Decision Table Based Method / Equivalence Class Testing Method
    #     - 3: Boundary Value Method
    # + d: Have format xxx is the id of testcase in each method. Eg: 001,002,...


## > To be specific: https://docs.google.com/spreadsheets/d/1-fAsovGVbdBcPLErWYU9T6JNXvR9A_W8/edit?usp=sharing&ouid=106303221635045723836&rtpof=true&sd=true | Sheet: Test Case Summary
# B-F1-1-xxx: Login system - Usecase Testing Method  (001-002)
# B-F1-2-xxx: Login System - Decision Table Based Method (001-004)
# B-F1-3-xxx: Login System - Boundary Value Method (001-005)

# B-F2-1-xxx: Change Password System - Usecase Testing Method (001-006)
# B-F2-2-xxx: Change Password System - Equivalence Class Testing Method (001-004)
# B-F2-3-xxx: Change Password System - Boundary Value Method (001-007)

# B-NF-xxx: Change profile picture performance (001-004)
### >>> 


def main(feature, io, sheet, skiprows):
    try:
        test = eval(f"{feature.replace('-','_').replace('.','_')}()")
        DF = Dataframe()
        DF.read_excel(io=f'test-data/{io}',
                      sheet_name=sheet, skiprows=skiprows)
        result = test.run(DF.storage[sheet])
        DF.write_result(result)
        return
    except:
        raise Exception('Can not load the feature')

    # if feature == 'B-F5.1':
    #     test = B_F5_1()
    # elif feature == 'B-F5.2':
    #     test = B_F5_2()


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('--feature', metavar='path', required=True)
    parser.add_argument('--io', metavar='path', required=True)
    parser.add_argument('--sheet', metavar='path', required=True)
    parser.add_argument('--skiprows', metavar='path')

    [feature, io, sheet, skiprows] = [arg[1]
                                      for arg in parser.parse_args()._get_kwargs()]
    if not skiprows:
        skiprows = 0

    main(feature, io, sheet, int(skiprows)) 