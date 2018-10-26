from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url


class BookmarkForm(Form):
    url = URLField('Please enter the url for bookmarks:', validators=[DataRequired(), url()])
    description = StringField('Add an optional description:')

    def validate(self):
        if not self.url.data.startswith("http://") or self.url.data.startswith("https://"):
            self.url.data = "http://" + self.url.data

        if not Form.validate(self):
            return False

        if not self.description.data:
            self.description.data = self.url.data

        return True

class LoginForm(Form):
    username = StringField('Your Username:', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')