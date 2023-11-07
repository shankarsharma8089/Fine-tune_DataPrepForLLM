# CSV/PDF to JSONL Converter (Streamlit App)

## Overview
This Streamlit app allows you to convert both CSV and PDF files into JSONL format, specifically designed for creating prompt-completion pairs. These pairs are commonly used for natural language processing (NLP) tasks.

## Features
- Upload CSV or PDF files for conversion.
- Automatically detects the file type (CSV or PDF) and processes it accordingly.
- For PDF files, text extraction is handled using the PyPDF2 library.
- For CSV files, data is processed, and JSONL files are generated.
- Users are provided with a download link to access the converted JSONL files.

## Usage
1. Upload your CSV or PDF file.
2. Wait for the conversion process to complete (a spinner indicates the progress).
3. Once finished, you'll receive a success message with a download link to access the converted JSONL file.

## Dependencies
- Streamlit
- PyPDF2
- json
- io
- csv

## How to Run
1. Install the required dependencies using pip.
2. Run the Streamlit app with the command `streamlit run app.py`, where `app.py` is the filename of your application.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgements
- Built using Streamlit, a fantastic library for creating web apps with ease.

Feel free to contribute, report issues, or make enhancements to this project.

