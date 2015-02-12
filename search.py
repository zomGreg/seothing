import mechanize
import sys
import time
from bs4 import BeautifulSoup
import re
import argparse

def googlesearch(search_term):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_equiv(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0')]
    br.open('http://www.google.com/')

    # do the query
    br.select_form(name='f')
    br.open("https://www.google.com/search?q=%s&num=50" % search_term.replace(' ', '+'))
    data = br.response()
    soup = BeautifulSoup(data.read())
    links = soup.select('.r a')

    results = [l['href'] for l in links]

    return results

def yahoosearch(search_term):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_equiv(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0')]
    br.open('http://search.yahoo.com/')

    # do the query
    br.select_form(name='s')
    br.open("https://search.yahoo.com/search?p=%s&pz=40" % search_term.replace(' ', '+'))
    data = br.response()
    soup = BeautifulSoup(data.read())

    links = soup.findAll('a', {"class" : "td-u"})

    results = [l['href'] for l in links]

    return results

def bingsearch(search_term):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_equiv(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0')]
    br.open('http://search.yahoo.com/')

    # do the query
    br.select_form(name='s')
    br.open("http://www.bing.com/search?count=50&q=%s" % search_term.replace(' ', '+'))
    data = br.response()
    soup = BeautifulSoup(data.read())

    li = soup.findAll('li', {'class': 'b_algo'})

    results = [l.a['href'] for l in li]

    return results

def process_terms(f, *args, **kwargs):

    search_terms = [search_term.strip("\n").replace(' ', '+') for search_term in f.readlines()]

    print '{:36} {:20} {:20}'.format('Search Term', 'dell.com', 'enstratius.com')
    for s in search_terms:
        if kwargs['google']:
            output = googlesearch(s)
        elif kwargs['yahoo']:
            output = yahoosearch(s)
        elif kwargs['bing']:
            output = bingsearch(s)

        dell_idx = [i for i, item in enumerate(output) if re.search('dell.com', item)]
        enstratius_idx = [i for i, item in enumerate(output) if re.search('enstratius.com', item)]
        enstratus_idx = [i for i, item in enumerate(output) if re.search('enstratus.com', item)]
        space_string = s.replace('+', ' ')
        print '{:36} {:20} {:20}'.format(space_string, str(dell_idx).strip('[]'), str(enstratius_idx).strip('[]'))

def main():
    parser = argparse.ArgumentParser(description="DCM SEO Thing")
    parser.add_argument('input', type=argparse.FileType('r'),
                        help='Text file containing search terms, one per line.', metavar='input.txt')
    parser.add_argument('--google', '-g', action='store_true', help='Run the google search.')
    parser.add_argument('--yahoo', '-y', action='store_true', help='Run the yahoo search.')
    parser.add_argument('--bing', '-b', action='store_true', help='Run the bing search.')

    args = parser.parse_args()

    google, yahoo, bing = args.google, args.yahoo, args.bing
    process_terms(args.input, google=google, yahoo=yahoo, bing=bing)

if __name__ == '__main__':
    main()
