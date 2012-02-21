import urllib
from BeautifulSoup import BeautifulSoup, Tag
import re
import os
import shelve

def beautiful(page):
    soup = BeautifulSoup(page)
    print soup.prettify()
    return soup


def save_image(n, path='images'):
    base_url = r"http://gatherer.wizards.com/Handlers"
    resource = "/Image.ashx?multiverseid={0}&type=card"
    res = base_url + resource
    res = res.format(n)
    urllib.urlretrieve(res, os.path.join(os.curdir, path, str(n)))


def get_page(n):
    base_url = r"http://gatherer.wizards.com/Pages/Card"
    resource = "/Details.aspx?multiverseid={0}"
    res = base_url + resource
    res = res.format(n)
    return urllib.urlopen(res).read()


def get_all_sets(soup):
    tag = 'All Sets:'
    ret = {}
    try:
        container = soup.find(text=re.compile(tag)).parent.parent
    except AttributeError:
        ret = None
    else:
        for element in container.contents:
            if type(element) == Tag and element['class'] == 'value':
                target = element
        for element in target.contents:
            if type(element) == Tag:
                for e in element.contents:
                    if type(e) == Tag:
                        key = e['href'].split(u'=')[-1]
                        val = e.contents[0]['title']
                        ret[key] = val
    return ret


def get_details(soup):
    tags = ['Card Name:', 'Converted Mana Cost:', 'Types:', 'Card Text:', 'Expansion:',
            'Rarity:', 'Artist:', 'Flavor Text:', 'Card #:']
    # Note: 'Mana Cost:' isn't in this list because the page reports those in terms of
    # images. While it's possible to grab that data, it would require a bit of work and
    # doesn't appear to have any immediate benefits.

    details_dict = {}
    for tag in tags:
        try:
            k, v = unicode(soup.find(text=re.compile(tag)).parent.parent.getText()).split(u':')[-2:]
        except AttributeError:
            k, v = unicode(tag), None
        details_dict[k] = v
    details_dict[u'ALl Sets'] = get_all_sets(soup)

    return details_dict


def get_soup(n):
    return BeautifulSoup(get_page(n))


class Handler(object):
    def __init__(self):
        self.card_shelve = shelve.open('card_shelve')
        self.redo_list = shelve.open('redo_list')

    def close(self):
        self.card_shelve.close()
        self.redo_list.close()

    def handle(self):
        for n in range(1, 30000):
            try:
                soup = get_soup(n)
                if soup.find(text=re.compile("Card Details Table")):
                    self.card_shelve[str(n)] = get_details(soup)
                    save_image(n)
            except Exception as e:
                print "Problem on " + str(n)
                self.redo_list[str(n)] = False
        self.close()


if __name__ == "__main__":
    #soup = get_soup(6)
    #get_details(soup)
    h = Handler();
    h.handle()
