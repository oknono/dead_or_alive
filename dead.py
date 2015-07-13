import sys
import requests
from bs4 import BeautifulSoup

def dead(name):
    name = name.title()
    url = wiki_url(name)
    r = requests.get(url)
    name_list = name.split()
    first_name = name_list[0]
    soup = BeautifulSoup(r.text, "lxml")
    if soup.find_all("a", text="disambiguation"):
        print "Name is ambiguous, try one of the following:"
        name_url = "/wiki/" + first_name
        for link in soup.find_all('a'):
            if link.has_attr('href') and link['href'].startswith(name_url):
                result =  link['href']
                stripped_result = result[6:].replace('_', ' ')
                if stripped_result != name:
                    print stripped_result
    elif soup.find_all("th", text="Died"):
	    print "{0} is dead".format(name)
    else:
	    print "{0} is still alive".format(name)

def wiki_url(name):
    name = name.replace(' ', '_')
    url = 'https://en.wikipedia.org/wiki/'
    return url + name

if __name__ == "__main__":
    try:
        args = sys.argv[:]
        script = args.pop(0)
        name = args.pop(0)
        dead(name)

    except IndexError:
        print "Please enter a name (e.g. \"James Brown\" or \"Mark E. Smith\")"
        exit(1)
