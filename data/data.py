#!/bin/env python3
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter
from colorama import Fore

import logging
logger = logging.getLogger("PyPDF2")
logger.setLevel(logging.ERROR)

class PdfExtract():
    def __init__(self,book,output):
        self.book = open(book,'rb')
        self.reader = PyPDF2.PdfFileReader(self.book)
        self.writer = PdfWriter()
        self.output = output

    def PDF_define_pages(self,pages):
        """Extracting Pages of the PDF"""
        if not pages:
            pages = self.reader.getNumPages()

        for number in range(pages):
            page = self.reader.getPage(number)
            with open(self.output,'a') as obj:
                obj.write(page.extractText())

    def Getmetadata(self):
        """Getting the Metadata of the PDF"""
        metainfo = PdfReader(self.book)
        meta = metainfo.metadata
        print(f"{Fore.GREEN}Author:{Fore.RESET} {meta.author}")
        print(f"{Fore.GREEN}Creator:{Fore.RESET} {meta.creator}")
        print(f"{Fore.GREEN}Producer:{Fore.RESET} {meta.producer}")
        print(f"{Fore.GREEN}Subject:{Fore.RESET} {meta.subject}")
        print(f"{Fore.GREEN}Title:{Fore.RESET} {meta.title}")

    def encrypt_pdf(self,password='123'):
        """encrypt pdf with password (not complete)"""
        self.writer = PdfWriter()

        self.writer.encrypt(password)

        with open(f"{self.book}.encrypt", "wb") as encrypted:
            self.writer.write(encrypted)
    
    def decrypt_pdf(self,password='123'):
        """decrypt pdf with password (not complete)"""

        if self.reader.is_encrypted:
            self.reader.decrypt(password)

        # Add all pages to the writer
        for page in self.reader.pages:
            self.writer.add_page(page)

        # Save the new PDF to a file
        with open("decrypted-pdf.pdf", "wb") as f:
            self.writer.write(f)
