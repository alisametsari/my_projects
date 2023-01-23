from flask import Flask

app = Flask(__name__)

@app.route('/')       #decorater
def hello():
    return "sayfama hoş geldiniz"

@app.route('/second')
def second():
    return 'ben ali samet '

@app.route('/third/subthird')
def third():
    return 've bu benim sayfam'

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page is {id}'








if __name__ == '__main__':
    app.run(debug=True)       #hiçbir şey yapılmazsa 5000 portta çalışır 