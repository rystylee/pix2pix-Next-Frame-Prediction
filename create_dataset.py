import subprocess
import argparse

def movie2img(src_path, dst_path, fps, format):
    cmd = 'ffmpeg -i ' + src_path + ' -vcodec ' + format + ' -r ' + fps + ' ' + dst_path + '/image_%04d.' + format
    print(cmd)
    subprocess.call(cmd.split())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('src_path', type=str)
    parser.add_argument('dst_path', type=str)
    parser.add_argument('fps', type=str)
    parser.add_argument('format', type=str)
    args = parser.parse_args()

    movie2img(args.src_path, args.dst_path, args.fps, args.format)