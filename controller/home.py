from flask import Blueprint, render_template, request, g, url_for, redirect, session

home = Blueprint('home', __name__)


@home.route("/")
def home_page():
    return render_template("home.html",title="Home")


@home.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html', title="Login")


@home.route('/login', methods=["POST"])
def login_api():
    rs = g.db.execute("select * from user where username = ? and password = ?",
                      [request.form['username'], request.form['password']])
    if rs.arraysize > 0:
        tmp = rs.fetchone()
        session['user'] = {"id": tmp[0], "username": tmp[1]}
        return redirect(url_for('home.home_page'))
    else:
        return redirect(url_for('home.login_page'))


@home.route('/logout')
def logout_api():
    session.pop('user', None)
    return redirect(url_for('home.login_page'))


@home.route('/about')
def about_page():
    return render_template('about.html')