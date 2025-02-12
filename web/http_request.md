### http request
#### header
- general format is same between request and response
- you can define request method (GET, POST, .. etc), HTTP version, status code and message

#### redirect
- status code is 3XX (codes are defined in https://httpwg.org/specs/rfc9110.html#overview.of.status.codes, including other classes.)
- i,e implementation sample in Flask
- If you access [server-url]/redirect, http request destination is redirected to [server-url]/

```python
from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World!"


@app.route('/redirect')
def redirect_to_home():
    return redirect('/')


@app.route('/notfound')
def not_found():
    return "404 Not Found", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

```

#### Cache-Control
- this header can define various types of cache.