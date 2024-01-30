import json

class CertificateProfileGenerator:
    def __init__(self, template_file_path, parsed_data_file_path):
        self.template_data = self.load_json_file(template_file_path)
        self.parsed_data = self.load_json_file(parsed_data_file_path)
        self.update_template_with_parsed_values()

    def load_json_file(self, file_path):
        with open(file_path, 'r') as json_file:
            return json.load(json_file)

    def update_template_with_parsed_values(self):
        keys_to_remove = []

        for key, value in self.template_data.items():
            should_print = value.get("print", True)

            if not should_print:
                keys_to_remove.append(key)
                continue

            args = value.get("args", [])
            for arg in args:
                xml_name = arg.get("xml_name", "")
                xml_name = str(xml_name)
                result = self.get_parsed_value(xml_name)
                position = arg.get("position", None)
                encode_value = arg.get("encode_value", None)
                prefix = arg.get("prefix", None)
                print(result)


                if result is not None:
                    arg["raw_value"] = result
                    if xml_name == 'type':
                        position = result
                    if xml_name == "93" and isinstance(result, int) and result == -1:
                        result = "True"
                        prefix = "Unlimited"
                    if position is not None:
                        if position == 999:
                            if isinstance(result, list) and all(
                                    isinstance(item, dict) and 'value' in item for item in result):
                                result = ', '.join(str(item['value']) for item in result)
                        else:
                            if isinstance(result, list):
                                result = result[position]['value']
                            if encode_value is not None:
                                result = [item["print_value"] for item in encode_value if
                                                   item["value"] == position]

                    result_str = "`" + str(result) + "`"

                    if prefix is not None:
                        result_str = prefix + ": " + result_str

                    arg["parsed_value"] = result_str

                    # Remove unwanted keys
                    arg.pop("encode_value", None)
                    arg.pop("xml_name", None)
                    arg.pop("position", None)
                    arg.pop("raw_value", None)
                    arg.pop("prefix", None)

                    if prefix == "Use" or prefix == "Available" and result == False:
                        break

            value["args"] = [arg for arg in value["args"] if "parsed_value" in arg]

        for key in keys_to_remove:
            del self.template_data[key]


    def get_parsed_value(self, xml_name):
        return self.parsed_data.get(xml_name, None)

    def save_updated_template(self, output_file_path):
        with open(output_file_path, 'w') as output_file:
            json.dump(self.template_data, output_file, indent=2)

if __name__ == "__main__":
    result_json_generator = CertificateProfileGenerator('../template/certprofile_template.json', 'certprofile_parsed.json')
    result_json_generator.save_updated_template('updated_certprofile_template.json')
