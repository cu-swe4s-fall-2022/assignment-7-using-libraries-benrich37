import argparse
import sys
import os
mainpath = os.path.join(os.path.dirname(__file__), '../../')
sys.path.append(mainpath)
import data_processor

parser = argparse.ArgumentParser()
parser.add_argument('--row',
                    type=int,
                    required=True)
parser.add_argument('--col',
                    type=int,
                    required=True)
parser.add_argument('--fname',
                    type=str,
                    required=True)
args = parser.parse_args()

data_processor.write_matrix_to_file(
    args.row, args.col, '../../' + args.fname)
