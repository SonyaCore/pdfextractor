#!/usr/bin/env python3
import argparse
from data.pdf import *
from data.encrypt import encrypt_pdf , decrypt_pdf 

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

    encryptparser = parser.add_argument_group( 'Encryption' )
    
    encryptparser.add_argument(
        "--encrypt",
        "-e",        
        action='store_true',
        required=False,
        help='\t\tEncrypt PDF'
    )
    encryptparser.add_argument(
        "--decrypt",
        "-d",        
        action='store_true',
        required=False,
        help='\t\tDecrypt PDF'
    )
    encryptparser.add_argument(
        "--password",
        "-pass",
        action="store",
        default='123',
        type=str,
        nargs="?",
        help="\tSet Password",
    )
    args = parser.parse_args()
    try:
        extract = PdfExtract(args.name,args.output)
        
        if args.output:
            extract.ExtractPDF(args.pages)

        if args.metadata == True:
            extract.Getmetadata()

        if args.encrypt == True:
            encrypt_pdf(args.name,args.password)
            print(f"{args.name} encrypted")

        elif args.decrypt == True:
            decrypt_pdf(args.name,args.password)
            print(f"{args.name} decrypted")

    except FileNotFoundError:
        print(f'{args.name} Not Found!')
    except IndexError:
        print(f'{args.pages} Defined Pages are Bigger than Actual Book Page')

    finally:
        if  args.pages:
            print(f"\n{args.name} {args.pages} number of pages written to {args.output}")
        elif args.output:
            print(f"\n{args.name} all pages written to {args.output}")
