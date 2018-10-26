from flask import render_template, flash, redirect, url_for

from forms import BookmarkForm
from models import Bookmark, User
from . import db, app


# def get_last_existing_bookmarks(num):
#     return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]

def get_logged_in_user():
    return User.query.filter_by(username='kushal').first()


@app.route('/')
def index():
    return render_template('index.html', title='Title passed from controller', text='Text passed from controller',
                           existing_bookmarks=Bookmark.get_latest_by_date(3))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        bm = Bookmark(user=get_logged_in_user(), url=url, description=description)
        db.session.add(bm)
        db.session.commit()
        flash("Stored Bookmark '{}'".format(description))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
