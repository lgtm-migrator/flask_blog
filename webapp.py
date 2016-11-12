from flask import Flask
from controller.home import home
from controller.blog import blog

app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(blog)

if __name__  == '__main__':
    app.run()