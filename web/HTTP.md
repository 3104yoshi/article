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
- it's used for below purposes
  - session management
  - personalization
  - tracking

- you can set some value to cookie, and check it from Application tab in browser's developer tool.

```python
@app.route('/setcookie')
def set_cookie():
    response = make_response("Cookie is set")
    response.set_cookie('username', 'user1')
    return response
```

##### session management example in framework for authentification
- you can take a look Flask-login framework as reference.
1. The web server will creates cookie including session id specific to user when user access to the web site for the first time.
2. User receive the cookie
3. When user send the login information and it is authentificated by server, server regard the session id as authentificated one.
4. User sent http request with cookie including authentificated session id, server can return contents limited to the authentificated user 

```python
from flask import Flask, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)

# you ought to generate secret key with below command, ref: https://flask.palletsprojects.com/en/latest/quickstart/#sessions
# $ python -c 'import secrets; print(secrets.token_hex())'
app.secret_key = 'supersecretkey'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Dummy user database
users = {'user1': {'password': 'password123'}}


class User(UserMixin):
    def __init__(self, id):
        self.id = id


@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None


@app.route('/')
def home():
    return '''
        <h1>Hello, World!</h1>
        <form action="/login" method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username"><br><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password"><br><br>
            <input type="submit" value="Login">
        </form>
        <br>
        <form action="/protected" method="get">
            <input type="submit" value="Go to Protected Page">
        </form>
    '''


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username]['password'] == password:
        user = User(username)
        login_user(user)
        return redirect(url_for('protected'))
    return "Invalid credentials", 401


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/protected')
@login_required
def protected():
    return f'Hello, {current_user.id}! This is a protected route.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

```