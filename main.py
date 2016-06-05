#!/usr/bin/python3
"""
extracts tags from website and generates new website
from these tags

----------USAGE----------

-h --help                   show this help-page
-s --source <arg>           specify source_url                      e.g. -s https://www.github.com
-t --tags '<arg1> <arg..n>' specify html tags to get from page      e.g. -t "img p h1 h2"
-o --output <arg>           specify output filename                 e.g. -o index.html
-d --debug                  inserts test values in required fields
-------------------------
"""

import getopt
import sys
from website_parser import WebsiteParser
from parser_properties import ParserProperties
from website_generator import WebsiteGenerator


def print_user_error():
    print(__doc__)
    print("source and tags are required parameter")
    sys.exit(0)


def main():
    properties = ParserProperties()
    properties.output_filename = "index.html"
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:t:o:d",
                                   ["help", "source=", "tags=", "output=", "debug"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        sys.exit(2)

    for o, a in opts:
        if o in ("-h", "--help"):
            print(__doc__)
            sys.exit(0)
        elif o in ("-s", "--source"):
            properties.source_url = a
        elif o in ("-t", "--tags"):
            properties.tags_to_download = a.split(' ')
        elif o in ("-o", "--output"):
            properties.output_filename = a
        elif o in ("-d", "--debug"):
            properties.source_url = "https://devhumor.com/"
            properties.tags_to_download = ["img", "h2"]
        else:
            assert False, "unhandled option"

    """end program if required parameters aren't given"""
    if properties.source_url is None or len(properties.tags_to_download) < 1:
        print_user_error()

    parser = WebsiteParser(properties)
    generator = WebsiteGenerator(properties)
    generator.generate(parser.html_tags_dict)

if __name__ == "__main__":
    main()
