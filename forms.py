from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class CalculusForm(FlaskForm):

    degree = IntegerField('degree', validators=[DataRequired(), Length(min=1)])
    coeffs = StringField('coeffs', validators=[DataRequired(), Length(min=1)])
    submit = SubmitField('Submit')