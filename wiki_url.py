def name_to_wiki_url(name):
    name = name.replace(' ', '_')
    url = 'https://en.wikipedia.org/wiki/'
    return url + name