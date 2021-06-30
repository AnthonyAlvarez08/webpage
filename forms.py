from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class CalculusForm(FlaskForm):

    degree = IntegerField('degree', validators=[DataRequired()])
    coeffs = StringField('coefficients', validators=[DataRequired(), Length(min=1)])
    submit = SubmitField('Submit')