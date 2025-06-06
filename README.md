# pixelsort cli

[![tests](https://github.com/Blotz/pixelsort-cli/actions/workflows/python-package.yml/badge.svg)](https://github.com/Blotz/pixelsort-cli/actions/workflows/python-package.yml)
[![package](https://github.com/Blotz/pixelsort-cli/actions/workflows/python-publish.yml/badge.svg)](https://github.com/Blotz/pixelsort-cli/actions/workflows/python-publish.yml)
[![CodeQL](https://github.com/Blotz/pixelsort-cli/actions/workflows/codeql.yml/badge.svg)](https://github.com/Blotz/pixelsort-cli/actions/workflows/codeql.yml)

A simple python command line tool for sort pixels in an image.
Based on the works of [Kim Asendorf](https://github.com/kimasendorf/ASDFPixelSort).

The script blocks pixels into dark and light areas using a contrast mask.
Then it sorts the pixels in a given direction via their luminance.

- You can increase/decrease the contrast by setting the threshold.
- You can also invert the mask to sort the light pixels instead of the dark ones.

## Usage

### Install

```bash
pip install git+https://github.com/Blotz/pixelsort-cli
```

or

```bash
pip install pixelsort-cli
```

or

```bash
git clone https://github.com/Blotz/pixelsort-cli
cd pixelsort-cli
pip install .
```

## Examples

```bash
pixelsort --help
```

```bash
usage: pixelsort [-h] [--angle ANGLE] [--image_path IMAGE_PATH] [--threshold THRESHOLD | --template_path TEMPLATE_PATH]
                 [--sort_brightest SORT_BRIGHTEST] [--reverse_sorting REVERSE_SORTING] [--output OUTPUT] [--verbose | --quiet]
                 [stdin]

Command line tool for sorting pixels in images

positional arguments:
  stdin

options:
  -h, --help            show this help message and exit
  --angle ANGLE         angle that the image is sorted. 0° is up. [0, 360]
  --image_path IMAGE_PATH
                        path to image
  --threshold THRESHOLD
                        threshold for contrast. [-1.0, 1.0] Default: 1.0
  --template_path TEMPLATE_PATH
                        path to template image
  --sort_brightest SORT_BRIGHTEST
                        Sort the brightest area of the image. Default: True
  --reverse_sorting REVERSE_SORTING
                        Sorts the pixels from lightest to darkest instead of darkest to lightest. Default: False
  --output OUTPUT       path to output file
  --verbose             print debug messages
  --quiet               print less messages
```

```bash
pixelsort --image_path data/mountains.jpg --threshold 1.2 | display
```

![example 1](https://raw.githubusercontent.com/Blotz/pixelsort-cli/main/data/example1.png)

```bash
cat data/mountains.jpg | pixelsort --template_path data/pyramid_mask.png | display
```

![example 2](https://raw.githubusercontent.com/Blotz/pixelsort-cli/main/data/example2.png)

```bash
pixelsort --image_path data/mountains.jpg --angle 30 --threshold 1.2 --output example.png
```

![example 3](https://raw.githubusercontent.com/Blotz/pixelsort-cli/main/data/example3.png)

Use it with other tools like imagemagick
```bash
magick data/mountains.jpg -colorspace gray PNG:- | pixelsort | display
```

![example 4](https://raw.githubusercontent.com/Blotz/pixelsort-cli/main/data/example4.png)


---

## License

MIT Ferdinand Theil
