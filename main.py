#!/usr/bin/env python

"""
Script that takes a path to a file as an argument, and executes each line in that file with a thread a pool
equal in size to the cpu_count of the computer, thus fully utilizing the CPU.
"""

import multiprocessing
import sys
import subprocess

# This MUST be defined before the pool is created. refer to: 
# http://stackoverflow.com/questions/2782961/yet-another-confusion-with-multiprocessing-error-module-object-has-no-attribu
def process_line(line_command):
    subprocess.check_call(line_command, shell=True)
    
num_cpu = multiprocessing.cpu_count()
job_pool = multiprocessing.Pool(num_cpu)

# Fetch the commands file path which contains each command we wish to run on a separate line
cmds_fp = sys.argv[1]
lines = [line.strip() for line in open(cmds_fp, 'r')]

job_pool.map(process_line, lines)

