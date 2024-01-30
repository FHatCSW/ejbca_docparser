import json
import xml.etree.ElementTree as ET


class XMLToJsonConverter:
    def __init__(self, xml_file_path):
        self.xml_file_path = xml_file_path

    def convert_element_to_dict(self, element):
        result = {}
        for child in element:
            result["value"] = self.convert_element_to_dict(child) if len(child) > 0 else self.convert_value(child)
        return result

    def convert_value(self, element):
        if element is not None:
            if element.tag == 'string':
                return element.text
            elif element.tag == 'boolean':
                return element.text.lower() == 'true'
            elif element.tag == 'float':
                return float(element.text)
            elif element.tag == 'int':
                return int(element.text)
            elif element.tag == 'long':
                return int(element.text)  # You might need to handle long values differently based on your requirements
            elif element.tag == 'object':
                return [self.convert_element_to_dict(obj) for obj in element.findall('void')]
        return None

    def parse_xml_to_json(self, profile_type: str = 'cp'):
        print(
            profile_type
        )
        if profile_type not in ['ee', 'cp']:
            raise ValueError("Invalid value for 'type'. Allowed values are 'ee' or 'cp'.")

        try:
            with open(self.xml_file_path, 'r') as xml_file:
                xml_content = xml_file.read()
                root = ET.fromstring(xml_content)
                result_dict = {}

                for void_element in root.findall('.//void'):
                    if profile_type is "cp":
                        lead_elements = void_element.findall('string')
                        sec_arg = "int"
                    else:
                        lead_elements = void_element.findall('int')
                        sec_arg = "string"

                    if len(lead_elements) >= 1:
                        key = lead_elements[0].text
                        value_element = None
                        boolean_elements = void_element.findall('boolean')
                        float_elements = void_element.findall('float')
                        long_elements = void_element.findall('long')
                        object_elements = void_element.findall('object')
                        sec_elements = void_element.findall(sec_arg)


                        if len(lead_elements) > 1:
                            value_element = lead_elements[1]

                        if len(boolean_elements) > 0:
                            value_element = boolean_elements[0]

                        if len(float_elements) > 0:
                            value_element = float_elements[0]

                        if len(sec_elements) > 0:
                            value_element = sec_elements[0]

                        if len(long_elements) > 0:
                            value_element = long_elements[0]

                        if len(object_elements) > 0:
                            value_element = object_elements[0]

                        result_dict[key] = self.convert_value(value_element)

                return result_dict
        except FileNotFoundError:
            print(f"Error: The file '{self.xml_file_path}' not found.")
            return None

    def convert_xml_to_json(self, output_json_path='parse_xml.json', profile_type: str = 'cp'):
        json_data = self.parse_xml_to_json(profile_type)

        if json_data is not None:
            json_str = json.dumps(json_data, indent=2)
            with open(output_json_path, 'w') as json_file:
                json_file.write(json_str)
            print(f"Successfully converted XML to JSON. Result saved in '{output_json_path}'")


if __name__ == "__main__":
    converter = XMLToJsonConverter(xml_file_path='../map/test.xml')  # Replace with the actual XML file path
    converter.convert_xml_to_json()
