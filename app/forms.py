from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, RadioField, SubmitField
from wtforms.validators import InputRequired, DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', [InputRequired()])
    password = PasswordField('Password', [InputRequired()])


class EmailSenderForm(FlaskForm):
    recipients = RadioField('Choose recipients',
                            choices=[('1', 'ALL OLAP USERS'), ('2', 'OSS'), ('3', 'Достаточность')])
    subject = StringField('Subject', validators=[DataRequired()])
    body = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')
