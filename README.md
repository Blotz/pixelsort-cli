# Pixel Sorter

A simple python command line tool for sort pixels in an image.
Based on the works of [Kim Asendorf](https://github.com/kimasendorf/ASDFPixelSort).

The script blocks pixels into dark and light areas using a contrast mask.
Then it sorts the pixels in a given direction via their luminance.

- You can increase/decrease the contrast by setting the threshold.
- You can also invert the mask to sort the light pixels instead of the dark ones.

## Usage

### Install

```bash
pip install git+https://github.com/Blotz/pixelsorter
```

## Examples

```bash
pixelsorter --help
```

```bash
usage: Pixel Sorter [-h] [--threshold THRESHOLD] [--invert INVERT] [--reverse_sorting REVERSE_SORTING] [--output OUTPUT] image_path {up,down,left,right}

Command line tool for sorting pixels

positional arguments:
  image_path            path to image
  {up,down,left,right}  direction to sort pixels

options:
  -h, --help            show this help message and exit
  --threshold THRESHOLD
                        threshold for contrast
  --invert INVERT       invert the selected area
  --reverse_sorting REVERSE_SORTING
                        reverse the sorting direction
  --output OUTPUT       path to output file
```

```bash
pixelsorter  data/mountains.jpg right --threshold 0.7 --invert True --output out.png
```

![example 1](https://raw.githubusercontent.com/Blotz/pixelsorter/main/data/example1.png)

---

## License

MIT Ferdinand Theil
