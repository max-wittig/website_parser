class WebsiteGenerator:
    def __init__(self, properties):
        self.init_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
"""
        self.end_html = """
</body>
</html>
"""
        self.between_html = ""
        self.output_filename = properties.output_filename
        self.html = None

    def generate(self, html_tags_dict):
        for key in html_tags_dict:
            for element in html_tags_dict[key]:
                self.add_dom_element(element)
        self.build_website()
        self.save_website()

    def add_dom_element(self, dom_element_string):
        self.between_html += str(dom_element_string)

    def build_website(self):
        self.html = self.init_html + self.between_html + self.end_html

    def save_website(self):
        if self.html is not None:
            with open(self.output_filename, "w") as f:
                f.write(self.html)
