from flask import Flask

app = Flask(__name__)

@app.route('/')
def sample():
    return "Hello World!"

def sample2():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)