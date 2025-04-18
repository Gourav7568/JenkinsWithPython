from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Azure!"

if __name__ == '__main__':
    # It's good practice to enable debug mode only in development
    app.run(host='0.0.0.0', port=5000, debug=True)
