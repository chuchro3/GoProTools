# -*- coding: utf-8 -*-
import os, sys
from shutil import copyfile

def merge_files(root_dir, dest_dir):
    '''
    Assuming the root_dir is constructed as follows:
    root_dir -> multiple sub_dir tiers -> image files to be merged
    '''
    file_counter = 0
    file_prefix = 'G'
    file_postfix = '.JPG'
    for sub_dir, _, files in os.walk(root_dir):
        num_files = len(files)
        if num_files == 0:
            continue
        print "copying", sub_dir, "with", num_files, "files."
        for i in range(0, num_files):
            src = sub_dir + '/' + files[i]
            dest = dest_dir + file_prefix + str(file_counter).zfill(7) + file_postfix
            #print dest
            copyfile(src, dest)
            file_counter += 1
            
            print_progress(i, num_files)

# Print iterations progress
def print_progress(iteration, total, prefix='', suffix='', decimals=1, bar_length=75):
    """
    Call in a loop to create terminal progress bar
    @params:
    iteration   - Required  : current iteration (Int)
    total       - Required  : total iterations (Int)
    prefix      - Optional  : prefix string (Str)
    suffix      - Optional  : suffix string (Str)
    decimals    - Optional  : positive number of decimals in percent complete (Int)
    bar_length  - Optional  : character length of bar (Int)
    """
    iteration += 1
    str_format = "{0:." + str(decimals) + "f}"
    percents = str_format.format(100 * (iteration / float(total)))
    filled_length = int(round(bar_length * iteration / float(total)))
    bar = '█' * filled_length + '-' * (bar_length - filled_length)

    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),

    if iteration == total:
        sys.stdout.write('\n\tDone.\n\n')
        sys.stdout.flush()


def read_command(argv):
    """
    Processes the command used to run openai gym from the command line.
    """
    from optparse import OptionParser
    usageStr = """
    USAGE:      python openai.py <options>
    EXAMPLES:   (1) python openai.py
                    - starts training on default environment and learning parameters
                (2) python openai.py -v MountainCar-v0 -b 30,30
                    - starts training on mountain car environment with bucket sizes for each of the (2) state space dimensions as 30
                (3) python openai.py --no-graphics
                    - starts training without graphics.
    """
    parser = OptionParser(usageStr)
    
    parser.add_option('-i', '--path', type='string', dest='root_dir', help=default('Root directory of merge'),
                        default='.')
    parser.add_option('-o', '--dest', type='string', dest='dest_dir', help=default('Path to write merged files'),
                        default='./')
 
    options, otherjunk = parser.parse_args(argv)
    assert len(otherjunk) == 0, "Unrecognized options: " + str(otherjunk)
    return vars(options)

def default(str):
    return str + ' [Default: %default]'

def parse_comma_separated_args(option, opt, value, parser):
    setattr(parser.values, option.dest, value.split(','))

if __name__ == '__main__':
    options = read_command(sys.argv[1:])
    merge_files(**options)
