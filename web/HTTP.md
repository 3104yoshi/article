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
- There is 'Cache-Control' in HTTP request (implementation sample is below).
- If you access to root/image multiple times in an hour, you can get content without downloading image file again (status code is 304 ref: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/304).
- you can check the status code and transfered file size (The size gets small by caching. If you disable cache, the size gets bigger)

```python
@app.route('/image')
def serve_image():
    response = make_response(send_file('../img/large_image.jpg'))
    response.headers['Cache-Control'] = 'public, max-age=3600'
    return response
```

#### cookie
- ref: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
- A cookie is a small piece of data server sends to user's web browser.