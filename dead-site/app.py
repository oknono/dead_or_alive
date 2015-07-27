from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = "Dit is de index"     
    return render_template('index.html', result=result)

@app.route('/<person>')
def name(person):
    result = "<person>"
    render_template('index.html', result=person)


if __name__ == '__main__':
    app.run()
