# arguments are of 2 types here - positional, optional
# in optional arguments -- will be used while parsing arguments, few arguments can be skipped

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", help = "firstnumber")
    parser.add_argument("--number2" , help = "secondnumber")
    parser.add_argument("--operation" , help = "operation")

    args = parser.parse_args()

    print(args.number1)
    print(args.number2)
    print(args.operation)

    n1 = int(args.number1)
    n2 = int(args.number2)
    result  = None

    if args.operation == "add":
        result = n1 + n2
    elif args.operation == "substract":
        result = n1 - n2
    elif args.operation == "multiply":
        result = n1 * n2
    else:
        print("unsupported")

    print(result)
