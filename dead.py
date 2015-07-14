import sys
import requests
from bs4 import BeautifulSoup
import wiki_url

def dead(name):
    name = name.title()
    url = wiki_url.name_to_wiki_url(name)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    if soup.find("div", {"class" : "noarticletext"}): 
        print "I don't know that person"
    elif soup.find("a", text="disambiguation"):
        print "Name is ambiguous, try one of the following:"
        name_url = "/wiki/" + name.split()[0]
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

if __name__ == "__main__":
    try:
        args = sys.argv[:]
        script = args.pop(0)
        name = ' '.join(args)
        dead(name)

    except IndexError:
        print "Please enter a name (e.g. \"James Brown\" or \"Mark E. Smith\""
        exit(1)
