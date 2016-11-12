from flask import Flask
from contextlib import contextmanager
from flask import g 
from controller.home import home
from controller.blog import blog
import sqlite3


app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(blog)
app.secret_key = 'A0Zr98j/3yX fdsafdsafdasfsad'

def connect_db():
    return sqlite3.connect("fblog.db")

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

if __name__  == '__main__':
    app.run(debug=True,use_debugger=False,use_reloader=False)