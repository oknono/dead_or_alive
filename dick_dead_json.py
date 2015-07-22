from time import time
import requests 

def dick_dead_json():
    r = requests.get('https://en.wikipedia.org/w/api.php?action=query&titles=Dick%20Cheney&continue=&prop=categories&format=json')
    text =  r.json()["query"]["pages"].values()[0]["categories"][1]
    if 'deaths' in text["title"]:
        print "He's dead!"
    else:
        print "Not yet!"

if __name__ == "__main__":
	t0 = time()
	dick_dead_json()
	t1 = time()
	print "Using JSON API took {0} seconds".format(t1-t0)
