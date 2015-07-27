def wiki_json(name):
    url = 'https://en.wikipedia.org/w/api.php?action=query&titles={0}&continue=&prop=categories&format=json'.format(name)
    return url

def categories(response):
	return response.json()["query"]["pages"].values()[0]["categories"]

def is_ambiguous(d):
    for item in d:
        if 'disambiguation' in item["title"]:
            return True
    return False
     
def is_dead(d):
    for item in d:
        if 'deaths' in item["title"]:
            return True
    return False

def was_born(d):
    for item in d:
        if 'births' in item["title"]:
            return True
    return False
    
      