"""forms for app"""


from flask_wtf import FlaskForm
# import your own form types and validators
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
