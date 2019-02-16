#!/usr/bin/env python

# 1. load a dataset from files
# 2. organize the data
# 3. summary statistics
# 4. print results
from argparse import ArgumentParser
parser = ArgumentParser(description="parser")
parser.add_argument("filename", help='path to the file')
args = parser.parse_args()
filename = args.filename


print("you enter", filename)

import pandas as pd
data = pd.read_csv(filename, sep='\s+|,', header=None)
print(data.head())

