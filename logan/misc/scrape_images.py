'''
import xml.parsers.expat as xml_parsers
from html.parser import HTMLParser, HTMLParseError
'''

import urllib
from HTMLParser import HTMLParser
from BeautifulSoup import BeautifulSoup

def beautiful(page):
    soup = BeautifulSoup(page)
    print soup.prettify()
    return soup


def gen_pages(max_page=300000):
    base_url = r"http://gatherer.wizards.com/Pages/Card"
    resource = "/Details.aspx?multiverseid={0}"

    for i in range(1, max_page):
        res = resource.format(i)
        f = urllib.urlopen(base_url + res)
        yield f.read()


def handle():
    for page in gen_pages(2):
        return beautiful(page)


if __name__ == "__main__":
    for page in gen_pages(2):
        beautiful(page)
