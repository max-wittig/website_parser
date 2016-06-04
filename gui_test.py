from tkinter import *
from website_parser import WebsiteParser
from parser_properties import ParserProperties
from website_generator import WebsiteGenerator


def main():
    top = Tk()
    website_label = Label(top, text="website:")
    website_input = Entry(top)
    website_label.pack(side=TOP)
    website_input.pack(side=TOP)

    tag_label = Label(top, text="tags:")
    tag_input = Entry(top)
    tag_input.pack(side=BOTTOM)
    tag_label.pack(side=BOTTOM)

    do_button = Button(top, text="GO", command=lambda: do_button_call_back(website_input.get(), tag_input.get()))
    do_button.pack(side=BOTTOM)
    top.mainloop()


def do_button_call_back(url, tags_string):
    properties = ParserProperties()
    properties.source_url = url
    properties.tags_to_download = str(tags_string).split(' ')
    properties.output_filename = "index.html"
    parser = WebsiteParser(properties)
    generator = WebsiteGenerator(properties)
    generator.generate(parser.html_tags_dict)

if __name__ == '__main__':
    main()
