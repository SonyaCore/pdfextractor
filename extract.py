#!/usr/bin/env python3
import argparse
from data.data import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='PDF Extractor')

    parser.add_argument(
        "--pages",
        "-p",
        action="store",
        default=0,
        type=int,
        nargs="?",
        help="\tSpecify Total Pages",
    )
    parser.add_argument(
        "--all",
        "-a",        
        action='store_true',
        required=False,
        help='\t\tExtract All Pages'
    )
    parser.add_argument(
        "--name",
        "-n",
        action="store",
        help='\tName of PDF',
    )
    parser.add_argument(
        "--output",
        "-o",
        action="store",
        help='\t\tOutput Name',
    )

    optionalparser = parser.add_argument_group( 'Optional Arguments' )

    optionalparser.add_argument(
        "--metadata",
        "-m",        
        action='store_true',
        required=False,
        help='\t\tShow Metadata'
    )

    args = parser.parse_args()
    try:
        if args.pages:
            PdfExtract(args.name,args.output).PDF_define_pages(args.pages)
        elif args.all:
            PdfExtract(args.name,args.output).PDF_all_pages()

        if args.metadata == True:
            PdfExtract(args.name,args.output).Getmetadata()

    except FileNotFoundError:
        print(f'{args.name} Not Found!')
    except IndexError:
        print(f'{args.pages} Defined Pages are Bigger than Actual Book Page')

    finally:
        if  args.pages:
            print(f"\n{args.name} {args.pages} number of pages written to {args.output}")
        if  args.all == True:
            print(f"\n{args.name} all pages written to {args.output}")