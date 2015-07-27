import requests
import sys
from time import time
from wiki_JSON import wiki_json, categories, is_ambiguous, is_dead, was_born

def dead(name):
    if name:
        try: 
            url = wiki_json(name)
            r = requests.get(url)
            data = categories(r)
            if is_ambiguous(data):
                print "Not sure who you're talking about"
            elif is_dead(data):
                print "{0} is dead".format(name.title())
            elif was_born(data):
                print "{0} is alive".format(name.title())
            else:
                print "No Birth date / Not a person"
        except KeyError:
            print "Wikipedia page does not exist"
    else:
        print "Please enter a name (e.g. \"James Brown\" or \"Mark E. Smith\""
        
if __name__ == "__main__":
    args = sys.argv[:]
    script = args.pop(0)
    name = ' '.join(args)
    t0 = time()
    dead(name)
    t1 = time()
    print "Calling Wikipedia API took {0} seconds".format(t1-t0)

   