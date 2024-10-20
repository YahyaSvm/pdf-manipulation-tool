import os
import argparse
import PyPDF2
import logging
from PyPDF2.errors import PdfReadError

# © 2024 Yahyaldye. All rights reserved. This code is provided as-is and may not be reproduced without permission.

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def embed_exe_in_pdf(pdf_path, exe_path):
    logging.info("Embedding .exe file into PDF...")
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            writer = PyPDF2.PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            with open(exe_path, "rb") as exe_file:
                exe_data = exe_file.read()
                writer.add_metadata({'/EmbeddedFile': exe_data})

            new_pdf_path = f"modified_{os.path.basename(pdf_path)}"
            with open(new_pdf_path, "wb") as new_file:
                writer.write(new_file)

        logging.info(f".exe file '{exe_path}' successfully embedded. New file: {new_pdf_path}")
    except PdfReadError as e:
        logging.error(f"Error while reading PDF: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def add_command_to_pdf(pdf_path, command):
    logging.info("Adding command to PDF...")
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            writer = PyPDF2.PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            writer.add_metadata({'/Command': command})

            new_pdf_path = f"modified_{os.path.basename(pdf_path)}"
            with open(new_pdf_path, "wb") as new_file:
                writer.write(new_file)

        logging.info(f"Command '{command}' added to PDF. New file: {new_pdf_path}")
    except PdfReadError as e:
        logging.error(f"Error while reading PDF: {e}")
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

def add_url_to_pdf(pdf_path, url):
    logging.info("Adding URL to PDF... (functionality to be implemented)")

def extract_text_from_pdf(pdf_path):
    logging.info("Extracting text from PDF...")
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = []
            for page in reader.pages:
                text.append(page.extract_text())
            return "\n".join(text)
    except PdfReadError as e:
        logging.error(f"Error while reading PDF: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def main():
    setup_logging()
    parser = argparse.ArgumentParser(description="Advanced PDF manipulation tool")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("--url", help="URL to be added")
    parser.add_argument("--exe", help="Path to the .exe file to be embedded")
    parser.add_argument("--command", help="Command to be added")
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
        embed_exe_in_pdf(args.pdf_path, args.exe)
    elif args.command:
        add_command_to_pdf(args.pdf_path, args.command)
    else:
        logging.error("Please specify a URL, .exe file, command to add, or use --extract to extract text.")

if __name__ == "__main__":
    main()
