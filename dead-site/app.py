from flask import Flask, render_template
import requests
from wiki_request import *

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index( name = None):
    if name:
        name = name.strip().title()
        r = requests.get(wiki_json(name))
        try: 
            result = categories(r)
            if is_ambiguous(result):
                message = "{} is an ambiguous name".format(name)
            elif is_dead(result):
                message = "{} is dead".format(name)
            elif was_born(result):
                message = "{} is still alive".format(name)
            else:
                message = "{} doesn't seem to be a person".format(name)
        except:
            message = "Wikipedia is not familiar with this name"
    else:
        name = ""
        message = "please append name of person to URL. E.g. \"deadyet.xyz/james brown\""  

    return render_template('index.html', name=name, message=message)

if __name__ == '__main__':
    app.run()
