import argparse
import os

from src.generate_content import CertificateProfileGenerator
from src.parse_xml import XMLToJsonConverter
from src.render_ejbca_doc import MarkdownGenerator

def parse_certprofile(xml_file_path):
    pass

def parse_endentity(xml_file_path):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process Certificate Profiles and End Entity Profiles.')
    parser.add_argument('xml_file', help='Path to the XML file to be processed')

    args = parser.parse_args()

    xml_file_path = args.xml_file

    if not xml_file_path.endswith('.xml'):
        print("Error: Please provide a valid XML file.")
        exit(1)

    if not os.path.exists(xml_file_path):
        print(f"Error: The file '{xml_file_path}' not found.")
        exit(1)

    script_name = os.path.basename(__file__)
    profile_type = 'cp' if 'certprofile' in script_name else 'ee'

    if profile_type == 'cp':
        parse_certprofile(xml_file_path)
    else:
        parse_endentity(xml_file_path)
