import argparse

import os
import glob

import tensorflow as tf
import numpy as np
from PIL import Image

from predictor import Predictor


def generate_img(predictor, src_path, dst_path):
    img_in = np.array(Image.open(src_path), dtype='f')
    img_in = img_in / 255.

    img_predicted = predictor.predict(img_in)[0]
    img_predicted = img_predicted * 255.

    img_out = Image.fromarray(np.uint8(img_predicted))
    img_out.save(dst_path)

    os.remove(src_path)
    img_out.save(src_path)


def generate_img_recursive(predictor, src_path, dst_path, num_itr):
    for i in range(num_itr):
        src = glob.glob(src_path + '/*')[0]
        dst = os.path.join(dst_path + '/', '{0:04d}'.format(i)) + '.png'
        generate_img(predictor, src, dst)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('json_path', type=str)
    parser.add_argument('input_dir', type=str)
    parser.add_argument('output_dir', type=str)
    parser.add_argument('num_itr', type=int)
    args = parser.parse_args()

    if not os.path.isdir(args.output_dir):
        os.mkdir(args.output_dir)

    predictor = Predictor(json_path=args.json_path)

    generate_img_recursive(predictor, args.input_dir, args.output_dir, args.num_itr)
