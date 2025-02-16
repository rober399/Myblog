from flask import render_template, flash, redirect, url_for
from app import app, db
from app.models import Post
from app.forms import PostForm

@app.route('/')
@app.route('/index')
def index():
    posts = Post.query.all()
    return render_template('index.html', title='Home', posts=posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been added.')
        return redirect(url_for('index'))
    return render_template('add.html', title='Add Post', form=form)
