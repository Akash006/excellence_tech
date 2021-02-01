import argparse
import random

def sum_of_list(data: list) -> int:
    return sum(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sum of list of numbers')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--list", "-l", type=int, nargs="+", help="Enter numbers for a list eg: 1 2 3 4")
    group.add_argument("--random", "-r", type=int, help="Give the list length and numbers will be picked randomly eg: 5")
    args = parser.parse_args()

    if args.random:
        data = [ random.randrange(1, 100, 1) for x in range(args.random) ]
    else:
        data = args.list

    result = sum_of_list(data)
    print("Output: " , " + ".join(map(str, data)) , " = ", str(result))

    # ans = lambda data: sum(data)
    # print("Output: " , " + ".join(map(str, data)) , " = ", str(ans(data)))
    