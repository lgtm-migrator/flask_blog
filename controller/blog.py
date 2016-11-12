from flask import Blueprint,render_template

blog = Blueprint('blog', __name__,url_prefix="/blog",template_folder="../templates")


@blog.route("/<page>")
def viewposts(page):
    return page

@blog.route("/new")
def newpost():
    return render_template("newpost.html")