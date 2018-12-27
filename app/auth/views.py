import ldap
from flask import request, render_template, flash, redirect, url_for, Blueprint, g
from flask_login import current_user, login_user, logout_user, login_required
from app import login_manager, db, app
from app.auth.models import User, Recipient, Event
from app.forms import LoginForm, EmailSenderForm
from app.email import send_email


auth = Blueprint('auth', __name__)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@auth.before_request
def get_current_user():
    g.user = current_user


@auth.route('/', methods=['GET', 'POST'])
@auth.route('/home', methods=['GET', 'POST'])
def home():
    form = EmailSenderForm()
    events = Event.query.all()
    if form.validate_on_submit():
        recipients = [str(i) for i in Recipient.query.filter_by(group_id=form.recipients.data).all()]
        print('Sending to: {}'.format(recipients))
        print('Sending copy to: {}'.format(app.config['COPY_GROUP']))
        send_email(form.subject.data, app.config['SENDER'], recipients, app.config['COPY_GROUP'], form.body.data, form.body.data)
        event = Event(owner=current_user.id, recipients=form.recipients.data, title=form.subject.data)
        db.session.add(event)
        db.session.commit()
        flash('Your message was send!')
        return redirect(url_for('auth.home'))
    return render_template('home.html', form=form, events=events)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in.')
        return redirect(url_for('auth.home'))

    form = LoginForm()

    if request.method == 'POST' and form.validate():
        username = request.form.get('username')
        password = request.form.get('password')

        try:
            User.try_login(username, password)
        except ldap.INVALID_CREDENTIALS:
            flash(
                'Invalid username or password. Please try again.',
                'danger')
            return render_template('login.html', form=form)

        user = User.query.filter_by(username=username).first()

        if not user:
            user = User(username, password)
            db.session.add(user)
            db.session.commit()
        login_user(user)
        return redirect(url_for('auth.home'))

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.home'))
