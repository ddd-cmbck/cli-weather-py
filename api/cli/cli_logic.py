from argparse import ArgumentParser


class OperationCLI:
    def __init__(self):

        # Initialize the parser
        self.args = None
        self.parser = ArgumentParser(usage='Use it like this. ')

        # Set up arguments
        self.setup_arguments()

    def setup_arguments(self):
        # Configuration of command line arguments
        self.parser.add_argument('a', type=int, help='The base value')
        self.parser.add_argument('b', type=int, help='The exponent')
        self.parser.add_argument('-v', '--verbose', action='count',
                                 help='Provides a verbose description. Use -vv for extra verbose')

    def parse_arguments(self, args_list=None):
        self.args = self.parser.parse_args(args_list)

    def perform_operation(self):
        # Perform the calculation based on parsed arguments
        result = self.args.a ** self.args.b

        # Handle verbosity
        if self.args.verbose == 1:
            print(f'The result is {result}')
        elif self.args.verbose == 2:
            print(f'{self.args.a}^ {self.args.b} = {result}')
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
