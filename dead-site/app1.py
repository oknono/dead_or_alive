from flask import Flask, render_template
import requests
from wiki_request import *

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index( name = "Bono"):
    #name = name.strip().title()
    #print "passed a name, name is {}".format(name)
    r = requests.get(wiki_json(name))
    result = categories(r)
    message = name + " " + r.status_code
        #elif is_ambiguous(result):
        #   message = "{} is an ambiguous name".format(name.title())
        #elif is_dead(result):
        #    message = "{} is dead".format(name.title())
        #elif was_born(result):
        #   message = "{} is still alive".format(name.title())
        #else:
        #    message = "Wikipedia does not recognize {} as a person".format()    
    #else:
    #    print "Did not pass a name"
    #    name = ""
    #    message = "please append name of person to URL. E.g. \"deadyet.xyz/james brown\""  

    return render_template('index.html', name=name, message=message)

if __name__ == '__main__':
    app.run()
