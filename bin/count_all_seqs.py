#!/usr/bin/env python

import sys
import os
import os.path
import seq_util

if len(sys.argv) < 2:
       exit ('specify sequence')
directory = sys.argv[1]
for filenames in os.listdir(directory):
       input_file = open(os.path.join(directory, filenames))
       seq_count = seq_util.count_seqs(input_file)
       print filenames, seq_count
#directory = '/home/user/Documents/python/data/*.fasta'
#input = open(directory)
#seq_count = seq_util.count_seqs(inp)
#print seq_count, 'in',filename

