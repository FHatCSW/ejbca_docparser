from src.generate_content import CertificateProfileGenerator
from src.parse_xml import XMLToJsonConverter
from src.render_ejbca_doc import MarkdownGenerator
import os

def parse_certprofile():
    current_directory = os.path.dirname(os.path.abspath(__file__))

    cert_profile_xml_path = os.path.join(current_directory,
                                         'example/cert_profile/certprofile_OiPKI-TlsCert-TlsClient-01-149295302.xml')
    cert_profile_template = os.path.join(current_directory, 'src/template/certprofile_template.json')
    parsed_cert_profile = os.path.join(current_directory, 'example/cert_profile/parsed_cert_profile.json')
    cert_profile_json_path = os.path.splitext(cert_profile_xml_path)[0] + '.json'
    result = os.path.splitext(cert_profile_xml_path)[0] + '.md'

    converter = XMLToJsonConverter(cert_profile_xml_path)
    converter.convert_xml_to_json(cert_profile_json_path, profile_type="cp")

    result_json_generator = CertificateProfileGenerator(cert_profile_template, cert_profile_json_path)
    result_json_generator.save_updated_template(parsed_cert_profile)

    markdown_generator = MarkdownGenerator(parsed_cert_profile, result)

def parse_endentity():
    current_directory = os.path.dirname(os.path.abspath(__file__))

    endentity_profile_xml_path = os.path.join(current_directory,
                                              'example/endentity_profile/entityprofile_testprofile-parser-463064307 20.xml')
    endentity_profile_template = os.path.join(current_directory, 'src/template/endentity_profile_template.json')
    parsed_endentity_profile = os.path.join(current_directory, 'example/endentity_profile/parsed_endentity_profile.json')
    endentity_profile_json_path = os.path.splitext(endentity_profile_xml_path)[0] + '.json'
    result = os.path.splitext(endentity_profile_xml_path)[0] + '.md'

    converter = XMLToJsonConverter(endentity_profile_xml_path)
    converter.convert_xml_to_json(endentity_profile_json_path, profile_type= "ee")

    result_json_generator = CertificateProfileGenerator(endentity_profile_template, endentity_profile_json_path)
    result_json_generator.save_updated_template(parsed_endentity_profile)

    markdown_generator = MarkdownGenerator(parsed_endentity_profile, result)



if __name__ == "__main__":
    parse_endentity()
    parse_certprofile()
