import sys
import requests
from bs4 import BeautifulSoup

def dead(name):
    url = wiki_url(name)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    if soup.find_all("a", text="disambiguation"):
        print "Name is ambiguous"
    elif soup.find_all("th", text="Died"):
	    print "{0} is dead".format(name)
    else:
	    print "{0} is still alive".format(name)

def wiki_url(name):
    name = name.split()
    url = 'https://en.wikipedia.org/wiki/'
    for index in range(len(name)):
        element = name[index]
        url += element
        if index < len(name) - 1:
            url += '_'
    return url

if __name__ == "__main__":
    try:
        args = sys.argv[:]
        script = args.pop(0)
        name = args.pop(0)
        dead(name)

    except IndexError:
        print "Please enter a name (e.g. \"James Brown\" or \"Mark E Smith\")"
        exit(1)
