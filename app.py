from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'CST Docker'

@app.route('/about')
def hello_world():
    return 'About CST Docker'

if __name__== '__main__':
    app.run(host="0.0.0.0",debug=True)