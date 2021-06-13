from flask import Flask

app = Flask(__name__)
port = 5001

@app.route('/')
def hello_world():
    return "<h1> Tá funfante na porta {0}</h1>".format(port)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)