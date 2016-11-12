from flask import Blueprint

blog = Blueprint('blog', __name__,url_prefix="/blog")


@blog.route("/<page>")
def viewposts(page):
    return page
