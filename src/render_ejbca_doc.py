import json

class MarkdownGenerator:
    def __init__(self, input_file_path, output_file_path):
        self.data = self.load_json_file(input_file_path)
        self.output_file_path = output_file_path
        self.generate_markdown_table()

    def load_json_file(self, file_path):
        with open(file_path, 'r') as json_file:
            return json.load(json_file)

    def generate_markdown_table(self):
        with open(self.output_file_path, 'w') as markdown_file:
            markdown_file.write("| Name | Description |\n")
            markdown_file.write("| --- | --- |\n")

            for key, value in self.data.items():
                pretty_name = value.get("pretty_name", "")
                args = value.get("args", [])

                if args:
                    parsed_values = "<br>".join(arg.get("parsed_value", "") for arg in args)
                    markdown_file.write(f"| {pretty_name} | {parsed_values} |\n")
                else:
                    markdown_file.write(f"| {pretty_name} | |\n")

if __name__ == "__main__":
    markdown_generator = MarkdownGenerator('updated_certprofile_template.json', 'output_table.md')
