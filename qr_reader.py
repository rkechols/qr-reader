import argparse
import sys

import cv2


if __name__ == "__main__":
    # get the file path
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("qr_image_path", type=str)
    args, _ = arg_parser.parse_known_args()
    qr_image_path = args.qr_image_path
    print(f"loading image from {qr_image_path}", file=sys.stderr)
    # load the image
    image = cv2.imread(qr_image_path)
    # read the image as a QR code
    detector = cv2.QRCodeDetector()
    data_str, _, _ = detector.detectAndDecode(image)
    # print the text
    print(data_str, end="")
