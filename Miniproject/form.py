from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField)
from wtforms.validators import(DataRequired)

class GraphForm(FlaskForm):
    Equation=StringField("",validators=[DataRequired()])
    Submit=SubmitField("")