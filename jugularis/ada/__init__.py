
import argparse
import logging
import os
from ppci import ir, api
from textx.metamodel import metamodel_from_file

this_dir = os.path.dirname(os.path.abspath(__file__))

def main():
    print('Compiling ada')

    ada_mm = metamodel_from_file(os.path.join(this_dir, 'ada83.tx'))

    parser = argparse.ArgumentParser()
    parser.add_argument('source')
    args = parser.parse_args()

    ast = ada_mm.load(args.source)
