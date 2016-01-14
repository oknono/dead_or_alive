from flask import Flask, render_template, jsonify
import requests
from wiki_request import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
# @app.route('/<name>')
def index(name = None):
    if name:
        result = Wiki_Person(name)
        if result.is_ambiguous():
            message = "{} is an ambiguous name".format(name)
        elif result.is_person():
            if result.is_dead():
                message = "{} is dead".format(name)
            else:
                message = "{} is still alive".format(name)
        else:
            message = "{} is not a person or an unknown person".format(name)
    else:
        name = ""
        message = "please append name of person to URL. E.g. \"deadyet.xyz/james brown\""  

    return render_template('index.html', name=name, message=message, )

@app.route('/api/<name>') 
def api(name = None):
    result = Wiki_Person(name)
    if result.is_person():
        if result.is_dead():
            is_dead = True
        else:
            is_dead = False
    else:
        is_dead = None  
    return jsonify({"is_dead" : is_dead})

if __name__ == '__main__':
    app.run()