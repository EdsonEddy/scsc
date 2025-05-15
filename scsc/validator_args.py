import argparse

# Validate arguments
def validate_arguments(args):
    if args.method == 'shingling':
        if args.window <= 0:
            raise argparse.ArgumentError(None, "--window must be greater than 0.")
    elif args.window is not None:
        raise argparse.ArgumentError(None, "--window is only allowed when --method is 'shingling'.")