import streamlit as st
import io
import csv
import PyPDF2
import json

# Function to generate prompts based on the dataset structure
def generate_prompts(header, row):
    prompt = ""
    for key, value in zip(header, row):
        prompt += f"{key.strip()}: {value.strip()}\n"
    completion = json.dumps(dict(zip(header, row)))  # Convert the row data to JSON for completion
    return {"prompt": prompt, "completion": completion}

# Main Streamlit app
st.title("CSV/PDF to JSONL Converter(prompt-completion pairs)")

# Upload a file
file = st.file_uploader("Upload a CSV or PDF file", type=["csv", "pdf"])

if file is not None:
    if file.type == "application/pdf":
        # Handle PDF file
        with st.spinner("Converting PDF to JSONL..."):
            input_pdf_file = file
            output_jsonl_file = 'fine_tune_info.jsonl'

            pdf_reader = PyPDF2.PdfReader(input_pdf_file)
            data = ""
            for page_num in range(len(pdf_reader.pages)):
                data += pdf_reader.pages[page_num].extract_text()

            jsonl_line = json.dumps(generate_prompts([], data))
            with open(output_jsonl_file, 'w', encoding='utf-8') as jsonl_file:
                jsonl_file.write(jsonl_line + '\n')

        st.success(f'Conversion completed. JSONL data saved to {output_jsonl_file}')

        # Allow the user to download the JSONL file
        st.download_button(
            label="Download JSONL",
            data=jsonl_line,
            key='jsonl-download'
        )

    elif file.type == "text/csv":
        # Handle CSV file
        with st.spinner("Converting CSV to JSONL..."):
            input_csv_file = file
            output_jsonl_file = 'fine_tune_info.jsonl'

            # Read the binary content of the CSV file and decode it to text
            content = input_csv_file.read().decode('utf-8')
            csv_reader = csv.reader(io.StringIO(content))  # Use io.StringIO

            header = next(csv_reader)

            data = ""
            for row in csv_reader:
                jsonl_line = json.dumps(generate_prompts(header, row))
                data += jsonl_line + '\n'

            with open(output_jsonl_file, 'w', encoding='utf-8') as jsonl_file:
                jsonl_file.write(data)

        st.success(f'Conversion completed. JSONL data saved to {output_jsonl_file}')

        # Allow the user to download the JSONL file
        st.download_button(
            label="Download JSONL",
            data=data,
            key='jsonl-download'
        )

