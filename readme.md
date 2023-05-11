# Text Replacement Finder

This script identifies specific words or phrases in a PDF document and suggests their replacements based on a provided dictionary of replacements.

## Motivation

Writing a report with other people will most likely cause some words being written differently. For instance some people writing in american english rather than british. This script will make it easier to find these errors and correct them.

## Usage

This script requires two arguments:

- `-d` or `--differences`: The path to a text file containing words or phrases to be replaced. Each line of this file should contain a target word or phrase, followed by a comma, followed by the replacement word or phrase (e.g., `target,replacement`).

- `-p` or `--pdf_file`: The path to the PDF document in which you want to find the target words or phrases.

Here's an example of how to call this script:

```bash
python script.py -d words.txt -p document.pdf
```
