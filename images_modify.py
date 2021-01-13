#!/usr/bin/env python

import os
import argparse
from PIL import Image

def images_modify(orig_im, dest_im):
    """Transform images located in argv[1] and save them in argv[2].
       The script expects the original images in tiff format, 192x192 pixel and
       90° anti-clockwise wrong oriented.
       It returns the images in jpeg format, 128x128 pixel and stright.
       The script expects the images are simply in a folder and does not take into account
       subfolders.
    """
    
    # Create the destination folder if it does't exist.
    if not os.path.exists(dest_im):
        os.mkdir(dest_im)

    # Generate the list with the image names to be transformed.
    images = os.listdir(orig_im)
    
    for image in images:
        try:
            with Image.open(os.path.join(orig_im,image)) as im:
                im.resize((128,128)).rotate(-90).convert('RGB').save(os.path.join(dest_im, image), 'JPEG')
        except OSError:
            print("Image {} was not transformed.".format(os.path.abspath(os.path.join(orig_im, image))))



if __name__ == '__main__':
    # If the script is run alone accetps command line input.
    parser = argparse.ArgumentParser(
            description='Transform Images from TIFF 192x192 into rotated JPEG 128x128.')
    parser.add_argument('-i', type=str, dest='inp', required=True,
            help='Input directory containing the images to transform.')
    parser.add_argument('-o', type=str, dest='out', required=True,
            help='Output directory where to save the converted images.')
    args = parser.parse_args()
    images_modify(args.inp, args.out)
