# qr-reader
Simple command-line QR code reader.

Usage:
```lang-none
python qr_reader.py path/to/image.jpg
```

Text read from the QR code is then printed to stdout as-is (no final newline added).

Required packages are listed in `requirements.txt`

Image files must be readable by `cv2.imread(...)`.
Documentation for that can be found [here](https://docs.opencv.org/4.5.5/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56)
