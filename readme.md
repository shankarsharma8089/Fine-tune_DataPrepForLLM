CSV/PDF to JSONL Converter (Prompt-Completion Pairs)

This Streamlit app allows you to easily convert CSV and PDF files into JSONL format, suitable for generating prompt-completion pairs. Whether you have structured data in CSV format or textual data in a PDF document, this app simplifies the process of creating structured prompts and completions.

Usage
Upload a File: You can upload either a CSV or a PDF file by clicking the "Upload a CSV or PDF file" button.

Conversion: After uploading the file, the app will handle the conversion based on the file type.

For PDF files, it extracts text from the PDF and converts it into prompt-completion pairs.

For CSV files, it reads the data, processes it, and generates prompt-completion pairs based on the data structure.

Download JSONL: Once the conversion is completed, you can download the generated JSONL file containing prompt-completion pairs.

How It Works
For PDF files, the app uses the PyPDF2 library to extract text from each page, assuming data is structured as key: value pairs.

For CSV files, the app reads the binary content of the file, decodes it to text, and processes the data to create prompt-completion pairs.

Installation
Before running the app, make sure to install the required libraries:

bash
Copy code
pip install streamlit PyPDF2
Running the App
You can run the app using the following command:

bash
Copy code
streamlit run app.py
Replace app.py with the name of your script.

Contributing
Feel free to contribute to this project by submitting issues, feature requests, or pull requests.

License
This project is licensed under the MIT License.

You can place this README in the root directory of your project, and it will provide clear instructions on how to use and contribute to your CSV/PDF to JSONL Converter app.
