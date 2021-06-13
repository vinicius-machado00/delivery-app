from flask import Flask
from modules_examples.viewer import viewer_bp
from modules_examples.order import order_bp

app = Flask(__name__)
app.register_blueprint(viewer_bp)
app.register_blueprint(order_bp)

@app.route('/')
def hello_world():
    return "<h1> Tá funfante</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)