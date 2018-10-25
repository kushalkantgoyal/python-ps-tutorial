import os
from datetime import datetime
from logging import DEBUG

from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from forms import BookmarkForm

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.logger.setLevel(DEBUG)
app.config['SECRET_KEY'] = '\xa8K\xd8]\x1cu;^&\t\xe0\xea/\xa6t\x7f\xfbs\x82\x99b\x97\xec\xdc'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
db = SQLAlchemy(app)

import models

bookmarks = []


def store_bookmark(url, desc):
    bookmarks.append(dict(
        url=url,
        user="kushal",
        description=desc,
        date=datetime.utcnow()
    ))


def get_last_existing_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]


@app.route('/')
def index():
    return render_template('index.html', title='Title passed from controller', text='Text passed from controller',
                           existing_bookmarks=models.Bookmark.get_latest_by_date(3))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        bm = models.Bookmark(url=url, description=description)
        db.session.add(bm)
        db.session.commit()
        store_bookmark(url, description)
        flash("Stored Bookmark '{}'".format(description))
        # app.logger.debug('stored url: '+ url)
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=False)
