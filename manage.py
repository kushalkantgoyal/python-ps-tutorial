from flask_script import Manager, prompt_bool

from models import User
from thermos import app, db

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()
    u1 = User(username='kushal', email='kkg@gmail.com')
    u2 = User(username='kushal2', email='kkg2@gmail.com')
    db.session.add(u1)
    db.session.add(u2)
    db.session.commit()
    print 'Initialized the database'


@manager.command
def dropdb():
    if prompt_bool(
            "Are you sure, you want to drop the database? You'll lose all your data."):
        db.drop_all()
        print 'Dropped the database'


if __name__ == '__main__':
    manager.run()
