from flask import Flask
from data import filmy


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/filmy')
def get_films():
    return render_template('filmy.html', filmy=filmy)

if __name__ == '__main__':
    app.run(debug=True)

