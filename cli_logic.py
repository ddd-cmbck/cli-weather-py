from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

parser.usage = 'Use it like this. '

parser.add_argument('a', type=int, help='The base value')
parser.add_argument('b', type=int, help='The exponent')
parser.add_argument('-v', '--verbose', action='count',
                    help='Provides a verbose description. Use -vv for extra verbose')

args: Namespace = parser.parse_args()

result: int = args.a ** args.b

if args.verbose == 1:
    print(f'The result is {result}')
elif args.verbose == 2:
    print(f'{args.a}^ {args.b} = {result}')
else:
    print(result)
    """


parser = ArgumentParser()

parser.add_argument('square', help='Squares a given number', type=int, default=0, nargs='?')
parser.add_argument('-v', '--verbose',
                    help='Verbose description. Use -vv for extra verbose',
                    action='count')

args: Namespace = parser.parse_args()

result: int = args.square ** 2


if args.verbose ==  1:
    print(f'The result is {result}')
elif args.verbose == 2:
    print(f'{args.square} ** {args.square} = {result}')
else:
    print(result)
"""
