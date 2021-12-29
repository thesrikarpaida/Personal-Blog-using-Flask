from flask import Flask, render_template, abort
from model import links, db

app = Flask(__name__)


# Return text files for the post data
def post_data(i):
    filename = "static/" + str(i) + ".txt"
    with open(filename) as f:
        text = f.read()
    return text


# Index page of the site
@app.route("/")
def index():
    return render_template("index.html",
                           varia=links,
                           paths=db)

'''
# About page for the site
# You can remove the quotes if you want to insert an about page.
@app.route("/about")
def about():
    return render_template("about.html")
'''

# Individual Post
@app.route("/<postName>/<int:i>")
def posts(i,postName):
    try:
        card = db[i]
        content = post_data(i)
        return render_template("posts.html",
                               card=card,
                               cont=content)
    except IndexError:
        abort(404)
