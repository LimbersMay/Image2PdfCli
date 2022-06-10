#!/usr/bin/python

import argparse
from pathlib import Path
from sys import stderr
from conversion import *


class CpException(Exception):
    pass


def convert_image_to_pdf(src: Path, dest: Path, single=False, group=False, one=False, name='merged'):
    
    print('source ->', src.absolute())
    print('Destination', dest.absolute())
    print(name)

    # We define the object to convert the Png images into Jpg images
    convert_png_to_jpg = PngToJpg(str(src.absolute()), str(dest.absolute()))

    # Object to convert Jpg files to PDF files
    convert_pdf = ImgToPdf(str(src.absolute()), str(dest.absolute()))

    # Convert png files to jpg files
    

    if single and not group: 
        convert_png_to_jpg.realizar_conversion_unica()
        convert_pdf.conversion_unico()    

    elif group and one:
        # Convert the images to onefile PDF
        convert_png_to_jpg.realizar_conversion()
        convert_pdf.convertir_unido(name)
    
    elif group and not one:
        # Convert the images in separe files
        convert_png_to_jpg.realizar_conversion()
        convert_pdf.convertir_separado()
    

def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='img-to-pdf',
        description='Convertir imagen a PDF'
    )

    parser.add_argument(
        'source',
        type=Path,
        help='Directory where the image file are'
    )

    parser.add_argument(
        'destination',
        type=Path,
        help='Destination directory where the image file will be converted into PDF'
    )

    parser.add_argument(
        '-n', '--name',
        type=str,
        default='merge',
        help='Name of the merged file PDF'
    )

    parser.add_argument(
        '-s',
        '--single',
        default=True,
        action='store_true',
        help='Convert only one file into PDF'
    )

    parser.add_argument(
        '-g',
        '--group',
        action='store_true',
        help='Convert a group image files into pdf'
    )

    parser.add_argument(
        '-o',
        '--one',
        action='store_true',
        help='Merge all the pdf files into one file'
    )

    return parser.parse_args()


def main():
    args = cli()
    try:
        convert_image_to_pdf(args.source, args.destination, args.single, args.group, args.one, args.name)
        print("Convertion sucefully..!!")
    
    except CpException as e:
        print(e, file=stderr)
        exit(1)


if __name__=='__main__':
    main()