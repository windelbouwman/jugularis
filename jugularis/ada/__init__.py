
import argparse
import logging
from ppci import ir, api
from textx.metamodel import metamodel_from_file


def main():
    print('Compiling ada')

    ada_mm = metamodel_from_file('ada83.tx')

    parser = argparse.ArgumentParser()
    parser.add_argument('source')
    args = parser.parse_args()

    ast = ada_mm.load(args.source)
