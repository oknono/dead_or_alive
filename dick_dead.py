import requests 
from bs4 import BeautifulSoup
from wiki_url import is_dead

def dick_dead():
    r = requests.get('https://en.wikipedia.org/wiki/Dick_Cheney')
    soup = BeautifulSoup(r.text, "lxml")
    if is_dead(soup):
        print "Yes, Dick is dead!"
    else:
        print "Not yet..."   

if __name__ == "__main__":
	dick_dead()
