import argparse
from PyPDF2 import PdfReader


def load_spelling_differences(file_path):
    spelling_differences = {}
    with open(file_path, 'r') as file:
        for line in file:
            if ',' not in line:
                continue  # Skip lines without a comma
            american, british = line.strip().split(',')
            spelling_differences[american] = british
    return spelling_differences

def read_pdf(file_path, spelling_differences):
    pdf_reader = PdfReader(file_path)
    num_pages = len(pdf_reader.pages)
    found_words = []
    for page_number, page in enumerate(pdf_reader.pages):
        text = page.extract_text().lower()
        for american, british in spelling_differences.items():
            if american in text:
                found_words.append((american, british, page_number))
    return found_words


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find American spellings in a PDF.')
    parser.add_argument('-d', '--differences', required=True, help='Path to the spelling differences file.')
    parser.add_argument('-f', '--file', required=True, help='Path to the PDF file.')
    parser.add_argument('-o', '--offset', required=False, help='Offset page number by this amount.', default=0)
    args = parser.parse_args()

    spelling_differences = load_spelling_differences(args.differences)
    found_words = read_pdf(args.file, spelling_differences)
    offset = int(args.offset)

    for american, british, page in found_words:
        print(f'Word "{american}" found on page {page+1 - offset} - consider change to "{british}"')
