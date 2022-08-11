#!/bin/env python3
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter

import logging
logger = logging.getLogger("PyPDF2")
logger.setLevel(logging.ERROR)

class PdfExtract():
    def __init__(self,book,output):
        self.book = open(book,'rb')
        self.reader = PyPDF2.PdfFileReader(self.book)
        self.writer = PdfWriter()
        self.output = output

    def PDF_define_pages(self,pages=0):
        """Defining the Total Number of Pages for Extraction"""
        for number in range(pages):
            page = self.reader.getPage(number)
            with open(self.output,'a') as obj:
                obj.write(page.extractText())

    def PDF_all_pages(self):
        """Extracting all Pages of PDF"""
        for totalnumber in range(self.reader.getNumPages()):
            page = self.reader.getPage(totalnumber)
            with open(self.output,'a') as obj:
                obj.write(page.extractText())

    def Getmetadata(self):
        """Getting the Metadata of the PDF"""
        metainfo = PdfReader(self.book)
        meta = metainfo.metadata
        print(f"Author: {meta.author}")
        print(f"Creator: {meta.creator}")
        print(f"Producer: {meta.producer}")
        print(f"Subject: {meta.subject}")
        print(f"Title: {meta.title}")

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
