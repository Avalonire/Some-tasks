from hw_4_2345 import currency_rates


def main(argv):
    program, args = argv
    print(currency_rates(args))


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
