import sys
import requests
from BeautifulSoup import BeautifulSoup
import wiki_url
from time import time

def dead(name):
    if name:
        url = wiki_url.name_to_wiki_url(name.title())
        r = requests.get(url)
        soup = BeautifulSoup(r.text)
        if wiki_url.not_exist(soup):
            print "I don't know this person"   
        elif wiki_url.is_ambiguous(soup):
            print "Name is ambiguous"
            #wiki_url.print_links(soup, name)
        elif wiki_url.is_dead(soup):
            print "{0} is dead".format(name.title())
        else:
	        print "{0} is still alive".format(name.title())
    else: 
        print "Please enter a name (e.g. \"James Brown\" or \"Mark E. Smith\""

if __name__ == "__main__":
    args = sys.argv[:]
    script = args.pop(0)
    name = ' '.join(args)
    t0 = time()
    dead(name)
    t1 = time()
    print "Scraping HTML with BS took {0} seconds".format(t1-t0)

