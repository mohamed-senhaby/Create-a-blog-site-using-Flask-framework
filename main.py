from flask import Flask, render_template
from post import Post
import requests

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url=blog_url)
blog_data = response.json()

all_posts = []
for blog in blog_data:
    posts = Post(blog["id"], blog["body"], blog["title"], blog["subtitle"])
    all_posts.append(posts)

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", bl=all_posts)


@app.route('/post/<int:num>')
def post_content(num):
    post = None
    for blog_post in all_posts:
        if blog_post.id == num:
            post = blog_post
    return render_template("post.html", s_post=post)


if __name__ == "__main__":
    app.run(debug=True)
