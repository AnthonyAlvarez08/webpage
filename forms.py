from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class CalculusForm(FlaskForm):

    degree = StringField('degree', validators=[DataRequired()])
    coeffs = StringField('coeffs', validators=[DataRequired()])
    submit = SubmitField('come up')