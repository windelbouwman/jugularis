
""" Convert llvm-ir to ppci-ir using textx """

import logging
import ppci
import argparse
from textx.metamodel import metamodel_from_file
from textx.exceptions import TextXSyntaxError


def main():
    logger = logging.getLogger('conv')
    mm = metamodel_from_file('llvm.tx')

    parser = argparse.ArgumentParser()
    parser.add_argument('source')
    args = parser.parse_args()

    logformat = '%(asctime)s | %(levelname)8s | %(name)10.10s | %(message)s'
    logging.basicConfig(level=logging.INFO, format=logformat)
    logger.info('Go with %s', ppci)

    try:
        logger.info('Loading %s', args.source)
        m = mm.model_from_file(args.source)
        print(m)
    except TextXSyntaxError as e:
        logger.error('%s', str(e))
        print_error(args.source, e)


def print_error(filename, error):
    """ Print a nicely formatted error """
    with open(filename, 'r') as f:
        lines = f.readlines()
    for row in range(error.line - 5, error.line + 5):
        if row - 1 in range(len(lines)):
            line = lines[row - 1].strip()
            print('{:5}: {}'.format(row, line))
        if row == error.line:
            padding = ' '*(error.col + 6)
            print('{}^ {}'.format(padding, error))


if __name__ == '__main__':
    main()
