import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--fname',
                    type=str,
                    required=True)
args = parser.parse_args()

if not os.path.exists('../../' + args.fname):
    raise FileNotFoundError('Csv not saved to expected path')
    sys.exit(1)
elif not os.stat('../../' + args.fname).st_size > 1:
    raise ValueError('Csv generated smaller than expected')
    sys.exit(1)
else:
    print('Found')