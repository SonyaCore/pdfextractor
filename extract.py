#!/bin/env python3
import PyPDF2
from PyPDF2 import PdfReader

import logging
logger = logging.getLogger("PyPDF2")
logger.setLevel(logging.ERROR)

class PdfExtract():
    def __init__(self,book,output,pages=0):
        self.book = open(book,'rb')
        self.reader = PyPDF2.PdfFileReader(self.book)

        for x in range(pages):
            page = self.reader.getPage(x)
            with open(output,'a') as obj:
                obj.write(page.extractText())

    def metadata(self):
        reader = PdfReader(self.book)
        meta = reader.metadata
        print(meta.author)
        print(meta.creator)
        print(meta.producer)
        print(meta.subject)
        print(meta.title)

if __name__ == "__main__":
    import argparse
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
        "--readmeta",
        "-r",        
        action='store_true',
        required=False,
        help='\t\tShow Metadata'
    )

    args = parser.parse_args()
    try:

        # Extract PDF
        argument = PdfExtract(args.name,args.output,args.pages)

        # Read Metadata
        if args.readmeta == True:
            PdfExtract.metadata(argument)

    except FileNotFoundError:
        print(f'{args.name} Not Found!')
    except IndexError:
        print(f'{args.pages} Defined Pages are Bigger than Actual Book Page')

    finally:
        print(f"{args.name} written to {args.output}")
