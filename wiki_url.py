from BeautifulSoup import *

def name_to_wiki_url(name):
    name = name.replace(' ', '_')
    url = 'https://en.wikipedia.org/wiki/'
    return url + name

def not_exist(name):
	return name.find("div", {"class" : "noarticletext"})

def is_ambiguous(name):
	return name.find("a", text="disambiguation")
        
def print_links(doc, name):
    links = doc.find_all('a')
    name_url = "/wiki/" + name.split()[0]
    for link in links:
        if link.has_attr('href') and link['href'].startswith(name_url):
            result =  link['href']
            stripped_result = result[6:].replace('_', ' ')
            if stripped_result != name:
                print stripped_result

def is_dead(name):
	return name.find("th", text="Died")
        