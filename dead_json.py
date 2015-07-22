import requests
import sys
from wiki_request import wiki_json, birth, death, is_ambiguous, is_dead, was_born

def dead(name):
    name = name.strip().title()
    url = wiki_json(name)
    r = requests.get(url)
    try:
        born = birth(r)
        dead = death(r)
        if is_ambiguous(born):
            print "Not sure who you're talking about"
        elif is_dead(dead):
            print "{0} is dead".format(name)
        elif was_born(born):
            print "{0} is alive".format(name)
        else:
            print "No Birth date / Not a person"

    except KeyError:
        print "Person/Wikipediapage does not exist"

if __name__ == "__main__":
    try:
        args = sys.argv[:]
        script = args.pop(0)
        name = ' '.join(args)
        dead(name)

    except IndexError:
        print "Please enter a name (e.g. \"James Brown\" or \"Mark E. Smith\""
        exit(1)