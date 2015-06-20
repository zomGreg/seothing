import mechanize
import sys
import time
from bs4 import BeautifulSoup
import re
import argparse
import json

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

    search_string = 'Search Term'
    dell_term = 'dell.com'
    enstratius_term = 'enstratius.com'

    result_list=[]
    result_counts=[]
    result_dict={}
    results = {}

    for s in search_terms:
        if kwargs['google']:
            output = googlesearch(s)
            search_engine = "google"
        elif kwargs['yahoo']:
            output = yahoosearch(s)
            search_engine = "yahoo"
        elif kwargs['bing']:
            output = bingsearch(s)
            search_engine = "bing"

        dell_idx = [i for i, item in enumerate(output) if re.search('dell.com', item)]
        enstratius_idx = [i for i, item in enumerate(output) if re.search('enstratius.com', item)]
        enstratus_idx = [i for i, item in enumerate(output) if re.search('enstratus.com', item)]
        space_string = s.replace('+', ' ')

        if len(dell_idx) == 0:
            dell = ""
        else:
            dell = str(dell_idx).strip('[]')

        if len(enstratius_idx) == 0:
            enstratius = ""
        else:
            enstratius = str(enstratius_idx).strip('[]')

        if dell == 'Not Found':
            length_dell=0
        else:
            length_dell=len(dell)

        if enstratius == 'Not Found':
            length_enstratius = 0
        else:
            length_enstratius = len(enstratius)

        result_counts.append({"label": str(space_string), "value": length_dell})

        result_list.append({"search_term": str(space_string), "results": {"dell.com": dell, "enstratius.com": enstratius}})

        result_dict[space_string] = {"dell.com": dell, "enstratius.com": enstratius}

    counts = {"key": "Search Counter", "values": result_counts}

    # with open ('./tmp/counts.json', 'w') as g:
    #     try:
            # data = json.dumps(counts)
            # g.write(data)
        # except ValueError:
        #     pass

    results[search_engine] = result_list
    with open('./tmp/'+search_engine+'.json', 'w') as f:
        try:
            data = json.dumps(results)
            f.write(data)
        except ValueError:
            pass

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
