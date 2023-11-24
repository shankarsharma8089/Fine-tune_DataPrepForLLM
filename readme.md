# CSV/PDF to JSONL Converter (Streamlit App)

## Overview
This Streamlit app allows you to convert both CSV and PDF files into JSONL format, specifically designed for creating prompt-completion pairs. These pairs are commonly used for natural language processing (NLP) tasks.

## Well-Known Models Using Prompt-Completion Approach

### GPT (Generative Pre-trained Transformer) Series:
- GPT-2
- GPT-3
- GPT-4 (if released in the future)

These models, developed by OpenAI, are known for their ability to generate coherent and contextually relevant text based on a given prompt.

### T5 (Text-To-Text Transfer Transformer):
- T5, developed by Google, is designed as a text-to-text model where both the input and output are treated as text strings. This allows for a unified approach to various natural language processing tasks.

### Babbage and Curie:
- Babbage and Curie are models developed by EleutherAI. These models are part of the GPT-inspired language model series and are designed for large-scale language generation tasks.

### InstructGPT:
- InstructGPT, also developed by OpenAI, is a variant of GPT-3 that is fine-tuned using an instruction-based approach. It is specifically trained to follow instructions in prompts.

### ChatGPT:
- ChatGPT, another model from OpenAI, is fine-tuned for conversational interactions. While not explicitly prompt-completion, it shares similarities in handling user inputs as prompts and generating responses.

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


