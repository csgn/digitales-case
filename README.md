# Digitales Helmet Detector


```
$ virtualenv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
```

```sh
# Download the model
$ wget "https://drive.google.com/file/d/1EXwzD1GBmJd9pxJG7ygYTYNX4ZoC1myw" -O best.pt
```

```sh
$ python run_inference.py --model <model.pt> --source_path <source.mp4>
```

```sh
$ python split_video.py --source_path datasets/helmet5.mp4 --output_path output_frame/ --interval 60 # each 60 frame
```
