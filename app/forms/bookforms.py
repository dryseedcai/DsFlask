from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange


class BookSearchForm(Form):
    q = StringField(validators=[Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=999)], default=1)
