# Certificate Profile and End Entity Profile to Markdown Processing

This Repository provides functionality for processing Certificate Profiles and End Entity Profiles. It consists of three main functions for parsing XML data, converting it to JSON, and generating Markdown documentation.

## Table of Contents

- [Requirements](#requirements)
- [Usage](#usage)
- [Functions](#functions)
    - [MarkdownGenerator](#markdowngenerator)
    - [XMLToJsonConverter](#xmltojsonconverter)
    - [CertificateProfileGenerator](#certificateprofilegenerator)

## Requirements

- Python 3.x

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/FHatCSW/ejbca_docparser.git
    cd ejbca_docparser
    ```

2. Install dependencies (if any):

    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:

    ```bash
    python main.py
    ```

## Functions

### MarkdownGenerator

This class generates a Markdown table based on input JSON data. It loops through the JSON data and constructs a table with names and descriptions.
### XMLToJsonConverter

This class is responsible for converting XML data to JSON format. It uses the ElementTree library to parse the XML and recursively converts elements and values.

### CertificateProfileGenerator

This class generates and updates a certificate profile template based on parsed data. It involves loading template and parsed data, updating template values, and saving the updated template to a new file.