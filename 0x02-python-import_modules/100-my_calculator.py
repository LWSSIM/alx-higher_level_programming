#!/usr/bin/python3
# this script uses calculator_1.py module
# perform simple arithmetics when called

import sys
import calculator_1
if __name__ == "__main__":
    ac = len(sys.argv)
    if ac == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op_list = {
            '+': calculator_1.add,
            '-': calculator_1.sub,
            '*': calculator_1.mul,
            '/': calculator_1.div
        }
        if sys.argv[2] in op_list:
            result = op_list[sys.argv[2]](a, b)
            print("{0} {1} {2} = {3}".format(a, sys.argv[2], b, result))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
