from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'CST Docker Rajinder'

@app.route('/about')
def hello_world():
    return 'About Rajinder'

@app.route('/create')
def hello_world():
    return 'Create Rajinder'

if __name__== '__main__':
    app.run(host="0.0.0.0",debug=True)