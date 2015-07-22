def wiki_json(name):
    name = name.strip().title()
    url = 'https://en.wikipedia.org/w/api.php?action=query&titles={0}&continue=&prop=categories&format=json'.format(name)
    return url

def birth(response):
	return response.json()["query"]["pages"].values()[0]["categories"][0]

def death(response):
	return response.json()["query"]["pages"].values()[0]["categories"][1]

def is_ambiguous(dic):
	return 'disambiguation' in dic["title"]
           
def is_dead(dic):
	return 'deaths' in dic["title"]

def was_born(dic):
    return 'births' in dic["title"]
      