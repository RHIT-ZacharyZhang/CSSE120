"""
This module tests   m5_calling_functions_returning_values.
You do NOT need to understand all of the code in this module,
but you should be able to pass all of its tests.

Authors: Mark Hays and others.  December 2014.
"""
##############################################################
# Do not change this file, it is intended only as a way to check
# your code.
##############################################################

import m5_calling_functions_returning_values as m4
import sys
from io import StringIO


def main():
    """ Calls the   TEST   functions in this module. """
    test_print_it()
    test_return_it()
    test_digits_in_squares_and_cubes()
    test_digits_in_power()


######################################################################
# Do not worry about understanding the code below this line. It is
# used to cleanly test your code, but you are not expected to
# understand how it work sat this point.
######################################################################
def test_print_it():
    """ Tests the   print_it   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   print_it   function:')
    print('--------------------------------------------------')
    testCases = TestCaseCollection()
    testCases.addTestCase([10], None, "1\n", [10])
    testCases.addTestCase([2], None, "19084\n", [2])
    testCases.addTestCase([35], None, "124309\n", [35])
    runTestOnMethod(m4.print_it, testCases, "print_it")


def test_return_it():
    """ Tests the   return_it   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   return_it   function:')
    print('--------------------------------------------------')
    testCases = TestCaseCollection()
    testCases.addTestCase([10], 1, "", [10])
    testCases.addTestCase([2], 19084, "", [2])
    testCases.addTestCase([35], 124309, "", [35])
    runTestOnMethod(m4.return_it, testCases, "return_it")


def test_digits_in_squares_and_cubes():
    """ Tests the   digits_in_squares_and_cubes   function. """
    print()
    print('-----------------------------------------------------')
    print('Testing the   digits_in_squares_and_cubes   function:')
    print('-----------------------------------------------------')
    testCases = TestCaseCollection()
    testCases.addTestCase([12], None, "12 3\n144 9\n1728 18\n", [12])
    runTestOnMethod(m4.digits_in_squares_and_cubes, testCases,
                    "digits_in_squares_and_cubes")


def test_digits_in_power():
    """ Tests the   digits_in_power   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   digits_in_power   function:')
    print('--------------------------------------------------')
    testCases = TestCaseCollection()
    testCases.addTestCase([12, 3], 18, "", [12, 3])
    runTestOnMethod(m4.digits_in_power, testCases, "digits_in_power")


def runTestOnMethod(function, testCases, function_name):
    numTests = len(testCases.expectedPrints)
    total = numTests * 2 + (len(testCases.args[0]) * numTests)
    resultsToPrint = ""
    correct = 0
    old_stdout = sys.stdout
    try:
        for k in range(numTests):
            sys.stdout = mystdout = StringIO()
            ep = testCases.expectedPrints[k]
            er = testCases.expectedReturns[k]
            ea = testCases.expectedArgumentsAfter[k]
            argList = testCases.args[k]
            actualReturn = None
            if (len(argList) == 0):
                actualReturn = function()
            elif (len(argList) == 1):
                actualReturn = function(argList[0])
            elif (len(argList) == 2):
                actualReturn = function(argList[0], argList[1])

            actualPrint = mystdout.getvalue()

            if (actualReturn == er):
                correct += 1
            else:
                resultsToPrint += "Failure with arguments: " + str(testCases.args[k]) + "\nReturn value of " + str(actualReturn) + " did not match expected value of " + str(er) + "\n"

            if (actualPrint == ep):
                correct += 1
            else:
                resultsToPrint += "Failure with arguments: " + str(testCases.args[k]) + "\nPrinted value of \n" + str(actualPrint) + "\n did not match expected value of \n" + str(ep) + "\n"

            for i in range(len(testCases.args[k])):
                if (testCases.args[k][i] == ea[i]):
                    correct += 1
                else:
                    resultsToPrint += "Failure with arguments: " + str(testCases.args[k]) + "\nArgument value of " + str(testCases.args[k][i]) + " did not match expected value of " + str(ea[i]) + "\n"

        sys.stdout = old_stdout
        # print(functionName, "Total:", str(correct) + "/" + str(total))

        print(resultsToPrint)
    except Exception as e:
        sys.stdout = old_stdout
        print("Exception occurred while executing test: ", e)
    finally:
        sys.stdout = old_stdout
    if correct == total:
        print(function_name, "COMPLETED SUCCESSFULLY!")
        return True
    print(function_name, "FAILED! See messages above.")
    return False


class TestCaseCollection():

    def __init__(self):
        self.expectedReturns = []
        self.expectedPrints = []
        self.expectedArgumentsAfter = []
        self.args = []

    def addTestCase(self, arguments, expectedReturn, expectedPrint,
                    expectedArgsAfter):
        self.args.append(arguments)
        self.expectedReturns.append(expectedReturn)
        self.expectedPrints.append(expectedPrint)
        self.expectedArgumentsAfter.append(expectedArgsAfter)

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
