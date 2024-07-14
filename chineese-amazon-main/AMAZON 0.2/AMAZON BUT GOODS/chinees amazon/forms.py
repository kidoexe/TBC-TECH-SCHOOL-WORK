from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, SubmitField, BooleanField, PasswordField, FloatField, URLField, SelectField, EmailField
from flask_wtf.file import FileField
from wtforms.validators import DataRequired, Length, EqualTo 


class AddProduct(FlaskForm):
    name = StringField("Product name", validators=[DataRequired()])
    price = FloatField("Price", validators=[DataRequired()])
    text = StringField("Text", validators=[DataRequired()])
    submit = SubmitField("Submit")



class RegisterUser(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")
    

class LoginUser(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

