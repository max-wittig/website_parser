from website_parser import WebsiteParser
from parser_properties import ParserProperties
from website_generator import WebsiteGenerator

"""extracts tags from website and generates new website
from these tags"""


def main():
    properties = ParserProperties()
    properties.source_url = "https://news.ycombinator.com/news"
    properties.tags_to_download = ["a"]
    parser = WebsiteParser(properties)
    generator = WebsiteGenerator()
    generator.generate(parser.html_tags_dict)

if __name__ == "__main__":
    main()
