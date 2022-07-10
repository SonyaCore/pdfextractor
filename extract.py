#!/bin/env python3
import PyPDF2

class PdfExtract():
    def __init__(self,book,output,pages):
        self.book = open(book,'rb')
        self.reader = PyPDF2.PdfFileReader(self.book)

        if not pages:
            pages = len(self.reader.pages)

        for x in range(pages):
            page = self.reader.getPage(x)
            with open(output,'a') as obj:
                obj.write(page.extractText())

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
    args = parser.parse_args()
    PdfExtract(args.name,args.output,args.pages)
