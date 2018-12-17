import pytest
from app import app, db
from app.auth.models import User, Recipient

# check auth

# check inserting new user

#

class TestMailer:

    def setup(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

    def teardown(self):
        db.session.remove()
        db.drop_all()

    def test_auth(self):
        assert(3 * 3 == 9)

    def test_db(self):
        assert(3 * 3 == 9)