import sys, argparse

parser = argparse.ArgumentParser(
    description='Plot a family tree')
    
parser.add_argument('name',
    help="name of the individual",
    type=str)
    
parser.add_argument('-b', '--born', 
    help="birth year of the individual",
    default=None,
    type=str)

parser.add_argument('-d', '--depth', 
    help="depth of search",
    default=3,
    type=int)

parser.add_argument('-l', '--links', 
    help="provide links",
    default=False,
    type=bool)

