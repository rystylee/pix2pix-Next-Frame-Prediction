# To Create Dataset

1. Split movie to image sequence

```
python create_dataset.py data/XXX.mp4 data/XXX 30 png
```

2. Resize source images

```
python tools/process.py --input_dir data/XXX --operation resize --output_dir data/resized
```

3. Copy the file at step2
```
cp -r data/resized data/resized2
```

4. Delete image_0001.png of resized2 and image_xxxx.png(last image) of resized1

5. Rename the images

```
python rename.py data/resized
```

5. Combine resized 2 set of images

```
python tools/process.py --input_dir data/resized --b_dir data/resized2 --operation combine --output_dir data/combined
```

* Split into train/val set

```
python tools/split.py --dir data/combined
```

# Training

```
python pix2pix.py \
  --mode train \
  --output_dir dst_path \
  --max_epochs 200 \
  --input_dir data_path \
  --which_direction AtoB
```

# Generate image sequence

```
python generate.py json_path src_path dst_path num_itr
```

# Generate movie

1. combine
```
ffmpeg -r 30 -i %04d.png -vcodec libx264 -pix_fmt yuv420p -r 30 movie.mp4
```

2. Resize

```
ffmpeg -i movie.mp4 -vf scale=640:-1 m.mp4
```