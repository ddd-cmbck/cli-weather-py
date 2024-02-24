from api import OperationCLI

if __name__ == '__main__':
    cli = OperationCLI()
    cli.parse_arguments()
    cli.perform_operation()




