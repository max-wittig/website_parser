from website_parser import WebsiteParser
from parser_properties import ParserProperties
from website_generator import WebsiteGenerator


def main():
    properties = ParserProperties()
    properties.source_url = "http://www.golem.de/"
    properties.tags_to_download = ["img", "h2"]
    parser = WebsiteParser(properties)
    generator = WebsiteGenerator()
    generator.generate(parser.html_tags_dict)

if __name__ == "__main__":
    main()
