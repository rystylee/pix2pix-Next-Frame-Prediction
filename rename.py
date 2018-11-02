import os
import glob
import argparse


def rename(input_dir, format):
    files = files = glob.glob(input_dir + '/*')
    for i, f in enumerate(files):
        os.rename(f, os.path.join(input_dir, '{0:04d}'.format(i)) + '.' + format)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir', type=str)
    args = parser.parse_args()

    rename(args.input_dir, 'png')