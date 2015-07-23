import sys
import requests
from BeautifulSoup import BeautifulSoup
import wiki_url

def dead(name):
    name = name.title()
    url = "https://en.wikipedia.org/w/api.php?action=query&titles={0}&continue=&prop=categories&format=json".format(name)
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    if wiki_url.not_exist(soup):
        print "I don't know this person"   
    elif wiki_url.is_ambiguous(soup):
        print "Name is ambiguous, try one of the following:"
        wiki_url.print_links(soup, name)
    elif wiki_url.is_dead(soup):
        print "{0} is dead".format(name)
    else:
	    print "{0} is still alive".format(name)

if __name__ == "__main__":
    try:
        args = sys.argv[:]
        script = args.pop(0)
        name = ' '.join(args)
        dead(name)

    except IndexError:
        print "Please enter a name (e.g. \"James Brown\" or \"Mark E. Smith\""
        exit(1)
