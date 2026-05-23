from flask import Flask

app = Flask(__name__)

@app.route('/')
def cart():
    return {
        "cart_items": 2
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)