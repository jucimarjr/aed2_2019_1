from flask_wtf import FlaskForm
from datetime import date
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired

#INSERT INTO users (username, password,admin ) VALUES ("lucas.botinelly", "paocommanteiga", 1)

class Form(FlaskForm):
    target = StringField("Target", validators = [DataRequired()])
    mutation = FloatField("Rate", validators = [DataRequired()])
    gen_size = IntegerField ("Generation Size", validators = [DataRequired()])
