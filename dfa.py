import sys;
import argparse;
from run import runDFA;

parser = argparse.ArgumentParser(
    description='Python DFA Implementation'
);

parser.add_argument(
    '-d',
    '--dfaFileName',
    help='File containing input string (.json or .dfa file extension)',
    required=True
);

parser.add_argument(
    '-i',
    '--inputFileName',
    help='File containing new line seperated input strings',
    required=False
);

parser.add_argument(
    '-interactive',
    '--interactive',
    help='Interactive mode',
    required=False,
    action='store_true',
);

parser.add_argument(
    '-v',
    '--verbose',
    help='Verbose Mode; displaying machine definition, transitions, etc',
    required=False,
    action='store_true'
);

parser.add_argument(
    'inputList',
    help='Pipe in text from stdin',
    nargs="*",
    default=sys.stdin
);

args = vars(parser.parse_args());

if args['inputFileName'] != None:
    runDFA(args['dfaFileName'], args['inputFileName'], None, args['verbose'], False);
elif args['interactive']:
    runDFA(args['dfaFileName'], args['inputFileName'], None, args['verbose'], True);
elif args['inputList']:
    inputs = [line.strip() for line in args['inputList']];
    runDFA(args['dfaFileName'], args['inputFileName'], inputs, args['verbose'], False);