from flask import Blueprint, render_template, request, g, session, abort, Markup
import markdown

blog = Blueprint('blog', __name__, url_prefix="/blog",
                 template_folder="../templates")


def row_2_blog(row):
    return dict(id=row[0], title=row[1], content=Markup(markdown.markdown(row[2])), contentsrc=row[2], userid=row[3], createdate=row[4])


@blog.route("/", defaults={'page': 1})
@blog.route("/page/<page>")
def view_posts(page):
    rs = g.db.execute(
        'select * from blog order by id desc limit ?,10', [(page - 1) * 10])
    posts = [row_2_blog(row) for row in rs.fetchall()]
    return render_template("post_list.html", posts=posts)


@blog.route("/new", methods=["GET"])
def new_post_page():
    return render_template("newpost.html")


@blog.route("/new", methods=["POST"])
def new_post_api():
    g.db.execute("insert into blog values(null,?,?,?,date('now'))", [
                 request.form['title'], request.form['content'], session['user']['id']])
    g.db.commit()
    if request.form['content'] and request.form['title']:
        return "OK"
    else:
        return "false"


@blog.route("/single/<id>")
def view_single_post(id):
    rs = g.db.execute("select * from blog where id = ?", [id])
    if rs.arraysize > 0:
        tmp = rs.fetchone()
        post = {"id": tmp[0], "title": tmp[1], "content": Markup(markdown.markdown(tmp[2])), "contentsrc": tmp[
            2], "userid": tmp[3], "createdate": tmp[4]}
        return render_template("single_post.html", post=post)
    else:
        abort(404)
